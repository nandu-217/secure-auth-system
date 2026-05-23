// Read token from URL if present
const params = new URLSearchParams(
    window.location.search
);

const urlToken = params.get("token");

// Auto verify if token exists in URL
if (urlToken) {

    document.getElementById(
        "token"
    ).value = urlToken;

    verifyEmail(urlToken);
}


async function verifyEmail(
    tokenFromUrl = null
) {

    const token =
        tokenFromUrl ||
        document.getElementById(
            "token"
        ).value.trim();

    if (!token) {

        showMessage(
            "Please enter verification token",
            false
        );

        return;
    }

    try {

        const response =
            await fetch(
                `http://127.0.0.1:5000/api/auth/verify-email/${token}`
            );

        const contentType =
            response.headers.get(
                "content-type"
            );

        let message =
            "Verification completed successfully";

        if (
            contentType &&
            contentType.includes(
                "application/json"
            )
        ) {

            const data =
                await response.json();

            message =
                data.message;
        }

        if (response.ok) {

            showMessage(
                "✅ Email verified successfully. You can now login.",
                true
            );

        } else {

            showMessage(
                message,
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

    const messageBox =
        document.getElementById(
            "message"
        );

    messageBox.innerText =
        message;

    messageBox.style.color =
        success
            ? "#28a745"
            : "#dc3545";

    messageBox.style.fontWeight =
        "bold";

    messageBox.style.marginTop =
        "15px";
}