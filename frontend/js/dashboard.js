const token = localStorage.getItem("token")

if (!token) {

    window.location.href = "index.html"
}

async function loadDashboard() {

    const response = await fetch(
        "http://127.0.0.1:5000/api/auth/dashboard",
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    )

    const data = await response.json()

    if (response.ok) {

        document.getElementById(
            "username"
        ).innerText = data.username

        document.getElementById(
            "email"
        ).innerText = data.email

    } else {

        alert("Unauthorized")

        window.location.href = "index.html"
    }
}

function logout() {

    localStorage.removeItem("token")

    window.location.href = "index.html"
}

loadDashboard()