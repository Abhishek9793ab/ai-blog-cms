from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.sitemaps import BlogSitemap
from blog.views import robots_txt


sitemaps = {
    "blogs": BlogSitemap,
}


urlpatterns = [

    # Django Admin
    path(
        "django-admin/",
        admin.site.urls
    ),

    # Public Blog
    path(
        "",
        include("blog.urls")
    ),

    # Authentication
    path(
        "",
        include("accounts.urls")
    ),

    # Custom Dashboard
    path(
        "dashboard/",
        include("dashboard.urls")
    ),

    # SEO Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps
        },
        name="sitemap"
    ),

    # Robots
    path(
        "robots.txt",
        robots_txt,
        name="robots"
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )