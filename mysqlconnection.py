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
#
# cursor.execute(f"Select * from hospital")
# column_name = [desc[0] for desc in cursor.description]
# print(column_name)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
#
# # Function to store username and password in the database
# def store_details():
#     username = username_entry.get()
#     password = password_entry.get()
#
#     if username and password:  # Ensure fields are not empty
#         try:
#             # Connect to MySQL database
#             connection = mysql.connector.connect(
#                 host="localhost",  # Replace with your host if needed
#                 user="root",  # Replace with your MySQL username
#                 password="26871234",  # Replace with your MySQL password
#                 database="emp"  # Replace with your database name
#             )
#             cursor = connection.cursor()
#
#             # Insert data into the details table
#             query = "INSERT INTO details (username, passwd) VALUES (%s, %s)"
#             values = (username, password)
#             cursor.execute(query, values)
#             connection.commit()
#
#             # Show success message
#             messagebox.showinfo("Success", "Details stored successfully!")
#
#             # Clear the fields
#             username_entry.delete(0, tk.END)
#             password_entry.delete(0, tk.END)
#
#         except mysql.connector.Error as err:
#             messagebox.showerror("Error", f"Database error: {err}")
#
#         finally:
#             if connection.is_connected():
#                 cursor.close()
#                 connection.close()
#     else:
#         messagebox.showwarning("Warning", "Both fields are required!")
#
# # Create the main window
# root = tk.Tk()
# root.title("Login Form")
#
# # Set the size of the window
# root.geometry("300x200")
#
# # Create the Username label and entry field
# username_label = tk.Label(root, text="Username:")
# username_label.pack(pady=5)
#
# username_entry = tk.Entry(root)
# username_entry.pack(pady=5)
#
# # Create the Password label and entry field
# password_label = tk.Label(root, text="Password:")
# password_label.pack(pady=5)
#
# password_entry = tk.Entry(root, show="*")
# password_entry.pack(pady=5)
#
# # Create the Submit button
# submit_button = tk.Button(root, text="Submit", command=store_details)
# submit_button.pack(pady=10)
#
# # Run the main event loop
# root.mainloop()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to store username and password in the database
def store_details():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        try:
            connection = mysql.connector.connect(
                host="localhost",  # Replace with your host if needed
                user="root",  # Replace with your MySQL username
                password="26871234",  # Replace with your MySQL password
                database="emp"  # Replace with your database name
            )
            cursor = connection.cursor()
            query = "INSERT INTO details (username, passwd) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "Details stored successfully!")
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    else:
        messagebox.showwarning("Warning", "Both fields are required!")

# Function to populate fields when a user clicks on an entry
def populate_fields(username, password):
    username_entry.delete(0, tk.END)
    username_entry.insert(0, username)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to fetch and display all usernames and passwords
def fetch_details():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if needed
            user="root",  # Replace with your MySQL username
            password="26871234",  # Replace with your MySQL password
            database="emp"  # Replace with your database name
        )
        cursor = connection.cursor()
        query = "SELECT username, passwd FROM details"
        cursor.execute(query)
        results = cursor.fetchall()

        # Clear the frame before displaying new data
        for widget in display_frame.winfo_children():
            widget.destroy()

        # Display fetched data inside the frame
        if results:
            tk.Label(display_frame, text="Username", font=("Arial", 10, "bold"), width=15).grid(row=0, column=0, padx=5, pady=5)
            tk.Label(display_frame, text="Password", font=("Arial", 10, "bold"), width=15).grid(row=0, column=1, padx=5, pady=5)

            for i, (username, password) in enumerate(results, start=1):
                username_label = tk.Label(display_frame, text=username, width=15, cursor="hand2")
                password_label = tk.Label(display_frame, text=password, width=15, cursor="hand2")

                # Bind click events to populate the fields
                username_label.bind("<Button-1>", lambda e, u=username, p=password: populate_fields(u, p))
                password_label.bind("<Button-1>", lambda e, u=username, p=password: populate_fields(u, p))

                username_label.grid(row=i, column=0, padx=5, pady=5)
                password_label.grid(row=i, column=1, padx=5, pady=5)
        else:
            tk.Label(display_frame, text="No data found.", fg="red").pack()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Set the size of the window
root.geometry("400x400")

# Create the Username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Create the Password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Create the Submit button
submit_button = tk.Button(root, text="Submit", command=store_details)
submit_button.pack(pady=10)

# Create the Fetch button
fetch_button = tk.Button(root, text="Fetch Details", command=fetch_details)
fetch_button.pack(pady=10)

# Create a frame to display fetched details
display_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=1)
display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Run the main event loop
root.mainloop()





