document.addEventListener("DOMContentLoaded", function () {

    // Sidebar mobile toggle
    const sidebarToggle =
        document.getElementById("sidebar-toggle");

    const sidebar =
        document.querySelector(".dashboard-sidebar");

    if (sidebarToggle && sidebar) {

        sidebarToggle.addEventListener("click", function () {

            sidebar.classList.toggle("show");

        });
    }


    // Automatically hide mobile sidebar
    document.addEventListener("click", function (event) {

        if (!sidebar || !sidebar.classList.contains("show")) {
            return;
        }

        if (
            !sidebar.contains(event.target) &&
            !sidebarToggle?.contains(event.target)
        ) {

            sidebar.classList.remove("show");

        }

    });


    // Delete confirmation
    const deleteForms =
        document.querySelectorAll(".delete-confirm");

    deleteForms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            const confirmed = confirm(
                "Are you sure you want to delete this item?"
            );

            if (!confirmed) {
                event.preventDefault();
            }

        });

    });


    // Auto close alerts
    const alerts =
        document.querySelectorAll(".auto-dismiss");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.opacity = "0";

            setTimeout(function () {
                alert.remove();
            }, 300);

        }, 4000);

    });

});