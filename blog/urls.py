from django.urls import path

from . import views


app_name = "blog"


urlpatterns = [

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "blogs/",
        views.blog_list,
        name="blog_list",
    ),

    path(
        "blog/<slug:slug>/",
        views.blog_detail,
        name="blog_detail",
    ),

    path(
        "blog/<slug:slug>/comment/",
        views.add_comment,
        name="add_comment",
    ),

    path(
        "blog/<slug:slug>/bookmark/",
        views.toggle_bookmark,
        name="toggle_bookmark",
    ),

    path(
        "category/<slug:slug>/",
        views.category_detail,
        name="category",
    ),

    path(
        "search-api/",
        views.search_api,
        name="search_api",
    ),

    path(
        "create/",
        views.create_blog,
        name="create_blog",
    ),

    path(
        "edit/<int:pk>/",
        views.edit_blog,
        name="edit_blog",
    ),

    path(
        "delete/<int:pk>/",
        views.delete_blog,
        name="delete_blog",
    ),

    path(
        "ai-generate/",
        views.ai_generate,
        name="ai_generate",
    ),
]