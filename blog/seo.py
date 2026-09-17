def seo_audit(blog):

    title = (
        blog.seo_title
        or blog.title
        or ""
    ).strip()


    meta = (
        blog.meta_description
        or ""
    ).strip()


    keyword = (
        blog.focus_keyword
        or ""
    ).strip().lower()


    content = (
        blog.content
        or ""
    ).lower()


    checks = []


    # SEO Title
    if 20 <= len(title) <= 60:

        title_score = 10

    elif title:

        title_score = 5

    else:

        title_score = 0


    checks.append(
        (
            "SEO Title",
            title_score,
            f"{len(title)} characters"
        )
    )


    # Meta Description
    if 70 <= len(meta) <= 160:

        meta_score = 10

    elif meta:

        meta_score = 5

    else:

        meta_score = 0


    checks.append(
        (
            "Meta Description",
            meta_score,
            f"{len(meta)} characters"
        )
    )


    # Focus Keyword
    if keyword and keyword in content:

        keyword_score = 10

        keyword_message = "Found in content"

    elif keyword:

        keyword_score = 4

        keyword_message = "Not found in content"

    else:

        keyword_score = 0

        keyword_message = "Missing"


    checks.append(
        (
            "Focus Keyword",
            keyword_score,
            keyword_message
        )
    )


    # Excerpt
    checks.append(
        (
            "Excerpt",
            10 if blog.excerpt else 0,
            "Present" if blog.excerpt else "Missing"
        )
    )


    # Featured Image
    checks.append(
        (
            "Featured Image",
            10 if blog.featured_image else 0,
            "Present"
            if blog.featured_image
            else "Missing"
        )
    )


    # Category
    checks.append(
        (
            "Category",
            10 if blog.category_id else 0,
            "Assigned"
            if blog.category_id
            else "Missing"
        )
    )


    # Tags
    tag_count = blog.tags.count()


    checks.append(
        (
            "Tags",
            10 if tag_count > 0 else 0,
            f"{tag_count} tags"
        )
    )


    # Content Length
    content_length = len(
        blog.content or ""
    )


    if content_length >= 1200:

        content_score = 10

    elif content_length >= 600:

        content_score = 5

    else:

        content_score = 0


    checks.append(
        (
            "Content Depth",
            content_score,
            f"{content_length} characters"
        )
    )


    score = sum(
        item[1]
        for item in checks
    )


    return {
        "score": score,
        "checks": checks,
    }