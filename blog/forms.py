from django import forms

from .models import (
    Blog,
    Category,
    Tag,
    Comment,
)


class BlogForm(forms.ModelForm):

    class Meta:

        model = Blog

        fields = [
            "title",
            "excerpt",
            "content",
            "featured_image",
            "category",
            "tags",
            "status",
            "seo_title",
            "meta_description",
            "focus_keyword",
            "canonical_url",
            "is_featured",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter blog title"
                }
            ),

            "excerpt": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write a short blog summary..."
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 18,
                    "placeholder": "Write your blog content..."
                }
            ),

            "featured_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "size": 6
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "seo_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "SEO title"
                }
            ),

            "meta_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "maxlength": "160",
                    "placeholder": "SEO meta description"
                }
            ),

            "focus_keyword": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Primary focus keyword"
                }
            ),

            "canonical_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com/blog/..."
                }
            ),

            "is_featured": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            ),
        }


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [
            "name",
            "description",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Category name"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Category description"
                }
            ),
        }


class TagForm(forms.ModelForm):

    class Meta:

        model = Tag

        fields = [
            "name"
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tag name"
                }
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = [
            "content"
        ]

        widgets = {

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Write your comment..."
                }
            ),
        }