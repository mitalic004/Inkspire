from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Story, Comment
from .forms import CommentForm, SubmissionForm
from slugify import slugify

# Create your views here.
class StoryList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "writersarchive/index.html"
    paginate_by = 6

# Display Post
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
    view to edit comments
    """
    if request.method == "POST":

        queryset = Story.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Delete Comment
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Story.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# Submission Page
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

    queryset = Story.objects

    if request.method == "POST":
        submission_form = SubmissionForm(data=request.POST)
        if submission_form.is_valid():
            post = submission_form.save(commit=False)
            post.author = request.user
            post.status = 0
            post.save()
            
            # # Create post slug
            # testslug = slugify(post.author) + slugify(post.title)
            # if testslug in queryset:
            #     slugnotunique = True
            #     i = 0
            #     while slugnotunique:
            #         tempslug = testslug
            #         tempslug += str(i)
            #         if tempslug in queryset:
            #             i += 1
            #         else:
            #             slugnotunique = False
            #             post.slug = tempslug
            #             break
            # else:
            #     post.slug = tempslug
                    

            messages.add_message(
                request, messages.SUCCESS,
                'Story submitted and awaiting approval.'
            )