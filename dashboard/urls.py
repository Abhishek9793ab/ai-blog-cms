from django.urls import path
from . import views


app_name = "dashboard"


urlpatterns = [
    # Dashboard Home
    path(
        "",
        views.dashboard_home,
        name="home"
    ),

    # Blog Management
    path(
        "blogs/",
        views.blogs,
        name="blogs"
    ),

    # Comments Management
    path(
        "comments/",
        views.comments,
        name="comments"
    ),

    path(
        "comments/<int:pk>/<str:action>/",
        views.comment_action,
        name="comment_action"
    ),

    # Categories Management
    path(
        "categories/",
        views.categories,
        name="categories"
    ),

    path(
        "categories/<int:pk>/delete/",
        views.category_delete,
        name="category_delete"
    ),

    # Tags Management
    path(
        "tags/",
        views.tags,
        name="tags"
    ),

    path(
        "tags/<int:pk>/delete/",
        views.tag_delete,
        name="tag_delete"
    ),

    # Users Management
    path(
        "users/",
        views.users,
        name="users"
    ),

    # AI Generator
    path(
        "ai-generator/",
        views.ai_generator,
        name="ai_generator"
    ),

    # SEO Audit
    path(
        "seo/",
        views.seo_settings,
        name="seo"
    ),
]