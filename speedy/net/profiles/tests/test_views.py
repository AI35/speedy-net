from speedy.core.test import TestCase, exclude_on_speedy_composer, exclude_on_speedy_mail_software
from django.test.client import RequestFactory
from django.views import generic

from speedy.net.accounts.tests.test_factories import UserFactory
from ..views import UserMixin


class UserMixinTestView(UserMixin, generic.View):
    def get(self, request, *args, **kwargs):
        return self


@exclude_on_speedy_composer
@exclude_on_speedy_mail_software
class UserMixinTextCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = UserFactory(slug='look-at-me', username='lookatme')
        self.other_user = UserFactory()

    def test_find_user_by_exact_slug(self):
        view = UserMixinTestView.as_view()(self.factory.get('/look-at-me/some-page/'), slug='look-at-me')
        self.assertEqual(first=view.get_user().id, second=self.user.id)

    def test_find_user_by_username(self):
        r = self.client.get('/l-o-o-k_a_t_m-e/')
        self.assertRedirects(response=r, expected_url='/look-at-me/', status_code=301)
