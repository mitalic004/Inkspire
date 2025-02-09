from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Story
from .forms import CommentForm, SubmissionForm

# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "writersarchive/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`writersarchive.Post`.

    **Context**

    ``post``
        An instance of :model:`writersarchive.Post`.

    **Template:**

    :template:`writersarchive/post_detail.html`
    """

    queryset = Story.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "writersarchive/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def submission_page(request):
    """
    Renders the Submission page
    """
    submission_form = SubmissionForm()

    return render(
        request,
        "writersarchive/submission.html",
        {
            "submission_form": submission_form
        },
    )