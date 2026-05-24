const params =
    new URLSearchParams(
        window.location.search
    );

const token =
    params.get("token");

const passwordInput =
    document.getElementById(
        "password"
    );

passwordInput.addEventListener(
    "input",
    checkStrength
);


function checkStrength() {

    const password =
        passwordInput.value;

    const text =
        document.getElementById(
            "strengthText"
        );

    if (
        password.length < 6
    ) {

        text.innerHTML =
            "Weak 🔴";

        return;
    }

    if (
        password.length < 10
    ) {

        text.innerHTML =
            "Medium 🟡";

        return;
    }

    text.innerHTML =
        "Strong 🟢";
}


async function resetPassword() {

    const password =
        document.getElementById(
            "password"
        ).value.trim();

    if (!password) {

        showMessage(
            "Enter password",
            false
        );

        return;
    }

    try {

        const response =
            await fetch(
                `https://secure-auth-system-bp36.onrender.com/api/auth/reset-password/${token}`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        password
                    })
                }
            );

        const data =
            await response.json();

        if (response.ok) {

            showMessage(
                "Password updated successfully. Redirecting to login...",
                true
            );

            setTimeout(() => {

                window.location.href =
                    "index.html";

            }, 3000);

        } else {

            showMessage(
                data.message,
                false
            );
        }

    }
    catch (error) {

        console.error(error);

        showMessage(
            "Unable to connect to server.",
            false
        );
    }
}


function showMessage(
    message,
    success
) {

    const box =
        document.getElementById(
            "message"
        );

    box.innerHTML =
        message;

    box.style.marginTop =
        "15px";

    box.style.fontWeight =
        "bold";

    box.style.color =
        success
        ? "#16a34a"
        : "#dc2626";
}