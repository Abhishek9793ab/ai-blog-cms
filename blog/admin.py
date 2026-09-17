from django.contrib import admin

from .models import (
    Blog,
    Category,
    Tag,
    Comment,
    Bookmark,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "status",
        "is_featured",
        "views",
        "created_at",
    )

    list_filter = (
        "status",
        "is_featured",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "seo_title",
        "focus_keyword",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = (
        "tags",
    )

    readonly_fields = (
        "views",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Blog Content",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "content",
                    "featured_image",
                )
            },
        ),
        (
            "Organization",
            {
                "fields": (
                    "author",
                    "category",
                    "tags",
                    "status",
                    "is_featured",
                )
            },
        ),
        (
            "SEO Settings",
            {
                "fields": (
                    "seo_title",
                    "meta_description",
                    "focus_keyword",
                    "canonical_url",
                )
            },
        ),
        (
            "Statistics",
            {
                "fields": (
                    "views",
                    "created_at",
                    "updated_at",
                    "published_at",
                )
            },
        ),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "blog",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "content",
        "user__username",
        "blog__title",
    )

    actions = (
        "approve_comments",
        "reject_comments",
    )

    @admin.action(description="Approve selected comments")
    def approve_comments(self, request, queryset):
        queryset.update(status="approved")

    @admin.action(description="Reject selected comments")
    def reject_comments(self, request, queryset):
        queryset.update(status="rejected")


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "blog",
        "created_at",
    )

    search_fields = (
        "user__username",
        "blog__title",
    )

    list_filter = (
        "created_at",
    )