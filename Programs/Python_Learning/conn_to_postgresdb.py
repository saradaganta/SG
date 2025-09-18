import psycopg2

# Establish the connection to your PostgreSQL database
try:
    connection = psycopg2.connect(
        host="localhost",  # or the address of the PostgreSQL server
        port="5432",  # default port for PostgreSQL
        database="practise",  # name of your database
        user="sg",  # your PostgreSQL username
        password="sg"  # your PostgreSQL password
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a query to fetch data from the emp table
    # cursor.execute("SELECT * FROM emp;")
    # SQL query to join the tables emp and dept
    sql_query = """
    SELECT e.emp_id, e.emp_name, e.dept_id, d.dept_name
    FROM emp e
    INNER JOIN dept d
    ON e.dept_id = d.dept_id;
    """
    # Execute the query
    cursor.execute(sql_query)

    # Get column headers
    headers = [desc[0] for desc in cursor.description]

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the headers
    print(headers)

    # Print the rows
    for row in rows:
        print(row)
    # This will repeate each column name for each value in row.
    #     print(f"EMPLOYEE ID: {row[0]}, EMPLOYEE NAME: {row[1]}, DEPARTMENT ID: {row[2]}, DEPARTMENT NAME: {row[3]}")

except Exception as error:
    print(f"Error: {error}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
