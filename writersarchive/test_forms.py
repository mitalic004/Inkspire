from django.test import TestCase
from .forms import CommentForm


# Comment Form Tests
class TestCommentForm(TestCase):
    """
    Tests Comment Form
    """

    def test_comment_form_is_valid(self):
        """
        Test if a valid submission passes
        """
        comment_form = CommentForm({
            'rating': 4,
            'body': 'This is a great post.'
        })
        self.assertTrue(
            comment_form.is_valid(),
            msg='Form is not valid.'
        )

    def test_comment_form_is_empty(self):
        """
        Test if an empty submission passes
        """
        comment_form = CommentForm({
            'rating': 0,
            'body': ''
        })
        self.assertFalse(
            comment_form.is_valid(),
            msg='Message was not provided, but the form is valid.'
        )

    def test_comment_form_is_imcomplete(self):
        """
        Test if a submission without all fields filled passes
        """
        comment_form = CommentForm({
            'body': 'This is a great post.'
        })
        self.assertFalse(
            comment_form.is_valid(),
            msg='Fields were missing, but the form is valid.'
        )
