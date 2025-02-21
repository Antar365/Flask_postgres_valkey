/*function checkPassword() {
  let password = document.getElementById("password").value;
  let confirmPassword = document.getElementById("confirm-password").value; // Corrected variable name
  console.log(password, confirmPassword); // Fixed console.log statement
  let message = document.getElementById("message");
  if (password.length !== 0) {
    if (password === confirmPassword) {
      message.textContent = "Password match";
      message.style.color = "#00FF00";
    } else {
      message.textContent = "Password does not match";
      message.style.color = "#FF0000";
    }
  } else {
    alert("All details are compulsory. Please fill all details.");
    message.textContent = "";
  }
}

var uploadField = document.getElementById("myfile");

uploadField.onchange = function() {
  if (this.files[0].size > 102400) {
    alert("File is too big! File size should be 100kb.");
    this.value = "";
  }
};*/


// Handle Employee Form Submission
// Handle Employee Registration Form Submission
document.getElementById("employee-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    const form = event.target;
    const formData = new FormData(form); // Collect form data

    const formDataObj = {};

    // Convert FormData to a plain object
    formData.forEach((value, key) => {
        formDataObj[key] = value;
    });

    try {
        const response = await fetch("/api/employees", {
            method: "POST",
            headers: {
                "Content-Type": "application/json", // Set correct content type
            },
            body: JSON.stringify(formDataObj), // Send the form data as JSON
        });

        if (response.ok) {
            const result = await response.json();
            alert("Employee data saved successfully: " + result.message);
            // Optionally, clear the form after successful submission
            form.reset();
        } else {
            const errorData = await response.json();
            alert("Failed to save employee data: " + errorData.message);
        }
    } catch (error) {
        console.error("Error submitting form:", error);
        alert("An error occurred. Please try again.");
    }
});

// Handle Search Form Submission
// Handle Search Form Submission
document.getElementById("search-form").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    const searchQuery = document.getElementById("search_query").value; // Get the search input value

    try {
        const response = await fetch(`/api/employees/search?search_query=${searchQuery}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json", // Set correct content type
            },
        });

        if (response.ok) {
            const results = await response.json();
            displaySearchResults(results);
        } else {
            alert("No employees found with the given criteria.");
        }
    } catch (error) {
        console.error("Error searching for employees:", error);
        alert("An error occurred while searching. Please try again.");
    }
});

// Function to display search results in the UI
function displaySearchResults(results) {
    const resultsContainer = document.getElementById("search-results");
    resultsContainer.innerHTML = ""; // Clear previous results

    if (results.length === 0) {
        resultsContainer.innerHTML = "<p>No employees found.</p>";
        return;
    }

    // Create a table to display results
    const table = document.createElement("table");
    table.innerHTML = `
    <thead>
        <tr>
            <th>Employee ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Gender</th>
            <th>Age</th>
            <th>Date of Birth</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>State</th>
        </tr>
    </thead>
    <tbody>
        ${results.map(employee => `
            <tr>
                <td>${employee.employee_id}</td>
                <td>${employee.first_name}</td>
                <td>${employee.last_name}</td>
                <td>${employee.gender}</td>
                <td>${employee.age}</td>
                <td>${employee.dob}</td>
                <td>${employee.email}</td>
                <td>${employee.phone}</td>
                <td>${employee.address}</td>
                <td>${employee.state}</td>
            </tr>
        `).join('')}
    </tbody>
`;
resultsContainer.appendChild(table);
}