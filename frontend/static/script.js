document.getElementById("trackForm").onsubmit = async function(event) {
    event.preventDefault();  // Stop page reload

    let email = document.getElementById("email").value;
    let crn = document.getElementById("crn").value;

    let response = await fetch("/track", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, crn })
    });

    let result = await response.json();
    alert(result.message);  // Show success or error message
};
