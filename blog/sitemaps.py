from django.contrib.sitemaps import Sitemap

from .models import Blog


class BlogSitemap(Sitemap):

    changefreq = "weekly"

    priority = 0.8


    def items(self):

        return Blog.objects.filter(
            status="published"
        )


    def lastmod(self, obj):

        return obj.updated_at


    def location(self, obj):

        return obj.get_absolute_url()