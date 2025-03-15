document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("employee-form");
    const searchInput = document.getElementById("search_query");
    const resultsContainer = document.getElementById("search-results");
    const confirmationMessage = document.getElementById("confirmation-message");

    // Handle form submission
    form.addEventListener("submit", async function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        const formData = new FormData(form);
        const formDataObj = Object.fromEntries(formData.entries());

        // Manually get radio button value safely
        const genderInput = document.querySelector('input[name="gender"]:checked');
        formDataObj.gender = genderInput ? genderInput.value : "";

        // Manually get checkbox value
        formDataObj.check = document.getElementById("declaration").checked ? "Declared" : "Not Declared";

        try {
            const response = await fetch("/register_employee", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formDataObj),
            });

            const result = await response.json();

            if (response.ok) {
                confirmationMessage.style.display = "block"; // Show success message
                confirmationMessage.innerHTML = `<p>${result.message}</p>`;

                setTimeout(() => {
                    confirmationMessage.style.display = "none"; // Hide after 3s
                }, 3000);

                form.reset(); // Clear the form
            } else {
                alert(`Error: ${result.error}`);
            }
        } catch (error) {
            console.error("Error submitting form:", error);
            alert("Failed to submit form.");
        }
    });

    // Handle search functionality
    searchInput.addEventListener("input", async function() {
        const searchQuery = searchInput.value.trim();

        if (searchQuery.length === 0) {
            resultsContainer.innerHTML = ""; // Clear results if input is empty
            return;
        }

        try {
            const response = await fetch("/list_employees", {
                method: "GET",
            });

            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status}`);
            }

            const result = await response.json();

            if (!result.employees || !Array.isArray(result.employees)) {
                resultsContainer.innerHTML = `<p class="error">No employee data available.</p>`;
                return;
            }

            displayResults(result.employees, searchQuery);
        } catch (error) {
            console.error("Error fetching employees:", error);
            resultsContainer.innerHTML = `<p class="error">Failed to fetch employees.</p>`;
        }
    });

    // Function to display search results
    function displayResults(employees, query) {
        const filteredEmployees = employees.filter(emp =>
            (emp.first_name && emp.first_name.toLowerCase().includes(query.toLowerCase())) ||
            (emp.last_name && emp.last_name.toLowerCase().includes(query.toLowerCase())) ||
            (emp.employee_id && emp.employee_id.toString().includes(query)) ||
            (emp.email && emp.email.toLowerCase().includes(query.toLowerCase()))
        );

        if (filteredEmployees.length === 0) {
            resultsContainer.innerHTML = `<p class="error">No results found.</p>`;
            return;
        }

        resultsContainer.innerHTML = filteredEmployees
            .map(emp => `<p>${emp.employee_id} - ${emp.first_name}</p>`)

        .join("");
    }
});