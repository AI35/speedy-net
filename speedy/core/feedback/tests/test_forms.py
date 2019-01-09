from django.conf import settings as django_settings

from speedy.core.base.test.models import SiteTestCase
from speedy.core.base.test.decorators import only_on_sites_with_login
from speedy.core.feedback.tests.test_mixins import SpeedyCoreFeedbackLanguageMixin
from speedy.core.feedback.forms import FeedbackForm
from speedy.core.feedback.models import Feedback

if (django_settings.LOGIN_ENABLED):
    from speedy.core.accounts.tests.test_factories import ActiveUserFactory


@only_on_sites_with_login
class FeedbackFormTestCase(SiteTestCase, SpeedyCoreFeedbackLanguageMixin):
    def assert_form_text_field(self, form):
        self.assertTrue(expr=form.fields['text'].required)

    def test_feedback_form_for_visitor_displays_name_and_email(self):
        defaults = {
            'type': Feedback.TYPE_FEEDBACK,
        }
        form = FeedbackForm(defaults=defaults)
        self.assertListEqual(list1=list(form.fields.keys()), list2=self._feedback_form_all_the_required_fields_keys(user_is_logged_in=False))
        self.assertTrue(expr=form.fields['sender_name'].required)
        self.assertTrue(expr=form.fields['sender_email'].required)
        self.assert_form_text_field(form=form)

    def test_feedback_form_for_user_doesnt_require_name_and_email(self):
        user = ActiveUserFactory()
        defaults = {
            'type': Feedback.TYPE_FEEDBACK,
            'sender': user,
        }
        form = FeedbackForm(defaults=defaults)
        self.assertListEqual(list1=list(form.fields.keys()), list2=self._feedback_form_all_the_required_fields_keys(user_is_logged_in=True))
        self.assert_form_text_field(form=form)

    def test_form_save_for_abuse_report_as_user(self):
        user = ActiveUserFactory()
        other_user = ActiveUserFactory()
        data = {
            'text': "I personally don't like this user.",
        }
        defaults = {
            'type': Feedback.TYPE_REPORT_ENTITY,
            'sender': user,
            'report_entity': other_user,
        }
        form = FeedbackForm(data=data, defaults=defaults)
        self.assertTrue(expr=form.is_valid())
        feedback = form.save()
        self.assertEqual(first=feedback.sender, second=user)
        self.assertEqual(first=feedback.sender_name, second='')
        self.assertEqual(first=feedback.sender_email, second='')
        self.assertEqual(first=feedback.type, second=Feedback.TYPE_REPORT_ENTITY)
        self.assertEqual(first=feedback.report_entity_id, second=other_user.pk)
        self.assertIsNone(obj=feedback.report_file)
        self.assertEqual(first=feedback.text, second=data['text'])


