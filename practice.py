# import mysql.connector as db
#
# con = db.connect(
#     user='root',
#     host='localhost',
#     database='emp',
#     passwd='26871234'
# )
#
# cursor = con.cursor()
# # cursor.execute("Select * from product")
#
# # column_names = [desc[0] for desc in cursor.description]
# # print(column_names)
#
# cursor.execute("SHOW TABLES")
# tables = [table[0] for table in cursor.fetchall()]
# print(tables)

import mysql.connector as db

# Establish database connection
con = db.connect(
    user='root',
    host='localhost',
    database='emp',
    passwd='26871234'
)

cursor = con.cursor()

print("1. Create table")
print("2. Insert values inside a table")
print("3. Update the values inside a table")
print("4. Delete/drop the table")
print("5. Display the table")

input1 = int(input("Enter the selected value: "))

if input1 == 1:
    # Create a new table
    table = input("Enter table name: ")
    cursor.execute(f"CREATE TABLE {table} (id INT(3), name VARCHAR(30));")
    print("Table created successfully.")

elif input1 == 2:
    # Insert values into an existing table
    insert_table = input("Enter table name in which you want to insert the values: ").lower()

    # Check if the table exists
    cursor.execute("SHOW TABLES")
    table_names = [table[0] for table in cursor.fetchall()]  # Fetch all tables

    if insert_table in table_names:
        cursor.execute(f"SELECT * FROM {insert_table}")
        column_names = [desc[0] for desc in cursor.description]
        print('Column names:', column_names)

        # Collect input for each column
        values = []
        for column in column_names:
            value = input(f"Enter value for {column}: ")
            # Add quotes for string columns
            if column.lower() == 'name':  # Assuming `name` is the string column
                value = f"'{value}'"
            values.append(value)

        # Join values into a single string for the query
        values_str = ", ".join(values)
        query = f"INSERT INTO {insert_table} ({', '.join(column_names)}) VALUES ({values_str});"

        try:
            cursor.execute(query)
            con.commit()
            print("Values inserted successfully.")
        except db.Error as error:
            print("Failed to insert values:", error)
    else:
        print(f"Table '{insert_table}' does not exist.")

elif input1 == 3:
    print("Update functionality not implemented yet.")

elif input1 == 4:
    print("Delete/drop functionality not implemented yet.")

elif input1 == 5:
    print("Display functionality not implemented yet.")

else:
    print("Invalid option selected.")

# Close the cursor and connection
if cursor.with_rows:  # Ensure all results are cleared before closing
    cursor.fetchall()  # Fetch any remaining results
cursor.close()
con.close()

