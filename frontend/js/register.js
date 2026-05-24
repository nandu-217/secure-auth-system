async function register() {

    const registerBtn =
        document.getElementById(
            "registerBtn"
        );

    registerBtn.disabled = true;

    try {

        const username =
            document.getElementById(
                "username"
            ).value.trim();

        const email =
            document.getElementById(
                "email"
            ).value.trim();

        const password =
            document.getElementById(
                "password"
            ).value.trim();

        if (
            !username ||
            !email ||
            !password
        ) {

            showError(
                "Please fill all fields"
            );

            return;
        }

        const response =
            await fetch(
                "https://secure-auth-system-bp36.onrender.com/api/auth/register",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        username,
                        email,
                        password
                    })
                }
            );

        const data =
            await response.json();

        console.log(
            "Status:",
            response.status
        );

        console.log(
            "Response:",
            data
        );

        if (response.ok) {

            showRegistrationSuccess(
                username,
                email
            );

            return;
        }

        showError(
            data.message ||
            "Registration failed"
        );

    }
    catch (error) {

        console.error(error);

        showError(
            "Unable to connect to server"
        );
    }
    finally {

        registerBtn.disabled = false;
    }
}


function showRegistrationSuccess(
    username,
    email
) {

    const overlay =
        document.createElement("div");

    overlay.id =
        "successOverlay";

    overlay.innerHTML = `

        <div class="success-box">

            <div class="success-icon">
                📧
            </div>

            <h1>
                Registration Successful
            </h1>

            <p>
                Welcome,
                <strong>${username}</strong>
            </p>

            <p>
                A verification link has been sent to:
            </p>

            <p>
                <strong>${email}</strong>
            </p>

            <p>
                Please check your inbox and
                click the verification link.
            </p>

            <p>
                Your account must be verified
                before you can log in.
            </p>

            <button
                onclick="window.location.href='index.html'"
                style="
                    margin-top:20px;
                    padding:12px 24px;
                    border:none;
                    border-radius:8px;
                    background:#1d2671;
                    color:white;
                    cursor:pointer;
                    font-size:16px;
                ">
                Go To Login
            </button>

        </div>
    `;

    document.body.appendChild(
        overlay
    );
}


function showError(message) {

    const overlay =
        document.createElement("div");

    overlay.id =
        "successOverlay";

    overlay.innerHTML = `

        <div class="success-box">

            <div
            class="success-icon error-icon">
                ❌
            </div>

            <h1>
                Registration Failed
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