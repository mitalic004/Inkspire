from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Story

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

    return render(
        request,
        "writersarchive/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )