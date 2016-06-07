from django.test import TestCase

from speedy.net.accounts.test_factories import UserFactory
from .forms import RegistrationForm


class RegistrationFormTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'email@example.com',
            'slug': 'user',
            'gender': 1,
            'password1': 'password',
            'password2': 'password',
        }

    def test_required_fields(self):
        form = RegistrationForm({})
        required_fields = self.valid_data.keys()
        form.full_clean()
        self.assertFalse(form.is_valid())
        for field in required_fields:
            self.assertEqual('This field is required.', form.errors[field][0])

    def test_non_unique_primary_email(self):
        existing_user = UserFactory()
        existing_user.email_addresses.create(email='email@example.com')
        form = RegistrationForm(self.valid_data)
        self.assertEqual(form.errors['email'][0], 'This email is already in use.')

    def test_unavailable_slug(self):
        data = self.valid_data.copy()
        data['slug'] = 'admin'
        form = RegistrationForm(data)
        self.assertEqual(form.errors['slug'][0], 'This username is unavailable.')

    def test_passwords_mismatch(self):
        data = self.valid_data.copy()
        data['password2'] = 'haha'
        form = RegistrationForm(data)
        form.full_clean()
        self.assertEqual(form.errors['password2'][0], 'The two password fields didn\'t match.')
