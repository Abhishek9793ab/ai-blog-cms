from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from blog.forms import CategoryForm, TagForm
from blog.models import Blog, Category, Tag, Comment
from blog.seo import seo_audit


def staff_required(view):

    return user_passes_test(
        lambda u: u.is_authenticated and u.is_staff,
        login_url="/accounts/login/",
    )(view)


@login_required
def dashboard_home(request):

    context = {

        "total_blogs":
            Blog.objects.count(),

        "published_blogs":
            Blog.objects.filter(
                status="published"
            ).count(),

        "draft_blogs":
            Blog.objects.filter(
                status="draft"
            ).count(),

        "total_views":
            sum(
                Blog.objects.values_list(
                    "views",
                    flat=True,
                )
            ),

        "total_users":
            User.objects.count(),

        "total_comments":
            Comment.objects.count(),

        "pending_comments":
            Comment.objects.filter(
                status="pending"
            ).count(),

        "total_categories":
            Category.objects.count(),

        "total_tags":
            Tag.objects.count(),

        "recent_blogs":
            Blog.objects.select_related(
                "author",
                "category",
            )[:8],
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )


@login_required
def blogs(request):

    qs = Blog.objects.select_related(
        "author",
        "category",
    )

    if not request.user.is_staff:

        qs = qs.filter(
            author=request.user
        )

    q = request.GET.get(
        "q",
        "",
    ).strip()

    status = request.GET.get(
        "status",
        "",
    ).strip()

    if q:

        qs = qs.filter(
            title__icontains=q
        )

    if status in {
        "draft",
        "published",
    }:

        qs = qs.filter(
            status=status
        )

    return render(
        request,
        "dashboard/blogs.html",
        {
            "blogs": qs,
            "query": q,
            "status": status,
        },
    )


@staff_required
def comments(request):

    items = Comment.objects.select_related(
        "blog",
        "user",
    )

    return render(
        request,
        "dashboard/comments.html",
        {
            "comments": items,
        },
    )


@staff_required
@require_POST
def comment_action(
    request,
    pk,
    action,
):

    comment = get_object_or_404(
        Comment,
        pk=pk,
    )

    if action in {
        "approved",
        "rejected",
        "pending",
    }:

        comment.status = action

        comment.save(
            update_fields=[
                "status"
            ]
        )

        messages.success(
            request,
            f"Comment marked {action}.",
        )

    return redirect(
        "dashboard:comments"
    )


@staff_required
def categories(request):

    items = Category.objects.all()

    form = CategoryForm(
        request.POST or None
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Category created.",
            )

            return redirect(
                "dashboard:categories"
            )

    return render(
        request,
        "dashboard/categories.html",
        {
            "categories": items,
            "form": form,
        },
    )


@staff_required
@require_POST
def category_delete(request, pk):

    get_object_or_404(
        Category,
        pk=pk,
    ).delete()

    messages.success(
        request,
        "Category deleted.",
    )

    return redirect(
        "dashboard:categories"
    )


@staff_required
def tags(request):

    items = Tag.objects.all()

    form = TagForm(
        request.POST or None
    )

    if request.method == "POST":

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Tag created.",
            )

            return redirect(
                "dashboard:tags"
            )

    return render(
        request,
        "dashboard/tags.html",
        {
            "tags": items,
            "form": form,
        },
    )


@staff_required
@require_POST
def tag_delete(request, pk):

    get_object_or_404(
        Tag,
        pk=pk,
    ).delete()

    messages.success(
        request,
        "Tag deleted.",
    )

    return redirect(
        "dashboard:tags"
    )


@staff_required
def users(request):

    return render(
        request,
        "dashboard/users.html",
        {
            "users":
                User.objects.all()
                .order_by("-date_joined")
        },
    )


@login_required
def ai_generator(request):

    return render(
        request,
        "dashboard/ai_generator.html",
    )


@staff_required
def seo_settings(request):

    blogs = (
        Blog.objects
        .select_related("category")
        .order_by("-updated_at")
    )

    audits = [
        (
            blog,
            seo_audit(blog),
        )
        for blog in blogs[:50]
    ]

    return render(
        request,
        "dashboard/seo_settings.html",
        {
            "audits": audits,
        },
    )