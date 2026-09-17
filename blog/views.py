from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .ai_service import AIServiceError, generate_blog_with_gemini
from .forms import BlogForm, CategoryForm, TagForm, CommentForm
from .models import Blog, Category, Tag, Comment, Bookmark
from .seo import seo_audit
from .utils import unique_slug


def home(request):
    featured = (
        Blog.objects
        .filter(status="published", is_featured=True)
        .select_related("author", "category")[:3]
    )

    blogs = (
        Blog.objects
        .filter(status="published")
        .select_related("author", "category")
        .order_by("-published_at", "-created_at")[:9]
    )

    categories = Category.objects.all()[:8]

    return render(
        request,
        "blog/home.html",
        {
            "featured": featured,
            "blogs": blogs,
            "categories": categories,
        },
    )


def blog_list(request):
    qs = (
        Blog.objects
        .filter(status="published")
        .select_related("author", "category")
        .prefetch_related("tags")
    )

    category = request.GET.get("category", "").strip()
    tag = request.GET.get("tag", "").strip()
    q = request.GET.get("q", "").strip()

    if category:
        qs = qs.filter(category__slug=category)

    if tag:
        qs = qs.filter(tags__slug=tag)

    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(excerpt__icontains=q)
            | Q(content__icontains=q)
            | Q(focus_keyword__icontains=q)
        ).distinct()

    categories = Category.objects.all()

    return render(
        request,
        "blog/blog_list.html",
        {
            "blogs": qs,
            "categories": categories,
            "query": q,
            "selected_category": category,
            "selected_tag": tag,
        },
    )


def blog_detail(request, slug):
    blog = get_object_or_404(
        Blog.objects
        .select_related("author", "category")
        .prefetch_related("tags"),
        slug=slug,
        status="published",
    )

    Blog.objects.filter(pk=blog.pk).update(views=blog.views + 1)
    blog.views += 1

    comments = (
        blog.comments
        .filter(status="approved")
        .select_related("user")
    )

    related = (
        Blog.objects
        .filter(status="published")
        .exclude(pk=blog.pk)
        .select_related("author", "category")
    )

    if blog.category_id:
        related = related.filter(category_id=blog.category_id)

    related = related[:3]

    bookmarked = False

    if request.user.is_authenticated:
        bookmarked = Bookmark.objects.filter(
            user=request.user,
            blog=blog,
        ).exists()

    return render(
        request,
        "blog/blog_detail.html",
        {
            "blog": blog,
            "comments": comments,
            "related": related,
            "comment_form": CommentForm(),
            "bookmarked": bookmarked,
            "seo": seo_audit(blog),
        },
    )


@login_required
@require_POST
def add_comment(request, slug):
    blog = get_object_or_404(
        Blog,
        slug=slug,
        status="published",
    )

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.user = request.user
        comment.status = "pending"
        comment.save()

        messages.success(
            request,
            "Comment submitted. It will appear after approval.",
        )

    else:
        messages.error(
            request,
            "Please write a valid comment.",
        )

    return redirect(blog.get_absolute_url())


@login_required
@require_POST
def toggle_bookmark(request, slug):
    blog = get_object_or_404(
        Blog,
        slug=slug,
        status="published",
    )

    bookmark, created = Bookmark.objects.get_or_create(
        user=request.user,
        blog=blog,
    )

    if not created:
        bookmark.delete()
        messages.info(request, "Blog removed from bookmarks.")
    else:
        messages.success(request, "Blog bookmarked.")

    return redirect(blog.get_absolute_url())


