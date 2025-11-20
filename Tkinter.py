# Act 9: Tkinter
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# -------- CONNECT TO XAMPP DATABASE --------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # default XAMPP password is empty
    database="login_db"
)

cursor = db.cursor()

# -------- LOGIN WINDOW --------
def login_page():
    def login():
        username = user_entry.get()
        password = pass_entry.get()

        cursor.execute("SELECT * FROM accounts WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful!")
            login_window.destroy()
            personal_info_form()
        else:
            messagebox.showerror("Failed", "Invalid Username or Password")

    def open_register():
        login_window.destroy()
        register_page()

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x230")
    login_window.config(bg="lightblue")

    tk.Label(login_window, text="Login", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(login_window, text="Username", bg="lightblue").pack()
    user_entry = tk.Entry(login_window, width=25)
    user_entry.pack()

    tk.Label(login_window, text="Password", bg="lightblue").pack()
    pass_entry = tk.Entry(login_window, width=25, show="*")
    pass_entry.pack()

    tk.Button(login_window, text="Login", command=login, bg="green", fg="white", width=10).pack(pady=5)
    tk.Button(login_window, text="Register", command=open_register, bg="blue", fg="white", width=10).pack()
    tk.Button(login_window, text="Exit", command=login_window.destroy, bg="red", fg="white", width=10).pack(pady=5)

    login_window.mainloop()


# -------- REGISTER WINDOW --------
def register_page():
    def register():
        username = new_user.get()
        password = new_pass.get()

        if username == "" or password == "":
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        try:
            cursor.execute("INSERT INTO accounts (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Success", "Account Created!")
            register_window.destroy()
            login_page()
        except:
            messagebox.showerror("Error", "Username already exists!")

    def back():
        register_window.destroy()
        login_page()

    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("300x230")
    register_window.config(bg="lightyellow")

    tk.Label(register_window, text="Create Account", font=("Arial", 16, "bold"), bg="lightyellow").pack(pady=10)

    tk.Label(register_window, text="New Username", bg="lightyellow").pack()
    new_user = tk.Entry(register_window, width=25)
    new_user.pack()

    tk.Label(register_window, text="New Password", bg="lightyellow").pack()
    new_pass = tk.Entry(register_window, width=25, show="*")
    new_pass.pack()

    tk.Button(register_window, text="Register", command=register, bg="green", fg="white", width=10).pack(pady=5)
    tk.Button(register_window, text="Back", command=back, bg="blue", fg="white", width=10).pack()
    tk.Button(register_window, text="Exit", command=register_window.destroy, bg="red", fg="white", width=10).pack(pady=5)

    register_window.mainloop()


# -------- PERSONAL INFO FORM --------
def personal_info_form():
    def submit_form():
        name = entry_name.get()
        age = entry_age.get()
        gender = gender_var.get()
        country = country_cb.get()
        comment = text_comment.get("1.0", "end-1c")
        
        hobbies = []
        if hobby_reading.get():
            hobbies.append("Reading")
        if hobby_sports.get():
            hobbies.append("Sports")
        if hobby_music.get():
            hobbies.append("Music")
        
        if name == "" or age == "" or gender == "" or country == "":
            messagebox.showwarning("Incomplete Data", "Please fill out all required fields!")
        else:
            info = (
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Gender: {gender}\n"
                f"Hobbies: {', '.join(hobbies)}\n"
                f"Country: {country}\n"
                f"Comment: {comment}"
            )
            messagebox.showinfo("Form Submitted", info)

    window = tk.Tk()
    window.title("Personal Information Form")
    window.geometry("400x500")
    window.config(bg="lightblue")

    tk.Label(window, text="Personal Information Form", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    frame = tk.Frame(window, bg="lightblue")
    frame.pack(pady=5)

    tk.Label(frame, text="Full Name:", bg="lightblue", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
    entry_name = tk.Entry(frame, width=30)
    entry_name.grid(row=0, column=1, pady=3)

    tk.Label(frame, text="Age:", bg="lightblue", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
    entry_age = tk.Entry(frame, width=30)
    entry_age.grid(row=1, column=1, pady=3)

    tk.Label(frame, text="Gender:", bg="lightblue", font=("Arial", 12)).grid(row=2, column=0, sticky="w")
    gender_var = tk.StringVar()
    tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="lightblue").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="lightblue").grid(row=2, column=1, sticky="e")

    tk.Label(frame, text="Hobbies:", bg="lightblue", font=("Arial", 12)).grid(row=3, column=0, sticky="w")
    hobby_reading = tk.BooleanVar()
    hobby_sports = tk.BooleanVar()
    hobby_music = tk.BooleanVar()
    tk.Checkbutton(frame, text="Reading", variable=hobby_reading, bg="lightblue").grid(row=3, column=1, sticky="w")
    tk.Checkbutton(frame, text="Sports", variable=hobby_sports, bg="lightblue").grid(row=4, column=1, sticky="w")
    tk.Checkbutton(frame, text="Music", variable=hobby_music, bg="lightblue").grid(row=5, column=1, sticky="w")

    tk.Label(frame, text="Country:", bg="lightblue", font=("Arial", 12)).grid(row=6, column=0, sticky="w")
    country_cb = ttk.Combobox(frame, values=["Philippines", "Japan", "USA", "Canada", "Australia"], width=27)
    country_cb.grid(row=6, column=1, pady=5)

    tk.Label(window, text="Comments:", bg="lightblue", font=("Arial", 12)).pack(pady=5)
    text_comment = tk.Text(window, width=35, height=4)
    text_comment.pack()

    tk.Button(window, text="Submit", command=submit_form, bg="green", fg="white", font=("Arial", 12), width=10).pack(pady=10)
    tk.Button(window, text="Exit", command=window.destroy, bg="red", fg="white", font=("Arial", 12), width=10).pack()

    window.mainloop()


# -------- RUN APP --------
if __name__ == "__main__":
    login_page()
