document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("ai-generator-form");
    const button = document.getElementById("generate-ai-btn");
    const resultBox = document.getElementById("ai-result");
    const errorBox = document.getElementById("ai-error");

    if (!form || !button) {
        return;
    }

    form.addEventListener("submit", async function (event) {

        event.preventDefault();

        errorBox.classList.add("d-none");
        resultBox.classList.add("d-none");

        button.disabled = true;

        button.innerHTML =
            '<span class="spinner-border spinner-border-sm me-2"></span>Generating...';

        try {

            const response = await fetch(
                form.action,
                {
                    method: "POST",
                    body: new FormData(form),
                    headers: {
                        "X-Requested-With": "XMLHttpRequest"
                    }
                }
            );

            const data = await response.json();

            if (!response.ok || !data.ok) {
                throw new Error(
                    data.error || "AI generation failed."
                );
            }

            const result = data.data;

            resultBox.classList.remove("d-none");

            document.getElementById(
                "generated-title"
            ).textContent = result.title || "";

            document.getElementById(
                "generated-excerpt"
            ).textContent = result.excerpt || "";

            document.getElementById(
                "generated-keyword"
            ).textContent = result.focus_keyword || "";

            document.getElementById(
                "generated-seo-title"
            ).textContent = result.seo_title || "";

            document.getElementById(
                "generated-meta"
            ).textContent = result.meta_description || "";

            document.getElementById(
                "generated-content"
            ).innerHTML = result.content_html || "";

            const tagsContainer =
                document.getElementById("generated-tags");

            tagsContainer.innerHTML = "";

            if (Array.isArray(result.tags)) {

                result.tags.forEach(function (tag) {

                    const span =
                        document.createElement("span");

                    span.className =
                        "badge text-bg-primary me-1 mb-1";

                    span.textContent = tag;

                    tagsContainer.appendChild(span);

                });

            }

        } catch (error) {

            errorBox.textContent =
                error.message || "Something went wrong.";

            errorBox.classList.remove("d-none");

        } finally {

            button.disabled = false;

            button.innerHTML =
                '<i class="bi bi-stars me-2"></i>Generate Blog';

        }

    });

});