from django.utils.text import slugify


def unique_slug(
    model,
    value,
    instance=None
):

    base = slugify(value)

    if not base:

        base = "blog"


    slug = base

    counter = 2


    queryset = model.objects.all()


    if instance and instance.pk:

        queryset = queryset.exclude(
            pk=instance.pk
        )


    while queryset.filter(
        slug=slug
    ).exists():

        slug = f"{base}-{counter}"

        counter += 1


    return slug