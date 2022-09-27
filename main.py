import pyrebase
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

firebaseConfig = {
  'apiKey': "AIzaSyAazdViQSpWkIWlvJ1zJ3BG6xPoJAnJwZw",
  'authDomain': "pythontkinter-23b3c.firebaseapp.com",
  'databaseURL': "https://trialauth-7eea1.firebaseio.com",
  'projectId': "pythontkinter-23b3c",
  'storageBucket': "pythontkinter-23b3c.appspot.com",
  'messagingSenderId': "123777162176",
  'appId': "1:123777162176:web:1b649843f1ddfed4790625"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

def logon_task():
  email= username_entry.get()
  password= password_entry.get()
  try:
    login = auth.sign_in_with_email_and_password(email, password)
    result.set_text("Successfully logged in!")
  except:
    result.set_text("Invalid email or password")
  return

def signup_task():
  email= username_entry.get()
  password= password_entry.get()
  try:
      user = auth.create_user_with_email_and_password(email, password)
      result.set_text("Succesfull Sign Up")
  except: 
      result.set_text("Email already exists")
  return

username = customtkinter.CTkLabel(master=app,
                               text = "Username",
                               width=80,
                               height=25,
                               text_color="black",
                               fg_color=("black", "white"),
                               corner_radius=8)
username.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

password = customtkinter.CTkLabel(master=app,
                               text="Password",
                               width=80,
                               height=25,
                               text_color="black",
                               fg_color=("black", "white"),
                               corner_radius=8)
password.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)   

username_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Username",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=10)
username_entry.place(relx=0.65, rely=0.3, anchor=tkinter.CENTER)

password_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Password",
                               width=180,
                               height=25,
                               border_width=2,
                               corner_radius=10)
password_entry.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER) 

login_button = customtkinter.CTkButton(master=app,
                                 width=80,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Login",
                                 command=logon_task)
login_button.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)


signup_button = customtkinter.CTkButton(master=app,
                                 width=80,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="SignUp",
                                 command=signup_task)
signup_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER) 

result = customtkinter.CTkLabel(master=app,
                               text = "",
                               width=120,
                               height=25,
                               text_color="black",
                               fg_color=("black", "white"),
                               corner_radius=8)
result.place(relx=0.62, rely=0.85, anchor=tkinter.CENTER)  

app.mainloop()  