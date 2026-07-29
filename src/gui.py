import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import pickle
from PIL import Image, ImageTk
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import winsound   # ✅ ADDED

# ==========================================================
# MODEL SETUP
# ==========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "alzheimer_model.pkl")
USERS_FILE = os.path.join(BASE_DIR, "users.txt")

FAAH_SOUND = os.path.join(BASE_DIR, "faah.wav")       # ✅ ADDED
ALRIGHT_SOUND = os.path.join(BASE_DIR, "alright.wav") # ✅ ADDED

if not os.path.exists(MODEL_PATH):
    X = np.array([
        [65, 30, 40, 35],
        [70, 20, 25, 30],
        [55, 80, 85, 75],
        [60, 75, 70, 80],
        [75, 15, 20, 18],
        [50, 90, 85, 88]
    ])
    y = np.array([1, 1, 0, 0, 1, 0])
    temp_model = RandomForestClassifier()
    temp_model.fit(X, y)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(temp_model, f)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ==========================================================
# LOGIN WINDOW
# ==========================================================

root = tk.Tk()
root.title("Alzheimer System Login")
root.geometry("500x480")
root.config(bg="#0D47A1")
root.resizable(True, True)

tk.Label(root, text="ALZHEIMER DETECTION SYSTEM",
         font=("Segoe UI", 18, "bold"),
         bg="#0D47A1", fg="white").pack(pady=25)

main_frame = tk.Frame(root, bg="white", bd=3, relief="ridge")
main_frame.pack(padx=30, pady=20, fill="both", expand=True)

btn_frame = tk.Frame(main_frame, bg="white")
btn_frame.pack(pady=10)

def show_register():
    login_frame.pack_forget()
    reset_frame.pack_forget()
    register_frame.pack(fill="both", expand=True)

def show_login():
    register_frame.pack_forget()
    reset_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def show_reset():
    login_frame.pack_forget()
    register_frame.pack_forget()
    reset_frame.pack(fill="both", expand=True)

tk.Button(btn_frame, text="Register", width=10,
          bg="green", fg="white",
          command=show_register).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Login", width=10,
          bg="blue", fg="white",
          command=show_login).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Reset", width=10,
          bg="orange", fg="white",
          command=show_reset).grid(row=0, column=2, padx=5)

# ==========================================================
# REGISTER
# ==========================================================

register_frame = tk.Frame(main_frame, bg="white")

tk.Label(register_frame, text="Username", bg="white").pack(pady=5)
reg_user = tk.Entry(register_frame, width=25)
reg_user.pack(pady=5)

tk.Label(register_frame, text="Password", bg="white").pack(pady=5)
reg_pass = tk.Entry(register_frame, show="*", width=25)
reg_pass.pack(pady=5)

def register():
    if reg_user.get() == "" or reg_pass.get() == "":
        messagebox.showerror("Error", "Fill all fields")
        return
    with open(USERS_FILE, "a") as f:
        f.write(reg_user.get() + "," + reg_pass.get() + "\n")
    messagebox.showinfo("Success", "Registered Successfully")

tk.Button(register_frame, text="Register",
          bg="green", fg="white",
          width=15,
          command=register).pack(pady=10)

register_frame.pack(fill="both", expand=True)

# ==========================================================
# LOGIN
# ==========================================================

login_frame = tk.Frame(main_frame, bg="white")

tk.Label(login_frame, text="Username", bg="white").pack(pady=5)
log_user = tk.Entry(login_frame, width=25)
log_user.pack(pady=5)

tk.Label(login_frame, text="Password", bg="white").pack(pady=5)
log_pass = tk.Entry(login_frame, show="*", width=25)
log_pass.pack(pady=5)

# ==========================================================
# RESET
# ==========================================================

reset_frame = tk.Frame(main_frame, bg="white")

tk.Label(reset_frame, text="Username", bg="white").pack(pady=5)
reset_user = tk.Entry(reset_frame, width=25)
reset_user.pack(pady=5)

tk.Label(reset_frame, text="New Password", bg="white").pack(pady=5)
reset_pass1 = tk.Entry(reset_frame, show="*", width=25)
reset_pass1.pack(pady=5)

tk.Label(reset_frame, text="Confirm Password", bg="white").pack(pady=5)
reset_pass2 = tk.Entry(reset_frame, show="*", width=25)
reset_pass2.pack(pady=5)

def reset_password():
    if reset_pass1.get() != reset_pass2.get():
        messagebox.showerror("Error", "Passwords do not match")
        return
    if not os.path.exists(USERS_FILE):
        return
    lines = open(USERS_FILE).readlines()
    with open(USERS_FILE, "w") as f:
        for line in lines:
            user, pwd = line.strip().split(",")
            if user == reset_user.get():
                f.write(user + "," + reset_pass1.get() + "\n")
            else:
                f.write(line)
    messagebox.showinfo("Success", "Password Reset Successful")

tk.Button(reset_frame, text="Reset Password",
          bg="orange", fg="white",
          width=18,
          command=reset_password).pack(pady=10)

