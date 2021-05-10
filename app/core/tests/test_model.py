from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_sucessful(self):
        """test creating a new user with email is sucessful"""
        email = "test@gmail.com"
        password = "Testpass1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        password = "Testpass1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test if creating a user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testpass1234')

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'Testpass1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
