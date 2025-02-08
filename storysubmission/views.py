from django.shortcuts import render
from .models import Submission
from .forms import SubmissionForm


def submission_page(request):
    """
    Renders the Submission page
    """
    submission_form = SubmissionForm()

    return render(
        request,
        "storysubmission/submission.html",
        {
            "submission_form": submission_form
        },
    )