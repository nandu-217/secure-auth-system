window.onload = function () {

    const params =
        new URLSearchParams(
            window.location.search
        );

    const email =
        params.get("email");

    if (email) {

        document.getElementById(
            "email"
        ).value = email;
    }
};


async function login() {

    const email =
        document.getElementById(
            "email"
        ).value.trim();

    const password =
        document.getElementById(
            "password"
        ).value.trim();

    if (!email || !password) {

        showError(
            "Please enter both email and password."
        );

        return;
    }

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/api/auth/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        email,
                        password
                    })
                }
            );

        const data =
            await response.json();

        // EMAIL NOT VERIFIED

        if (response.status === 403) {

            showVerifyRequired();

            return;
        }

        // LOGIN FAILED

        if (!response.ok) {

            showError(
                data.message ||
                "Login failed"
            );

            return;
        }

        // SAVE TOKENS

        localStorage.setItem(
            "access_token",
            data.access_token
        );

        localStorage.setItem(
            "refresh_token",
            data.refresh_token
        );

        localStorage.setItem(
            "username",
            data.username
        );

        showLoginSuccess(
            data.username
        );

    }
    catch (error) {

        console.error(error);

        showError(
            "Unable to connect to server."
        );
    }
}


function showLoginSuccess(username) {

    const overlay =
        document.createElement(
            "div"
        );

    overlay.id =
        "successOverlay";

    overlay.innerHTML = `

        <div class="success-box">

            <div class="success-icon">
                🔐
            </div>

            <h1>
                Authentication Successful
            </h1>

            <p>
                Welcome back,
                <strong>${username}</strong>
            </p>

            <p>
                Your account has been
                authenticated successfully.
            </p>

            <p>
                Redirecting to dashboard...
            </p>

            <div class="success-loader">
            </div>

        </div>

    `;

    document.body.appendChild(
        overlay
    );

    setTimeout(() => {

        window.location.href =
            "dashboard.html";

    }, 3000);
}


function showVerifyRequired() {

    const overlay =
        document.createElement(
            "div"
        );

    overlay.id =
        "successOverlay";

    overlay.innerHTML = `

        <div class="success-box">

            <div class="success-icon">
                📩
            </div>

            <h1>
                Email Verification Required
            </h1>

            <p>
                Your account has not yet
                been verified.
            </p>

            <p>
                Please check your inbox
                and click the verification
                link sent to your email.
            </p>

        </div>

    `;

    document.body.appendChild(
        overlay
    );

    setTimeout(() => {

        overlay.remove();

    }, 4000);
}


function showError(message) {

    const overlay =
        document.createElement(
            "div"
        );

    overlay.id =
        "successOverlay";

    overlay.innerHTML = `

        <div class="success-box">

            <div
                class="success-icon error-icon">

                ❌

            </div>

            <h1>
                Authentication Failed
            </h1>

            <p>
                ${message}
            </p>

        </div>

    `;

    document.body.appendChild(
        overlay
    );

    setTimeout(() => {

        overlay.remove();

    }, 3000);
}