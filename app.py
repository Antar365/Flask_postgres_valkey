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




from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql 
from psycopg2.extras import execute_batch
import time
import redis
import json
import random
import string
app = Flask(__name__)

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

# Create the "tasks" table (run this once during setup)
def create_tasks_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task_id VARCHAR(255) UNIQUE NOT NULL,
            task TEXT NOT NULL
        );
    """)
    connection.commit()
    cursor.close()
    connection.close()

create_tasks_table()  # Ensure the table is created when the app starts

@app.route("/")
def main():
    return "Welcome to the Task Manager with PostgreSQL and Redis!"

# Endpoint to add a task
@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task_id = data.get("task_id")
    task = data.get("task")
   
    if not task_id or not task:
        return jsonify({"error": "Task ID and task description are required"}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO tasks (task_id, task) VALUES (%s, %s)
        """, (task_id, task))
        connection.commit()
        cursor.close()
        connection.close()

        # Cache the task in Redis
        redis_client.set(task_id, task)

        return jsonify({"message": f"Task '{task}' added with ID '{task_id}'"}), 201
    except psycopg2.IntegrityError:
        return jsonify({"error": f"Task ID '{task_id}' already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#new
@app.route("/get_all_keys", methods=["GET"])
def get_all_keys():
    keys = redis_client.keys("*")  # Get all keys
    data = {key: redis_client.get(key) for key in keys}  # Get values
    return jsonify({"data": data}), 200


# Endpoint to get a task
@app.route("/get_task/<task_id>", methods=["GET"])
def get_task(task_id):
    
    ##########################3
    
    result = {"id": task_id}

    # Measure time for Valkey
    start_time_valkey = time.time()
    cached_task = redis_client.get(task_id)
    time_taken_valkey = time.time() - start_time_valkey  

    # Measure time for PostgreSQL
    start_time_postgres = time.time()
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT task FROM tasks WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    cursor.close()
    connection.close()
    time_taken_postgres = time.time() - start_time_postgres  

    # Check if the task exists in Valkey
    if cached_task:
        result["task_from_valkey"] = cached_task
        result["time_taken_valkey"] = f"{time_taken_valkey:.6f} seconds"
    else:
        result["task_from_valkey"] = "Not Found"

    # Check if the task exists in PostgreSQL
    if task:
        result["task_from_postgres"] = task[0]
        result["time_taken_postgres"] = f"{time_taken_postgres:.6f} seconds"
    else:
        result["task_from_postgres"] = "Not Found"

    return jsonify(result), 200
    
    ####################################
    
    
    
    
    
    # Check if the task is cached in Redis
    cached_task = redis_client.get(task_id)
    if cached_task:
        return jsonify({"id": task_id, "task": cached_task, "source": "cache"}), 200

    # If not in cache, retrieve from PostgreSQL
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT task FROM tasks WHERE task_id = %s
    """, (task_id,))
    task = cursor.fetchone()
    cursor.close()
    connection.close()
   
    if not task:
        return jsonify({"error": f"No task found with ID '{task_id}'"}), 404

    # Cache the retrieved task in Redis
    redis_client.set(task_id, task[0])

    return jsonify({"id": task_id, "task": task[0], "source": "database"}), 200

# Endpoint to list all tasks
@app.route("/list_tasks", methods=["GET"])
def list_tasks():
    # Check if the tasks list is cached in Redis
    cached_tasks = redis_client.get("all_tasks")
    if cached_tasks:
        return jsonify({"tasks": json.loads(cached_tasks), "source": "cache"}), 200

    # If not cached, retrieve from PostgreSQL
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT task_id, task FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
   
    task_list = [{"id": row[0], "task": row[1]} for row in tasks]

    # Cache the tasks list in Redis
    redis_client.set("all_tasks", json.dumps(task_list))

    return jsonify({"tasks": task_list, "source": "database"}), 200

# Endpoint to delete a task
@app.route("/delete_task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM tasks WHERE task_id = %s
    """, (task_id,))
    result = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
   
    if result == 0:
        return jsonify({"error": f"No task found with ID '{task_id}'"}), 404

    # Remove the task from Redis
    redis_client.delete(task_id)

    # Invalidate the cached tasks list
    redis_client.delete("all_tasks")

    return jsonify({"message": f"Task with ID '{task_id}' deleted"}), 200





# Generate Unique Keys and 7-Digit Integer Values
def generate_unique_data(n):
    unique_keys = set()
    
    while len(unique_keys) < n:
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # 10-char unique key
        unique_keys.add(key)
    
    # Create a list of (key, value) pairs
    data = [(key, random.randint(1000000, 9999999)) for key in unique_keys]  # 7-digit integer value
    return data

# Endpoint to insert 1 Million Records
@app.route("/insert_bulk", methods=["POST"])
def insert_bulk_data():
    n = 1000000  # 1 million entries
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Generate Unique 1 Million Records
        records = generate_unique_data(n)

        # Insert into PostgreSQL
        execute_batch(cursor, "INSERT INTO tasks (task_id, task) VALUES (%s, %s)", records)
        connection.commit()

        # Insert into Valkey (Redis) Using Pipeline
        pipeline = redis_client.pipeline()
        for task_id, task in records:
            pipeline.set(task_id, task)
        pipeline.execute()

        cursor.close()
        connection.close()

        return jsonify({"message": f"Inserted {n} records into PostgreSQL and Valkey!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
