from django.test import TestCase
from .forms import CommentForm, SubmissionForm

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

# Submission Form Tests
class TestSubmissionForm(TestCase):
    """
    Tests Submission
    """
    
    def test_submit_form_is_valid(self):
        """
        Test for all fields
        """
        form = SubmissionForm({
            'title': 'Story Title', 
            'summary': 'Story summary.', 
            'content': 'This is a story.', 
            'genre': ('Adventure', )
        })
        self.assertTrue(
            form.is_valid(), 
            msg="Form is not valid"
        )
    
    def test_submit_title_is_required(self):
        """
        Test for the 'title' field
        """
        form = SubmissionForm({
            'title': '', 
            'summary': 'Story summary.', 
            'content': 'This is a story.', 
            'genre': 'Adventure'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Title was not provided, but the form is valid"
        )

    def test_submit_summary_is_required(self):
        """
        Test for the 'summary' field
        """
        form = SubmissionForm({
            'title': 'Story Title', 
            'summary': '', 
            'content': 'This is a story.', 
            'genre': 'Adventure'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Summary was not provided, but the form is valid"
        )

    def test_submit_content_is_required(self):
        """
        Test for the 'content' field
        """
        form = SubmissionForm({
            'title': 'Story Title', 
            'summary': 'Story summary.', 
            'content': '', 
            'genre': 'Adventure'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Content was not provided, but the form is valid"
        )

    def test_submit_genre_is_required(self):
        """
        Test for the 'genre' field
        """
        form = SubmissionForm({
            'title': 'Story Title', 
            'summary': 'Story summary.', 
            'content': 'This is a story.', 
            'genre': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Genre was not provided, but the form is valid"
        )