# Test Cases for Valkey and PostgreSQL Integration

## TC1: Adding a New Employee Record

### Scenario:
A user sends a request to add a new employee with a unique ID and Name.

### Remarks:
N/A

### Given:
- The backend is set up with a PostgreSQL database and Valkey for key-value storage.
- Initially, no employee records exist.

### When:
- The user sends an API request to add an employee with a unique ID and Name.

### Then:
- The system first checks Valkey to confirm that the employee ID does not exist.
- The employee record is stored in PostgreSQL and the key-value pair is added in Valkey.
- The system returns a success message confirming the addition.

### Test Run Date: 01-02-2025


### Result: Pass


### Testing Outputs:
![Screenshot](assetss/1.png)


---

## TC2: Adding an Employee with an Existing ID

### Scenario:
A user attempts to add an employee record using an ID that already exists in the system.

### Remarks:
N/A

### Given:
- The backend is running with existing employee records in PostgreSQL and Valkey.
- The employee ID is already stored in Valkey.

### When:
- The user sends an API request to add an employee with an ID that is already in use.

### Then:
- The system detects the duplicate ID in Valkey and rejects the request.
- An error message is returned: `"Employee already registered"`
- No changes are made to PostgreSQL or Valkey.

### Test Run Date:01-02-2025


### Result: Pass


### Testing Outputs:
![Screenshot](assetss/2.png)

---

## TC3: Retrieving Employee Data

### Scenario:
A user requests employee details using an existing employee ID.

### Remarks:
N/A

### Given:
- The backend has 1 million employee records stored in both PostgreSQL and Valkey.

### When:
- The user sends an API request to retrieve employee details by providing an existing employee ID.

### Then:
- The system checks Valkey first for quick retrieval.
- If the ID is found in Valkey, the corresponding employee data is returned immediately.
- If not, the system fetches the details from PostgreSQL.


### Test Run Date:01-02-2025


### Result:Pass


### Testing Outputs:
![Screenshot](assetss/3.png)

---

## TC4: Handling Empty or Invalid Input

### Scenario:
A user sends an API request with missing or invalid employee data.

### Remarks:
N/A

### Given:
- The backend expects valid employee IDs and names.

### When:
- The user sends an API request with an empty ID or invalid data (for example, a special character in the name).

### Then:
- The system validates the input and returns an error: `"Invalid Input. Please provide a valid ID and Name."`
- No data is inserted into PostgreSQL or Valkey.

### Test Run Date:01-02-2025


### Result:Pass


### Testing Outputs:

![Screenshot](assetss/4.png)
---

## TC5: Deleting an Employee Record

### Scenario:
A user sends a request to delete an employee record by a valid employee ID.

### Remarks:
N/A

### Given:
- The backend has 1 million employee records stored in PostgreSQL and Valkey.

### When:
- The user sends an API request to delete an employee using a valid employee ID.

### Then:
- The system deletes the employee record from PostgreSQL.
- It also removes the corresponding key-value pair from Valkey.
- If the ID does not exist, the system returns `"Employee not found."`

### Test Run Date:01-02-2025


### Result:Pass


### Testing Outputs:

![Screenshot](assetss/5.png)
---

## TC6: Checking Data Consistency

### Scenario:
A user performs data operations (add, delete) and expects consistent data between PostgreSQL and Valkey.

### Remarks:
N/A

### Given:
- The backend uses PostgreSQL as the persistent data store and Valkey for fast in-memory lookups and the system contains several employee records.

### When:
- The user adds, deletes and get all employee data via the API.

### Then:
- The user get all the data stored in the valkey

### Test Run Date:01-02-2025


### Result:Pass


### Testing Outputs:
![Screenshot](assetss/6.png)

---

## TC7: Performance Comparison: PostgreSQL vs. Valkey Data Retrieval

### Scenario:
A user requests employee details using an existing employee ID, and the response times are compared.

### Remarks:
N/A

### Given:
- The backend has 1 million employee records in both PostgreSQL and Valkey.

### When:
- The user sends an API request to retrieve employee details by providing an existing employee ID.

### Then:
- When retrieving data from PostgreSQL, the response takes longer due to disk I/O, transaction logging, and indexing overhead.
- When retrieving data from Valkey, the response is significantly faster because it is an in-memory store.
- **Result:** The performance difference is evident: Valkey returns data in a fraction of the time compared to PostgreSQL, confirming its use for fast lookups while PostgreSQL remains the source of truth.

### Test Run Date:
01-02-2025

### Result:
Pass

### Testing Outputs:
![Screenshot](assetss/3.png)

## TC8: Performance Comparison: PostgreSQL vs. Valkey Data Retrieval

### Scenario:
A user requests employee details using an existing employee ID, and the response times are compared.

### Remarks:
N/A

### Given:
- The backend is empty

### When:
- The user sends an API request to insert 10000 employees data.

### Then:
- Api request for bulk data inserts 10000 rows with unique employee_id , Email id and phone number. Valkey takes less time than postgres 

### Test Run Date:01-02-2025


### Result:Pass



### Screenshot:

![Screenshot](assetss/8.png)