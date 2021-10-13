from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests (TestCase):

    def test_create_user_with_email_successful(self):
        '''successful creation: new user with an email'''

        email = 'dodo@gotoit.com'
        password = 'dodoTest007!'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''normalized: new user email'''

        email = 'dodo@GOTOIT.com'
        user = get_user_model().objects.create_user(email, 'dodoTest007!')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''raises error: creating user with no email'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'dodoTest007')

    def test_create_new_superuser(self):
        '''successful creation: new Superuser with an email'''

        user = get_user_model().objects.create_superuser(
               'dodo@gotoit.com',
               'dodoTest007!')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
