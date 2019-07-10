from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test if the creation of a new user is successful"""
        email = 'test30@gmail.com'
        password = 'test@#1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized"""
        email = 'test30@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test0123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Check create user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test456')

    def test_create_new_superuser(self):
        """ Test the creation of new superuser"""
        user = get_user_model().objects.create_superuser(
            'test30@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