@login_required
def create_blog(request):
    ai_data = request.session.get("ai_generated_blog", {})

    initial = {}

    if ai_data and request.method == "GET":
        initial = {
            "title": ai_data.get("title", ""),
            "excerpt": ai_data.get("excerpt", ""),
            "content": ai_data.get("content_html", ""),
            "seo_title": ai_data.get("seo_title", ""),
            "meta_description": ai_data.get("meta_description", ""),
            "focus_keyword": ai_data.get("focus_keyword", ""),
        }

    form = BlogForm(
        request.POST or None,
        request.FILES or None,
        initial=initial,
    )

    if request.method == "POST" and form.is_valid():

        blog = form.save(commit=False)

        blog.author = request.user
        blog.slug = unique_slug(Blog, blog.title)

        if blog.status == "published" and not blog.published_at:
            blog.published_at = timezone.now()

        blog.save()
        form.save_m2m()

        ai_tags = ai_data.get("tags", [])

        if ai_tags and not blog.tags.exists():
            for tag_name in ai_tags:
                tag_name = str(tag_name).strip()[:50]

                if tag_name:
                    tag, _ = Tag.objects.get_or_create(
                        name=tag_name
                    )
                    blog.tags.add(tag)

        request.session.pop("ai_generated_blog", None)

        messages.success(
            request,
            "Blog created successfully.",
        )

        return redirect("dashboard:blogs")

    return render(
        request,
        "blog/create_blog.html",
        {
            "form": form,
            "page_title": "Create Blog",
        },
    )


@login_required
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if not (
        request.user.is_staff
        or blog.author_id == request.user.id
    ):
        raise Http404

    form = BlogForm(
        request.POST or None,
        request.FILES or None,
        instance=blog,
    )

    if request.method == "POST" and form.is_valid():

        obj = form.save(commit=False)

        if (
            obj.status == "published"
            and not obj.published_at
        ):
            obj.published_at = timezone.now()

        obj.save()
        form.save_m2m()

        messages.success(
            request,
            "Blog updated successfully.",
        )

        return redirect("dashboard:blogs")

    return render(
        request,
        "blog/create_blog.html",
        {
            "form": form,
            "page_title": "Edit Blog",
            "blog": blog,
        },
    )


@login_required
@require_POST
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if (
        request.user.is_staff
        or blog.author_id == request.user.id
    ):
        blog.delete()

        messages.success(
            request,
            "Blog deleted successfully.",
        )

    else:
        messages.error(
            request,
            "You do not have permission to delete this blog.",
        )

    return redirect("dashboard:blogs")


def category_detail(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
    )

    blogs = (
        Blog.objects
        .filter(
            status="published",
            category=category,
        )
        .select_related("author", "category")
        .prefetch_related("tags")
    )

    return render(
        request,
        "blog/category.html",
        {
            "category": category,
            "blogs": blogs,
        },
    )


def search_api(request):
    q = request.GET.get("q", "").strip()

    results = []

    if q:
        blogs = (
            Blog.objects
            .filter(status="published")
            .filter(
                Q(title__icontains=q)
                | Q(excerpt__icontains=q)
                | Q(content__icontains=q)
            )
            [:10]
        )

        for blog in blogs:
            results.append(
                {
                    "title": blog.title,
                    "url": blog.get_absolute_url(),
                    "excerpt": blog.excerpt[:140],
                }
            )

    return JsonResponse(
        {
            "results": results,
        }
    )


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "Sitemap: http://127.0.0.1:8000/sitemap.xml\n"
    )

    return HttpResponse(
        content,
        content_type="text/plain",
    )


@login_required
@require_POST
def ai_generate(request):
    topic = request.POST.get(
        "topic",
        "",
    ).strip()

    keyword = request.POST.get(
        "keyword",
        "",
    ).strip()

    tone = request.POST.get(
        "tone",
        "professional",
    ).strip()

    length = request.POST.get(
        "length",
        "medium",
    ).strip()

    if not topic:
        return JsonResponse(
            {
                "ok": False,
                "error": "Topic is required.",
            },
            status=400,
        )

    try:
        result = generate_blog_with_gemini(
            topic,
            keyword,
            tone,
            length,
        )

    except AIServiceError as exc:
        return JsonResponse(
            {
                "ok": False,
                "error": str(exc),
            },
            status=400,
        )

    request.session["ai_generated_blog"] = result
    request.session.modified = True

    return JsonResponse(
        {
            "ok": True,
            "data": result,
        }
    )