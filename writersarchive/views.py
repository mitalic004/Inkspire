from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Story, Comment
from .forms import CommentForm, SubmissionForm


# Display Published Posts as a List on the Landing Page
class StoryList(generic.ListView):
    queryset = Story.objects.filter(status=1)
    template_name = "writersarchive/index.html"
    paginate_by = 6


# Display Post
@login_required
def post_detail(request, slug):
    """
    Display an individual :model:`writersarchive.Story`.

    **Context**

    ``post``
        An instance of :model:`writersarchive.Story`.

    **Template:**

    :template:`writersarchive/post_detail.html`
    """

    queryset = Story.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Submit Comment
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
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


# Edit Comment
def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":

        queryset = Story.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Only allows comment to be edited if the user is same as the commenter
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment Updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Delete Comment
def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    queryset = Story.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    # Only allows comment to be deleted if the user is same as the commenter
    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# Submission Page
@login_required
def submission_page(request):
    """
    Renders the Submission page
    """
    if request.method == "POST":
        submission_form = SubmissionForm(request.POST)
        if submission_form.is_valid():
            submission = submission_form.save(commit=False)
            submission.author = request.user
            submission.status = 0
            submission.save()
            # Successful Submission Message
            messages.add_message(
                request, messages.SUCCESS,
                'Story submitted and awaiting approval.'
            )
            return redirect("writersarchive/submission.html")
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting story!'
            )
    else:
        submission_form = SubmissionForm()

    return render(
        request, "writersarchive/submission.html",
        {"submission_form": submission_form}
    )