# ==========================================================
# MAIN SYSTEM WINDOW
# ==========================================================

def open_main_system():

    root.withdraw()

    top = tk.Toplevel()
    top.title("Alzheimer Detection System")
    top.geometry("1100x600")
    top.config(bg="#E3F2FD")
    top.resizable(True, True)

    def on_close():
        top.destroy()
        root.deiconify()

    top.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(top, text="Early Alzheimer Disease Detection System",
             font=("Segoe UI", 18, "bold"),
             bg="#E3F2FD").pack(pady=15)

    container = tk.Frame(top, bg="#E3F2FD")
    container.pack(fill="both", expand=True, padx=20, pady=10)

    left = tk.Frame(container, bg="white", bd=2, relief="ridge")
    left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    center = tk.Frame(container, bg="white", bd=2, relief="ridge")
    center.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    right = tk.Frame(container, bg="white", bd=2, relief="ridge")
    right.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    tk.Label(left, text="Patient Details",
             font=("Segoe UI", 14, "bold"),
             bg="white").pack(pady=15)

    tk.Label(left, text="Patient Name", bg="white").pack()
    name_entry = tk.Entry(left, width=22)
    name_entry.pack(pady=8)

    tk.Label(left, text="Age", bg="white").pack()
    age_entry = tk.Entry(left, width=22)
    age_entry.pack(pady=8)

    tk.Label(center, text="MRI Scan",
             font=("Segoe UI", 14, "bold"),
             bg="white").pack(pady=15)

    image_label = tk.Label(center, bg="white")
    image_label.pack(pady=20)

    tk.Label(right, text="Report",
             font=("Segoe UI", 14, "bold"),
             bg="white").pack(pady=15)

    report_text = tk.Text(right)
    report_text.pack(fill="both", expand=True, padx=10, pady=10)

    mri_holder = {"path": ""}

    def extract_features(path):
        img = Image.open(path).convert("L").resize((200, 200))
        pixels = list(img.getdata())
        avg = sum(pixels) / len(pixels)
        return max(0,100-(avg/2)), max(0,100-(avg/3)), max(0,100-(avg/4))

    def upload_mri():
        file = filedialog.askopenfilename(filetypes=[("Image", "*.jpg *.png")])
        if file:
            mri_holder["path"] = file
            img = Image.open(file).resize((220, 220))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img

    def predict():
        if mri_holder["path"] == "":
            messagebox.showerror("Error", "Upload MRI First")
            return
        try:
            age = float(age_entry.get())
        except:
            messagebox.showerror("Error", "Enter valid Age")
            return
        memory, thinking, decision = extract_features(mri_holder["path"])
        pred = model.predict([[age, memory, thinking, decision]])[0]
        result = "Alzheimer Detected" if pred == 1 else "Normal"
        risk = "HIGH" if pred == 1 else "LOW"

        # ✅ SOUND ADDED HERE
        if pred == 1:
            winsound.PlaySound(FAAH_SOUND, winsound.SND_FILENAME)
        else:
            winsound.PlaySound(ALRIGHT_SOUND, winsound.SND_FILENAME)

        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END,
                           f"Patient Name : {name_entry.get()}\n"
                           f"Age : {age}\n\n"
                           f"Memory : {memory:.2f}\n"
                           f"Thinking : {thinking:.2f}\n"
                           f"Decision : {decision:.2f}\n\n"
                           f"Risk : {risk}\n"
                           f"Prediction : {result}")

    def analyze_dataset():
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file:
            return
        df = pd.read_csv(file)
        total = len(df)
        under_60 = len(df[df["Age"] < 60])
        above_60 = len(df[df["Age"] >= 60])
        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END,
                           f"DATASET ANALYSIS\n\n"
                           f"Total Patients : {total}\n"
                           f"Age < 60       : {under_60}\n"
                           f"Age >= 60      : {above_60}")

    button_frame = tk.Frame(top, bg="#E3F2FD")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Upload MRI", width=15,
              bg="purple", fg="white",
              command=upload_mri).grid(row=0, column=0, padx=10)

    tk.Button(button_frame, text="Predict", width=15,
              bg="green", fg="white",
              command=predict).grid(row=0, column=1, padx=10)

    tk.Button(button_frame, text="Dataset", width=15,
              bg="orange", fg="white",
              command=analyze_dataset).grid(row=0, column=2, padx=10)

    tk.Button(button_frame, text="Exit", width=15,
              bg="red", fg="white",
              command=on_close).grid(row=0, column=3, padx=10)

def login():
    if not os.path.exists(USERS_FILE):
        messagebox.showerror("Error", "No users registered")
        return
    lines = open(USERS_FILE).readlines()
    for line in lines:
        user, pwd = line.strip().split(",")
        if user == log_user.get() and pwd == log_pass.get():
            open_main_system()
            return
    messagebox.showerror("Error", "Invalid Login")

tk.Button(login_frame, text="Login",
          bg="blue", fg="white",
          width=15,
          command=login).pack(pady=10)

root.mainloop()