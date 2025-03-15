# from flask import Flask, render_template, request, jsonify
# import psycopg2  # type: ignore
# import redis  # type: ignore
# import json

# app = Flask(__name__, static_folder='public')

# # Initialize PostgreSQL connection
# def get_db_connection():
#     return psycopg2.connect(
#         host="localhost",
#         port="5432",
#         database="postgres",
#         user="postgres",
#         password="root"
#     )

# # Initialize Redis connection
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# # Create the "employees" table
# def create_employees_table():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS employees (
#             employee_id VARCHAR(6) PRIMARY KEY,
#             first_name VARCHAR(30) NOT NULL,
#             last_name VARCHAR(30) NOT NULL,
#             gender VARCHAR(10),
#             age INT,
#             dob DATE,
#             email VARCHAR(100),
#             phone VARCHAR(10),
#             address TEXT,
#             state VARCHAR(50)
#         );
#     """)
#     connection.commit()
#     cursor.close()
#     connection.close()

# create_employees_table()

# @app.route("/")
# def main():
#     return render_template("index.html")  # type: ignore

# # Endpoint to register an employee
# @app.route("/api/employees", methods=["POST"])
# def register_employee():
#     # Log the content type for debugging
#     print(f"Received content type: {request.content_type}")

#     # Check if the content type is application/json
#     if request.content_type != 'application/json':
#         return jsonify({"error": "Unsupported Media Type, use application/json"}), 415

#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "Invalid JSON data"}), 400

#     employee_id = data.get("employee_id")
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     email = data.get("email")
    
#     if not employee_id or not first_name or not last_name or not email:
#         return jsonify({"error": "Employee ID, First Name, Last Name, and Email are required"}), 400

#     # Check Redis (Valkey) for existing employee
#     if redis_client.exists(employee_id):
#         return jsonify({"error": f"Employee with ID '{employee_id}' already exists in cache"}), 400

#     try:
#         connection = get_db_connection()
#         cursor = connection.cursor()
#         cursor.execute("""
#             INSERT INTO employees (employee_id, first_name, last_name, gender, age, dob, email, phone, address, state)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (employee_id, first_name, last_name, data.get("gender"), data.get("age"), data.get("dob"),
#                email, data.get("phone"), data.get("address"), data.get("state")))
#         connection.commit()
#         cursor.close()
#         connection.close()

#         # Store in Redis (Valkey)
#         redis_client.set(employee_id, json.dumps(data))
#         return jsonify({"message": f"Employee '{first_name} {last_name}' registered successfully!"}), 201
#     except psycopg2.IntegrityError:
#         return jsonify({"error": f"Employee with ID '{employee_id}' already exists in database"}), 400
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Endpoint to search for employees
# @app.route("/api/employees/search", methods=["GET"])
# def search_employees():
#     search_query = request.args.get("search_query")
#     if not search_query:
#         return jsonify({"error": "Search query is required"}), 400

#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("""
#         SELECT employee_id, first_name, last_name, gender, age, dob, email, phone, address, state
#         FROM employees
#         WHERE employee_id LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR email LIKE %s
#     """, (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
#     employees = cursor.fetchall()
#     cursor.close()
#     connection.close()

#     if not employees:
#         return jsonify({"error": "No employees found matching the search criteria"}), 404

#     employee_list = [{
#         "employee_id": emp[0],
#         "first_name": emp[1],
#         "last_name": emp[2],
#         "gender": emp[3],
#         "age": emp[4],
#         "dob": emp[5],
#         "email": emp[6],
#         "phone": emp[7],
#         "address": emp[8],
#         "state": emp[9]
#     } for emp in employees]

#     return jsonify(employee_list), 200

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True)




from flask import Flask, request, jsonify, render_template , send_from_directory
import psycopg2
from psycopg2 import sql 
from psycopg2.extras import execute_batch
import time
import redis
import json
import random
import string
app = Flask(__name__ , static_folder="static")

# Initialize PostgreSQL connection
def get_db_connection():
    return psycopg2.connect(
        host="localhost",    # Replace with your PostgreSQL host
        port="5432",         # Default PostgreSQL port
        database="employee", # Replace with your database name
        user="postgres",    # Replace with your database user
        password="root" # Replace with your database password
    )

# Initialize Redis connection
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

