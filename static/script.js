function predict() {
    const area = document.getElementById("area").value;
    const bedrooms = document.getElementById("bedrooms").value;
    const bathrooms = document.getElementById("bathrooms").value;
    const floors = document.getElementById("floors").value || 1;
    const waterfront = document.getElementById("waterfront").value || 0;
    const grade = document.getElementById("grade").value || 5;

    if (!area || !bedrooms || !bathrooms) {
        document.getElementById("result").innerText = "⚠ Fill required fields";
        return;
    }

    document.getElementById("loader").style.display = "block";
    document.getElementById("result").innerText = "";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            area,
            bedrooms,
            bathrooms,
            floors,
            waterfront,
            grade
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loader").style.display = "none";
        document.getElementById("result").innerText =
            "💰 ₹ " + data.price + " Lakhs";
    })
    .catch(() => {
        document.getElementById("loader").style.display = "none";
        document.getElementById("result").innerText = "❌ Error";
    });
}