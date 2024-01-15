import sqlite3

def get_table_schema(database_path, table_name):
    # Connect to the SQLite database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Use PRAGMA table_info to get information about the columns in the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns_info = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Extract column names and types from the result
    column_names = [column[1] for column in columns_info]
    column_types = [column[2] for column in columns_info]

    # Create a dictionary with column names and types
    table_schema = dict(zip(column_names, column_types))

    return table_schema