def create_employees_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT PRIMARY KEY,  -- Primary Key should be the first column
            first_name VARCHAR(30) NOT NULL, 
            last_name VARCHAR(30) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            dob DATE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(10) UNIQUE NOT NULL,
            address TEXT NOT NULL,
            state VARCHAR(50) NOT NULL  
        );
    """)  # Properly closing the statement

    connection.commit()
    cursor.close()
    connection.close()

create_employees_table()  # Ensure the table is created when the app starts


@app.route("/")
def main():
    return render_template("index.html")


# Endpoint to add a task
@app.route("/register_employee", methods=["POST"])
def register_employee():
    data = request.get_json()
    employee_id = data.get("employee_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    gender = data.get("gender")
    age = data.get("age")
    dob = data.get("dob")
    email = data.get("email")
    phone = data.get("phone")
    address = data.get("address")
    state = data.get("state")

    if not all([employee_id, first_name, last_name, gender, age, dob, email, phone, address, state]):
        return jsonify({"error": "All fields are required"}), 400

    try:
        # 🔹 1️⃣ Check if Employee ID already exists in Valkey
        if redis_client.get(employee_id):
            return jsonify({"error": f"Employee ID '{employee_id}' already exists in Valkey"}), 400

        # Establish PostgreSQL connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # 🔹 2️⃣ If not in Valkey, check PostgreSQL (as a fallback)
        cursor.execute("SELECT 1 FROM employees WHERE employee_id = %s", (employee_id,))
        existing = cursor.fetchone()
        if existing:
            return jsonify({"error": f"Employee ID '{employee_id}' already exists in PostgreSQL"}), 400

        # 🔹 3️⃣ Insert into PostgreSQL
        cursor.execute("""
            INSERT INTO employees (employee_id, first_name, last_name, gender, age, dob, email, phone, address, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (employee_id, first_name, last_name, gender, age, dob, email, phone, address, state))
        connection.commit()

        # 🔹 4️⃣ Store in Valkey only after successful PostgreSQL insertion
        redis_client.set(employee_id, first_name)

        cursor.close()
        connection.close()

        return jsonify({"message": f"Employee '{first_name} {last_name}' registered successfully"}), 201

    except psycopg2.IntegrityError as e:
        connection.rollback()
        return jsonify({"error": f"PostgreSQL Integrity Error: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
#new
@app.route("/get_all_keys", methods=["GET"])
def get_all_keys():
    keys = redis_client.keys("*")  # Get all keys
    data = {key: redis_client.get(key) for key in keys}  # Get values
    return jsonify({"data": data}), 200


# Endpoint to get a task
@app.route("/get_employee/<employee_id>", methods=["GET"])
def get_employee(employee_id):
    result = {"employee_id": employee_id}
    first_name = None
    data_source = None

    # Measure time for Valkey lookup
    try:
        start_time_valkey = time.time()
        cached_name = redis_client.get(employee_id)
        time_taken_valkey = time.time() - start_time_valkey

        if cached_name:
            first_name = cached_name
            data_source = "Valkey"
    except Exception as e:
        result["valkey_error"] = str(e)
        time_taken_valkey = None  # If an error occurs, don't report invalid time

    # Measure time for PostgreSQL lookup
    try:
        start_time_postgres = time.time()
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT first_name FROM employees WHERE employee_id = %s", (employee_id,))
                employee = cursor.fetchone()
        time_taken_postgres = time.time() - start_time_postgres

        if employee:
            first_name = employee[0]
            data_source = "PostgreSQL"

            # Cache in Valkey for future use (with expiry)
            try:
                redis_client.setex(employee_id, 3600, first_name)  # Cache for 1 hour
            except Exception as e:
                result["valkey_cache_error"] = str(e)
    except Exception as e:
        result["postgres_error"] = str(e)
        time_taken_postgres = None  # If an error occurs, don't report invalid time

    if not first_name:
        return jsonify({"error": f"No employee found with ID '{employee_id}'"}), 404

    # Update response with both times
    result.update({
        "first_name": first_name,
        "source": data_source,
        "time_taken_valkey": time_taken_valkey,
        "time_taken_postgres": time_taken_postgres
    })

    return jsonify(result), 200
# Endpoint to list all employees
@app.route("/list_employees", methods=["GET"])
def list_employees():
    # Get all employee IDs (keys)
    employee_keys = redis_client.keys("*")  # Get all keys

    if not employee_keys:
        return jsonify({"employees": [], "source": "valkey"}), 200  # No employees found

    employee_list = []
    for key in employee_keys:
        employee_name = redis_client.get(key)  # Get the first name (value)

        if employee_name:  # Ensure it's not empty
            employee_list.append({
                "employee_id": key,  # Key is the Employee ID
                "first_name": employee_name  # Value is the First Name
            })

    return jsonify({"employees": employee_list, "source": "valkey"}), 200

# Endpoint to delete an employee
@app.route("/delete_employee/<employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Delete from PostgreSQL
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
    result = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    if result == 0:
        return jsonify({"error": f"No employee found with ID '{employee_id}'"}), 404

    # Remove employee from Valkey
    redis_client.delete(employee_id)

    # Invalidate cached employee list
    redis_client.delete("all_employees")

    return jsonify({"message": f"Employee with ID '{employee_id}' deleted"}), 200


# Generate a random email
def generate_email(first_name, last_name):
    domains = ["gmail.com", "yahoo.com", "outlook.com", "company.com"]
    return f"{first_name.lower()}.{last_name.lower()}{random.randint(1000, 9999)}@{random.choice(domains)}"

# Generate a random phone number
def generate_phone_number():
    return str(random.randint(6000000000, 9999999999))  # 10-digit Indian phone number

# Generate unique employee records with uniqueness checks for email, phone, and employee ID
def generate_unique_employees(n, existing_employees=set(), existing_emails=set(), existing_phones=set()):
    records = []
    
    names = ["John", "Alice", "Bob", "Emma", "Michael", "Sophia", "Liam", "Olivia", "Ethan", "Ava"]
    last_names = ["Doe", "Smith", "Brown", "Wilson", "Taylor", "Johnson", "Lee", "Martinez"]
    addresses = ["123 Main St", "456 Elm St", "789 Oak St", "101 Pine St"]
    states = ["California", "Texas", "New York", "Florida", "Illinois"]

    while len(records) < n:
        employee_id = random.randint(100000, 999999)  # Unique 6-digit ID
        email = generate_email("John", "Doe")  # Placeholder names for generation
        phone = generate_phone_number()

        # Ensure uniqueness of employee ID, email, and phone number
        if employee_id in existing_employees or email in existing_emails or phone in existing_phones:
            continue  # Skip this record if any value is already taken

        first_name = random.choice(names)
        last_name = random.choice(last_names)
        address = random.choice(addresses)
        state = random.choice(states)
        gender = random.choice(["Male", "Female"])
        age = random.randint(20, 60)
        dob = f"{random.randint(1960, 2005)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"  # Random DOB

        # Add the new record
        records.append((employee_id, first_name, last_name, gender, age, dob, email, phone, address, state))
        
        # Add to the sets to track uniqueness
        existing_employees.add(employee_id)
        existing_emails.add(email)
        existing_phones.add(phone)

    return records

# Endpoint to insert bulk employees
@app.route("/insert_bulk_employees", methods=["POST"])
def insert_bulk_employees():
    n = 10000  # Number of employees to insert
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Get existing emails and phone numbers from the database
        cursor.execute("SELECT email, phone FROM employees")
        existing_data = cursor.fetchall()
        existing_emails = {email for email, _ in existing_data}
        existing_phones = {phone for _, phone in existing_data}
        existing_employees = set()  # Add logic to track employee_id uniqueness as needed

        # Generate Unique Employee Records (with uniqueness checks)
        records = generate_unique_employees(n, existing_employees, existing_emails, existing_phones)

        # Insert into PostgreSQL
        start_postgres = time.time()
        execute_batch(cursor, """
            INSERT INTO employees (employee_id, first_name, last_name, gender, age, dob, email, phone, address, state)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, records)
        connection.commit()
        postgres_time = time.time() - start_postgres

        # Insert into Valkey (Redis) Using Pipeline
        start_valkey = time.time()
        pipeline = redis_client.pipeline()
        for emp in records:
            employee_id, first_name, last_name, gender, age, dob, email, phone, address, state = emp
            pipeline.hset(f"employee:{employee_id}", mapping={
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "age": age,
                "dob": dob,
                "email": email,
                "phone": phone,
                "address": address,
                "state": state
            })
        pipeline.execute()
        valkey_time = time.time() - start_valkey

        cursor.close()
        connection.close()

        return jsonify({
            "message": f"Inserted {n} employee records into PostgreSQL and Valkey!",
            "postgres_time_seconds": postgres_time,
            "valkey_time_seconds": valkey_time
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000 , debug=True)
