async function sendOTP() {

    const email =
        document.getElementById(
            "email"
        ).value;

    const response =
        await fetch(
            "http://127.0.0.1:5000/api/otp/send",
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

    alert(data.message);
}


async function verifyOTP() {

    const email =
        document.getElementById(
            "email"
        ).value;

    const otp =
        document.getElementById(
            "otp"
        ).value;

    const response =
        await fetch(
            "http://127.0.0.1:5000/api/otp/verify",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    email,
                    otp
                })
            }
        );

    const data =
        await response.json();

    alert(data.message);

    if (response.ok) {

        window.location.href =
            "dashboard.html";
    }
}