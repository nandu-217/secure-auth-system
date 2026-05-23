async function sendResetLink() {

    const email =
        document.getElementById(
            "email"
        ).value.trim();

    if (!email) {

        showMessage(
            "Please enter email",
            false
        );

        return;
    }

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/api/auth/forgot-password",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        email
                    })
                }
            );

        const data =
            await response.json();

        if (response.ok) {

            showMessage(
                "Password reset link sent successfully. Check your email.",
                true
            );

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