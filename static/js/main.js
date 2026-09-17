document.addEventListener("DOMContentLoaded", function () {

    /* =====================================
       MOBILE MENU
    ===================================== */

    const menuButton = document.getElementById("mobileMenuBtn");
    const mobileMenu = document.getElementById("mobileMenu");

    if (menuButton && mobileMenu) {

        menuButton.addEventListener("click", function () {

            mobileMenu.classList.toggle("active");

            const icon = menuButton.querySelector("i");

            if (mobileMenu.classList.contains("active")) {

                icon.classList.remove("bi-list");

                icon.classList.add("bi-x-lg");

            } else {

                icon.classList.remove("bi-x-lg");

                icon.classList.add("bi-list");
            }

        });
    }


    /* =====================================
       AUTO HIDE MESSAGES
    ===================================== */

    setTimeout(function () {

        const messages =
            document.querySelectorAll(".alert-message");

        messages.forEach(function (message) {

            message.style.transition =
                "opacity 0.4s ease, transform 0.4s ease";

            message.style.opacity = "0";

            message.style.transform =
                "translateX(20px)";

            setTimeout(function () {

                message.remove();

            }, 400);

        });

    }, 4000);


    /* =====================================
       IMAGE ERROR HANDLING
    ===================================== */

    document.querySelectorAll("img").forEach(function (image) {

        image.addEventListener("error", function () {

            image.style.display = "none";

            const parent = image.parentElement;

            if (parent) {

                parent.classList.add(
                    "image-placeholder"
                );

                parent.innerHTML =
                    '<i class="bi bi-image"></i>';
            }

        });

    });

});