from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Frame
from tkinter import *  # type: ignore
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmb
import os
import json
import random
import string
from PIL import Image, ImageTk
import Project
from Project import hollywoodMovies, bollywoodMovies

# Set the OUTPUT_PATH to the parent directory of the current script
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r" ")  # Set the ASSETS_PATH to the tS folder

# Define a function to create a Path object relative to ASSETS_PATH


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Global variables
movieName = None
seats = None
theatreName = None
time = None

user = None
tempString = None

# Constants for seat states
BOOKED = "booked"
AVAILABLE = "available"
SELECTED = "selected"

# Change color codes for seat states
AVAILABLE_COLOR = "#FFF5E0"
BOOKED_COLOR = "#C70039"
SELECTED_COLOR = "black"


def login():
    window = Tk()  # Create a window
    window.minsize(400, 500)  # Set the minimum size of the window
    window.title("Login/SignUp Page")  # Set the title of the window
    window.eval('tk::PlaceWindow . center')  # Center the window on the screen

    def close_window_homepage():  # Define a function to close the window and open the homepage
        window.destroy()
        homepage()
        window.protocol("WM_DELETE_WINDOW", close_window_homepage)

    # Define a function to delete the text in the entry box
    def delete_entry_text(text):
        text.delete('0', END)
        text.configure(fg="#000000")

    def user_data(x):  # Define a function to store the user data in a json file
        filename = r'D:\SRAJAN\Python\DSA Sem-3 Cinemate Project\userdata.json'
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump(x, f)
        # 'with open' closes the file as the 'with open' finishes.
        with open(filename, "r+") as f:
            data = json.load(f)
            data.update(x)
            f.seek(0)
            json.dump(data, f)

    filename = r'D:\SRAJAN\Python\DSA Sem-3 Cinemate Project\userdata.json'

    def login_check():
        global user
        user = username.get()  # Get the username entered by the user
        pwd = password.get()  # Get the password entered by the user
        with open(filename, 'r') as f:
            data = json.load(f)
        flag = False
        for usern, passw in data.items():  # Check if the username and password are valid
            if ((user.isspace() == True) or (user == "") or (user == "Username")):
                flag = True
                tkmb.showwarning(
                    title="INVALID", message="Please fill in the username")  # Show a warning if the username is invalid
                break
            elif ((pwd.isspace() == True) or (pwd == "") or (pwd == "Password")):
                flag = True
                tkmb.showwarning(
                    title="INVALID", message="Please fill in the password")  # Show a warning if the password is invalid
                break
            if (user == usern):  # Check if the username is valid
                flag = True
                if (pwd == passw):  # Check if the password is valid
                    tkmb.showinfo(title="Login Successfull",
                                  message=f"Welcome {username.get().upper()} to CINEMATE")
                    close_window_homepage()
                else:
                    tkmb.showwarning(title="Incorrect Password",
                                     message="Please Re-enter your password")
        if (flag == False):  # Check if the username is valid
            tkmb.showwarning(title="Invalid Details",
                             message="Invalid Username or Password , PLS Re-try")

    def acc_create():
        global user
        user = username.get()
        pwd = password.get()
        with open(filename, 'r+') as f:
            data = json.load(f)
        flag = False
        for usern, passw in data.items():  # Check if the username and password are valid
            # Check if the username is valid
            if ((user.isspace() == True) or (user == "") or (user == "Username")):
                flag = True
                tkmb.showwarning(
                    title="INVALID", message="Please fill in the username")
                break
            # Check if the password is valid
            elif ((pwd.isspace() == True) or (pwd == "") or (pwd == "Password")):
                flag = True
                tkmb.showwarning(
                    title="INVALID", message="Please fill in the password")
                break
            if (user == usern):
                if (pwd == passw):
                    tkmb.showwarning(title="EXISTING",
                                     message="This Account already exists Please Login")
                    flag = True
                    break
                else:
                    tkmb.showwarning(
                        title="Username Taken", message="This username is taken please enter a new one")
                    flag = True
                    break
        if (flag == False):
            data[user] = pwd  # Add the username and password to the json file
            # Call the user_data function to store the data in the json file
            user_data(data)
            tkmb.showinfo(title="Account Created",
                          message="Account created Successfully")
            window.after(100, lambda: close_window_homepage)

    canvas = Canvas(master=window,
                    width=400,
                    height=500,
                    highlightthickness=0,
                    bg="#0B1E32",
                    bd=0,
                    relief="flat")
    canvas.place(x=0, y=0)

    # Cinemate Image
    img1 = Image.open(
        relative_to_assets("cinemate ss.png"))
    resized_img1 = img1.resize((293, 53))
    cinemate_img = ImageTk.PhotoImage(resized_img1)
    canvas.create_image(203.5, 94, image=cinemate_img)

    # Block image
    img2 = Image.open(
        relative_to_assets("block ss.png"))
    resized_img2 = img2.resize((284, 288))
    block_img = ImageTk.PhotoImage(resized_img2)
    canvas.create_image(203, 288, image=block_img)

    # username img
    img3 = Image.open(
        relative_to_assets("username ss.png"))
    resized_img3 = img3.resize((218, 27))
    username_img = ImageTk.PhotoImage(resized_img3)
    canvas.create_image(203, 209, image=username_img)

    # password img
    img4 = Image.open(
        relative_to_assets("password ss.png"))
    resized_img4 = img4.resize((218, 27))
    password_img = ImageTk.PhotoImage(resized_img4)
    canvas.create_image(203, 249, image=password_img)

    # # login img
    img5 = Image.open(
        relative_to_assets("login ss .png"))
    resized_img5 = img5.resize((169, 30))
    login_img = ImageTk.PhotoImage(resized_img5)

    # signup image
    img6 = Image.open(
        relative_to_assets("signup ss.png"))
    resized_img6 = img6.resize((169, 30))
    signup_img = ImageTk.PhotoImage(resized_img6)

    # username entry
    username = Entry(master=canvas,
                     font=("montserrat alternates", 11),
                     fg="#BFBFBF",
                     bg="#FFFFFF",
                     highlightthickness=0,
                     bd=0,
                     width=20)
    username.place(x=100, y=198)
    username.insert(0, "Username")
    username.bind(
        "<FocusIn>", lambda args: delete_entry_text(username))

    # password entry
    password = Entry(master=canvas,
                     font=("montserrat alternates", 11),
                     fg="#BFBFBF",
                     bg="#FFFFFF",
                     highlightthickness=0,
                     bd=0,
                     width=20)
    password.place(x=100, y=238)
    password.insert(0, "Password")
    password.bind(
        "<FocusIn>", lambda args: delete_entry_text(password))
    password.bind(
        "<Return>", lambda args: login_check())

    # login Button
    login_button = Button(master=canvas,
                          bg="#CE2E4E",
                          image=login_img,
                          highlightthickness=0,
                          bd=0,
                          command=login_check)
    login_button.place(x=120, y=320)

    # signup Button
    signup_button = Button(master=canvas,
                           image=signup_img,
                           bg="#0B1E32",
                           highlightthickness=0,
                           bd=0,
                           command=acc_create)
    signup_button.place(x=120, y=360)

    window.resizable(False, False)
    window.mainloop()


def searchSug():
    window = Tk()  # Create a window
    window.title("Cinemate")
    window.minsize(960, 540)
    window.configure(bg="#E5E5E5")
    radioVar = IntVar()  # Create a variable to store the value of the radio button

    # Define a function to close the window and go back to the theatreSelection
    def close_window_theatreSelection():
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_theatreSelection)

    # Define a function to close the window and go back to the homepage
    def close_window_homepage():
        window.destroy()
        homepage()
        window.protocol("WM_DELETE_WINDOW", close_window_homepage)

    # Define a function to close the window and go back to the bookinghistory
    def close_window_bookinghistory():
        window.destroy()
        bookinghistory()
        window.protocol("WM_DELETE_WINDOW", close_window_bookinghistory)

    # Define a function to display Hollywood movies
    def displayHollywood():
        update(hollywoodMovies)

    # Define a function to display Bollywood movies
    def displayBollywood():
        update(bollywoodMovies)

    # Define a function to fill the search input field with a selected item from the list
    def fill(event):
        search.delete(0, END)
        search.insert(0, list1.get(ACTIVE))

    # Define a function to update the list based on the search input
    def update(data):
        list1.delete(0, END)
        for item in data:
            list1.insert(END, item)

    # Define a function to refresh the list based on the search input
    def refresh(event):
        if (radioVar.get() == 1):
            value = search.get()
            if value == "":
                data = hollywoodMovies
            else:
                data = []
                for item in hollywoodMovies:
                    if value.lower() in item.lower():
                        data.append(item)
            update(data)
        else:
            value = search.get()
            if value == "":
                data = bollywoodMovies
            else:
                data = []
                for item in bollywoodMovies:
                    if value.lower() in item.lower():
                        data.append(item)
            update(data)

    # Define a function to handle the selection of a movie
    def name(event):
        global movieName
        movieName = search.get()
        if (radioVar.get() == 1):
            for movie, value in hollywoodMovies.items():
                if (movieName == movie):
                    if (value == None):
                        tkmb.showwarning(title="Not Available",
                                         message=f"No Available Theatres for : {movieName}")
                        search.delete('0', 'end')
                    else:
                        tkmb.showinfo(title="Successfully Selected",
                                      message=f"Movie Selected : {movieName}")
                        close_window_theatreSelection()
        elif (radioVar.get() == 2):
            for movie, value in bollywoodMovies.items():
                if (movieName == movie):
                    if (value == None):
                        tkmb.showwarning(title="Not Available",
                                         message=f"No Available Theatres for : {movieName}")
                        search.delete('0', 'end')
                    else:
                        tkmb.showinfo(title="Successfully Selected",
                                      message=f"Movie Selected : {movieName}")
                        close_window_theatreSelection()

    # Create a Canvas for the search page
    canvas = Canvas(
        window,
        bg="#E5E5E5",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="flat"
    )
    list1 = Listbox(
        canvas,
        bg="white",
        font=("Helevetica", 15),
        width=50,
        height=15)
    list1.place(x=240, y=120)

    canvas.create_rectangle(
        0.0,
        0.0,
        960.0,
        60.0,
        fill="#0B1E32",
        outline="")

    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    canvas.create_image(
        525.0,
        30.5,
        image=entry_image_1
    )
    search = Entry(
        canvas,
        bd=0,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0,
        font=("Mohave", 11)
    )
    search.place(
        x=260.0,
        y=20.0,
        width=540.0,
        height=24.0
    )

    # Create a button for signing in or accessing booking history
    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        highlightthickness=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        command=lambda: close_window_bookinghistory(),
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    # Create a back button
    backImg = PhotoImage(
        file=relative_to_assets("back.png"))
    backButton = Button(
        image=backImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_homepage(),
        relief="flat"
    )
    backButton.place(
        x=919.0,
        y=22.0,
        width=16.0,
        height=20.0
    )

    canvas.create_rectangle(
        0.0,
        60.0,
        250.0,
        90.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    canvas.create_text(
        40.0,
        49.0,
        anchor="nw",
        text="Movie Search",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )

    # Create radio buttons for Hollywood and Bollywood movies
    hollywoodButton = Radiobutton(canvas,
                                  text="Hollywood",
                                  font=("Bungee", 12),
                                  fg="#000000",
                                  bg="#E5E5E5",
                                  variable=radioVar,
                                  value=1,
                                  command=displayHollywood)
    hollywoodButton.place(x=360, y=60)

    bollywoodButton = Radiobutton(canvas,
                                  text="Bollywood",
                                  font=("Bungee", 12),
                                  fg="#000000",
                                  bg="#E5E5E5",
                                  variable=radioVar,
                                  value=2,
                                  command=displayBollywood)
    bollywoodButton.place(x=560, y=60)

    canvas.place(x=0, y=0)

    list1.bind("<<ListboxSelect>>", fill)
    search.bind("<KeyRelease>", refresh)
    search.bind("<Return>", name)

    window.mainloop()


def homepage():
    # Define functions to close the window and set the selected movie
    def close_window_godfather():
        global movieName
        movieName = "The Godfather"
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_godfather)

    def close_window_pk():
        global movieName
        movieName = "PK"
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_godfather)

    def close_window_kgf():
        global movieName
        movieName = "K.G.F: Chapter 1"
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_godfather)

    def close_window_mm():
        global movieName
        movieName = "Mission Mangal"
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_godfather)

    def close_window_searchSug():
        window.destroy()
        searchSug()
        window.protocol("WM_DELETE_WINDOW", close_window_searchSug)

    def close_window_bookinghistory():
        window.destroy()
        bookinghistory()
        window.protocol("WM_DELETE_WINDOW", close_window_bookinghistory)

    # Define a function to create a rounded rectangle
    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    window = Tk()
    window.title("Cinemate")
    window.geometry("960x540")
    window.configure(bg="#E5E5E5")

    canvas = Canvas(
        window,
        bg="#E5E5E5",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    # Create a blue rectangle for the title
    canvas.create_rectangle(
        0.0,
        0.0,
        960.0,
        60.0,
        fill="#0B1E32",
        outline="")

    # Display the "CINEMATE" title text
    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    # Load and display images
    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)

    # Create a gray rectangle for the movie search section
    canvas.create_rectangle(
        0.0,
        60.0,
        960.0,
        90.0,
        fill="#D3D3D3",
        outline=""
    )

    # Load and display an image
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    # Display the "Recommended" text
    canvas.create_text(
        40.0,
        49.0,
        anchor="nw",
        text="Recommended",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )

    # Load and display an input field image
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    canvas.create_image(
        525.0,
        30.5,
        image=entry_image_1
    )

    # Create an input field for searching movies
    search = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#7E7E7E",
        highlightthickness=0,
        font=("Mohave", 11)
    )
    search.place(
        x=260.0,
        y=20.0,
        width=540.0,
        height=24.0
    )

    # Set the initial input field text
    search.insert(0, "SEARCH FOR MOVIES")
    search.bind("<FocusIn>", lambda args: close_window_searchSug())

    # Create a button for signing in or accessing booking history
    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        highlightthickness=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        command=lambda: close_window_bookinghistory(),
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    canvas.place(x=0, y=0)

    # Create text and buttons for recommended movies
    canvas.create_text(
        28.0,
        430.0,
        anchor="nw",
        text="The Godfather",
        fill="#000000",
        font=("Fira Code Medium", 14 * -1)
    )

    canvas.create_text(
        271.0,
        430.0,
        anchor="nw",
        text="PK",
        fill="#000000",
        font=("Fira Code Medium", 14 * -1)
    )

    canvas.create_text(
        510.0,
        430.0,
        anchor="nw",
        text="K.G.F: Chapter 1",
        fill="#000000",
        font=("Fira Code Medium", 14 * -1)
    )

    canvas.create_text(
        751.0,
        430.0,
        anchor="nw",
        text="Mission Mangal",
        fill="#000000",
        font=("Fira Code Medium", 14 * -1)
    )

    # Create buttons for recommended movies with images
    mmImg = PhotoImage(
        file=relative_to_assets("mm.png"))
    mmButton = Button(
        image=mmImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_mm(),
        relief="flat"
    )
    mmButton.place(
        x=750.0,
        y=155.0,
        width=180.0,
        height=260.0
    )

    kgfImg = PhotoImage(
        file=relative_to_assets("kgf.png"))
    kgfButton = Button(
        image=kgfImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_kgf(),
        relief="flat"
    )
    kgfButton.place(
        x=507.0,
        y=155.0,
        width=180.0,
        height=260.0
    )

    pkImg = PhotoImage(
        file=relative_to_assets("pk.png"))
    pkButton = Button(
        image=pkImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_pk(),
        relief="flat"
    )
    pkButton.place(
        x=269,
        y=155.0,
        width=180.0,
        height=260.0
    )

    godImg = PhotoImage(
        file=relative_to_assets("godf.png"))
    godButton = Button(
        image=godImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_godfather(),
        relief="flat"
    )
    godButton.place(
        x=26,
        y=155,
        width=180.0,
        height=260.0
    )

    # Make the window non-resizable
    window.resizable(False, False)
    window.mainloop()


def theatreSelection():
    global movieName

    try:
        # Attempt to access a Hollywood movie
        temp = Project.hollywoodMovies[str(movieName)]
    except:
        # If not found, access a Bollywood movie
        temp = Project.bollywoodMovies[str(movieName)]

    # Define a function to close the window and go back to the homepage
    def close_window_homepage():
        window.destroy()
        homepage()
        window.protocol("WM_DELETE_WINDOW", close_window_homepage)

    # Define a function to close the window and go to seat selection
    def close_window_seats():
        window.destroy()
        seat_selection()
        window.protocol("WM_DELETE_WINDOW", close_window_seats)

    # Define a function to close the window and go to booking history
    def close_window_bookinghistory():
        window.destroy()
        bookinghistory()
        window.protocol("WM_DELETE_WINDOW", close_window_bookinghistory)

    # Define a function to delete the text in the search field
    def delete_entry_text():
        search.delete('0', 'end')
        search.configure(fg="#000000")

    # Define a function to draw a rounded rectangle
    def round_rectangle(x1, y1, x2, y2, radius, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    window = Tk()
    window.title("Cinemate")
    window.geometry("960x540")
    window.configure(bg="#E5E5E5")

    canvas = Canvas(
        window,
        bg="#E5E5E5",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        0.0,
        60.0,
        960.0,
        90.0,
        fill="#D3D3D3",
        outline=""
    )

    canvas.create_text(
        375.0,
        63.0,
        anchor="nw",
        text=str(movieName),
        fill="#0B1E32",
        font=("Cinzel", 20 * -1, "bold")
    )

    # Shapes and Text for Details
    round_rectangle(
        10.0,
        362.0,
        950.0,
        442.0,
        radius=25.0,
        fill="#FFFFFF",
        outline="")

    round_rectangle(
        10.0,
        450.0,
        950.0,
        530.0,
        radius=25.0,
        fill="#FFFFFF",
        outline="")

    round_rectangle(
        10.0,
        274.0,
        950.0,
        354.0,
        radius=25.0,
        fill="#FFFFFF",
        outline="")

    round_rectangle(
        10.0,
        186.0,
        950.0,
        266.0,
        radius=25.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        47.0,
        232.0,
        anchor="nw",
        text="Digital Ticket",
        fill="#2A9D8F",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        47.0,
        320.0,
        anchor="nw",
        text="Digital Ticket",
        fill="#2A9D8F",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        47.0,
        408.0,
        anchor="nw",
        text="Digital Ticket",
        fill="#2A9D8F",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        47.0,
        496.0,
        anchor="nw",
        text="Digital Ticket",
        fill="#2A9D8F",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        47.0,
        200.0,
        anchor="nw",
        text=temp[1][0],
        fill="#264653",
        font=("Nokora Black", 14 * -1)
    )

    canvas.create_text(
        47.0,
        288.0,
        anchor="nw",
        text=temp[2][0],
        fill="#264653",
        font=("Nokora Black", 14 * -1)
    )

    canvas.create_text(
        47.0,
        376.0,
        anchor="nw",
        text=temp[3][0],
        fill="#264653",
        font=("Nokora Black", 14 * -1)
    )

    canvas.create_text(
        47.0,
        464.0,
        anchor="nw",
        text=temp[4][0],
        fill="#264653",
        font=("Nokora Black", 14 * -1)
    )

    round_rectangle(
        10.0,
        98.0,
        950.0,
        178.0,
        fill="#FFFFFF",
        radius=25.0,
        outline="")

    canvas.create_text(
        47.0,
        108.0,
        anchor="nw",
        text=temp[0][0],
        fill="#264653",
        font=("Nokora Black", 14 * -1)
    )

    canvas.create_text(
        47.0,
        140.0,
        anchor="nw",
        text="Digital Ticket",
        fill="#2A9D8F",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        130.0,
        140.0,
        anchor="nw",
        text="🧋 Food & Beverage",
        fill="#E76F51",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        130.0,
        233.0,
        anchor="nw",
        text="🧋 Food & Beverage",
        fill="#E76F51",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        130.0,
        321.0,
        anchor="nw",
        text="🧋 Food & Beverage",
        fill="#E76F51",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        130.0,
        409.0,
        anchor="nw",
        text="🧋 Food & Beverage",
        fill="#E76F51",
        font=("Nokora", 11 * -1)
    )

    canvas.create_text(
        125.0,
        498.0,
        anchor="nw",
        text="🧋 Food & Beverage",
        fill="#E76F51",
        font=("Nokora", 11 * -1)
    )

    # Button Functions
    def button_1_command():
        global theatreName, time
        theatreName = temp[0][0]
        time = temp[0][1]
        close_window_seats()

    def button_2_command():
        global theatreName, time
        theatreName = temp[1][0]
        time = temp[1][1]
        close_window_seats()

    def button_9_command():
        global theatreName, time
        theatreName = temp[2][0]
        time = temp[2][1]
        close_window_seats()

    def button_10_command():
        global theatreName, time
        theatreName = temp[3][0]
        time = temp[3][1]
        close_window_seats()

    def button_11_command():
        global theatreName, time
        theatreName = temp[4][0]
        time = temp[4][1]
        close_window_seats()

    button_image_1 = PhotoImage(
        file=relative_to_assets("redBorderButton.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        text=f"{temp[0][1]}",
        font=("Nokora Black", 14 * -1),
        fg="#DC143C",
        compound="center",
        command=button_1_command,
        relief="flat"
    )

    button_1.place(
        x=320.0,
        y=110.0,
        width=120.0,
        height=50.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("redBorderButton.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        text=f"{temp[1][1]}",
        font=("Nokora Black", 14 * -1),
        fg="#DC143C",
        compound="center",
        command=button_2_command,
        relief="flat"
    )
    button_2.place(
        x=320.0,
        y=205.0,
        width=120.0,
        height=50.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("redBorderButton.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        text=f"{temp[2][1]}",
        font=("Nokora Black", 14 * -1),
        fg="#DC143C",
        compound="center",
        command=button_9_command,
        relief="flat"
    )
    button_9.place(
        x=320.0,
        y=289.0,
        width=120.0,
        height=50.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("redBorderButton.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        text=f"{temp[3][1]}",
        font=("Nokora Black", 14 * -1),
        fg="#DC143C",
        compound="center",
        command=button_10_command,
        relief="flat"
    )
    button_10.place(
        x=320.0,
        y=377.0,
        width=120.0,
        height=50.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("redBorderButton.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        text=f"{temp[4][1]}",
        font=("Nokora Black", 14 * -1),
        fg="#DC143C",
        compound="center",
        command=button_11_command,
        relief="flat"
    )
    button_11.place(
        x=320.0,
        y=465.0,
        width=120.0,
        height=50.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_3.place(
        x=480.0,
        y=205.0,
        width=120.0,
        height=50.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_4.place(
        x=480.0,
        y=376.0,
        width=120.0,
        height=50.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_5.place(
        x=640.0,
        y=465.0,
        width=120.0,
        height=50.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_6.place(
        x=480.0,
        y=465.0,
        width=120.0,
        height=50.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_7.place(
        x=800.0,
        y=464.0,
        width=120.0,
        height=50.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        highlightthickness=0,
        relief="flat"
    )
    button_8.place(
        x=640.0,
        y=205.0,
        width=120.0,
        height=50.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("greyBorderButton.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        text="N/A",
        font=("Nokora Black", 14 * -1),
        fg="#949494",
        compound="center",
        relief="flat"
    )
    button_12.place(
        x=480.0,
        y=110.0,
        width=120.0,
        height=50.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        960.0,
        60.0,
        fill="#0B1E32",
        outline="")

    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        525.0,
        30.5,
        image=entry_image_1
    )

    search = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#7E7E7E",
        highlightthickness=0,
        font=("Mohave", 11)
    )
    search.place(
        x=260.0,
        y=19.0,
        width=540.0,
        height=24.0
    )
    search.insert(0, "SEARCH FOR MOVIES")
    search.bind("<FocusIn>", lambda args: delete_entry_text())

    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        highlightthickness=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        command=lambda: close_window_bookinghistory(),
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    backImg = PhotoImage(
        file=relative_to_assets("back.png"))
    backButton = Button(
        image=backImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_homepage(),
        relief="flat"
    )
    backButton.place(
        x=919.0,
        y=22.0,
        width=16.0,
        height=20.0
    )

    canvas.create_rectangle(
        0.0,
        60.0,
        250.0,
        90.0,
        fill="#D9D9D9",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    canvas.create_text(
        40.0,
        49.0,
        anchor="nw",
        text="Movie Name",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


def bookinghistory():
    global user
    window = Tk()
    window.title("Cinemate")
    window.geometry("960x540")
    window.configure(bg="#E5E5E5")

    def round_rectangle(x1, y1, x2, y2, radius, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        # type: ignore
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def close_window_homepage():
        window.destroy()
        homepage()
        window.protocol("WM_DELETE_WINDOW", close_window_homepage)

    canvas = Canvas(
        window,
        bg="#E5E5E5",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        60.0,
        960.0,
        90.0,
        fill="#D3D3D3",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    # Shapes and Text for Details
    canvas.create_text(
        25.0,
        49.0,
        anchor="nw",
        text="Booking History",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )

    round_rectangle(
        10.0,
        98.0,
        950.0,
        520.0,
        radius=25.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        65.0,
        115.0,
        anchor="nw",
        text="Movie Name",
        fill="#264653",
        font=("Nokora Black", 18 * -1)
    )

    canvas.create_text(
        286.0,
        115.0,
        anchor="nw",
        text="Theatre Name",
        fill="#264653",
        font=("Nokora Black", 18 * -1)
    )

    canvas.create_text(
        542.0,
        115.0,
        anchor="nw",
        text="Time",
        fill="#264653",
        font=("Nokora Black", 18 * -1)
    )

    canvas.create_text(
        773.0,
        115.0,
        anchor="nw",
        text="Seat",
        fill="#264653",
        font=("Nokora Black", 18 * -1)
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        960.0,
        60.0,
        fill="#0B1E32",
        outline="")

    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)

    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        highlightthickness=0,
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    backImg = PhotoImage(
        file=relative_to_assets("back.png"))
    backButton = Button(
        image=backImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_homepage(),
        relief="flat"
    )
    backButton.place(
        x=919.0,
        y=22.0,
        width=16.0,
        height=20.0
    )

    # Open a JSON file for reading
    with open("DSA Sem-3 Cinemate Project\\browse.json", "r") as f:
        data = json.load(f)  # Load data from the JSON file
        lis = []  # Create an empty list to store user-related data
        movie = []  # Create a list to store movie details

        # Iterate through the data to find entries related to the user
        for i in data:
            ind = i.find(str(user))
            if ind != -1:
                lis.append(i)  # Append user-related entries to the list 'lis'

    # Initialize variables for positioning elements on the canvas
    line_y = 145
    detail_y = 165

    # Iterate through user-related movie data
    for i in lis:
        movie.append(data[i])  # Append movie details to the 'movie' list

    # Loop to display up to 5 user-related movies on the canvas
    for i in range(len(movie)):
        if i < 5:
            # Create a black rectangle as a separator line
            canvas.create_rectangle(
                20.0,
                line_y,
                940.0,
                line_y,
                fill="#000000",
                outline="")

            line_y += 75

            canvas.create_text(
                64.0,
                detail_y,
                anchor="nw",
                text=movie[i][0],
                fill="#000000",
                font=("Roboto Mono", 12 * -1))

            canvas.create_text(
                330.0,
                detail_y,
                anchor="nw",
                text=movie[i][1],
                fill="#000000",
                font=("Roboto Mono", 12 * -1))

            canvas.create_text(
                551.0,
                detail_y,
                anchor="nw",
                text=movie[i][2],
                fill="#000000",
                font=("Roboto Mono", 12 * -1))

            canvas.create_text(
                780.0,
                detail_y,
                anchor="nw",
                text=movie[i][3],
                fill="#000000",
                font=("Roboto Mono", 12 * -1))

            # Update Y coordinate for the next movie details
            detail_y += 75

        else:
            break

    window.resizable(False, False)
    window.mainloop()


def seat_selection():
    global movieName

    # Function to close the window and return to the theatre selection
    def close_window_theatreSelection():
        window.destroy()
        theatreSelection()
        window.protocol("WM_DELETE_WINDOW", close_window_theatreSelection)

    # Function to close the window and return to the ticket selection
    def close_window_ticket():
        window.destroy()
        ticket()
        window.protocol("WM_DELETE_WINDOW", close_window_ticket)

    # Function to close the window and return to the booking history
    def close_window_bookinghistory():
        window.destroy()
        bookinghistory()
        window.protocol("WM_DELETE_WINDOW", close_window_bookinghistory)

    # Function to create a 2D matrix representing the seat availability
    def create_seat_matrix():
        seat_matrix = [
            [random.choice([BOOKED, AVAILABLE]) for _ in range(12)] for _ in range(12)
        ]
        return seat_matrix

    # Function to create a selection interface for the number of seats
    def create_num_seats_selection():
        def select_num_seats(num):
            nonlocal num_seats
            num_seats = num
            num_seats_label.config(
                text=f"Number of Seats to Book: {num_seats:02d}")
            num_seats_selection_frame.pack_forget()
            create_seat_selection_matrix()

        num_seats_selection_frame = Frame(window)
        num_seats_selection_frame.pack()

        for i in range(1, 10):
            button = tk.Button(
                num_seats_selection_frame,
                text=str(i),
                font=("Arial", 14),
                command=lambda n=i: select_num_seats(n),
            )
            button.grid(row=0, column=i, padx=5)

    # Function to create a matrix for seat selection
    def create_seat_selection_matrix():
        def select_seat(row, col):
            if seat_matrix[row][col] == AVAILABLE:
                seat_matrix[row][col] = SELECTED
                buttons[row][col].config(bg=SELECTED_COLOR)
            elif seat_matrix[row][col] == SELECTED:
                seat_matrix[row][col] = AVAILABLE
                buttons[row][col].config(bg=AVAILABLE_COLOR)

        def confirm_booking():
            global seats
            selected_seats = [
                (row, col)
                for row in range(10)
                for col in range(10)
                if seat_matrix[row][col] == SELECTED
            ]
            seats = [(row + 1, col + 1) for row, col in selected_seats]
            if len(selected_seats) == 0:
                messagebox.showinfo("Booking Confirmation",
                                    "No seats selected.")
            elif len(selected_seats) != num_seats:
                messagebox.showinfo(
                    "Booking Confirmation", f"Please select {num_seats:02d} seats."
                )
            else:
                messagebox.showinfo("Booking Confirmation",
                                    f"Selected seats: {seats}")
                close_window_ticket()

        # Label for displaying the number of seats to book
        num_seats_label.config(
            text="Number of Seats to Book:", font=("Mohave", 18))
        num_seats_label.pack(side="top", pady=(2, 0))
        buttons = []

        for row in range(10):
            row_buttons = []
            for col in range(10):
                state = seat_matrix[row][col]
                bg_color = (
                    BOOKED_COLOR if state == BOOKED
                    else AVAILABLE_COLOR if state == AVAILABLE
                    else SELECTED_COLOR
                )
                button_text = "      "
                button = tk.Button(
                    seat_frame,
                    text=button_text,
                    bg=bg_color,
                    command=lambda r=row, c=col: select_seat(r, c),
                )
                button.grid(row=row + 1, column=col + 1)
                row_buttons.append(button)
            buttons.append(row_buttons)

        book_button = tk.Button(text="Book Tickets", command=confirm_booking)
        book_button.pack(side="top", pady=(10, 0))

        # Remove "Select seats" text and shift the matrix up by 10 pixels
        num_seats_label.pack_forget()
        # Adjust padding to shift up by 10 pixels
        seat_frame.pack(pady=(20, 0))
        return book_button

    window = Tk()
    window.title("Cinemate")
    window.geometry("960x540")  # Adjust window height for a 12x12 matrix
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#E5E5E5",
        height=720,  # Adjust canvas height
        width=960,
        bd=0,
        highlightthickness=0,
        relief="flat",
    )

    canvas.create_rectangle(0.0, 0.0, 960.0, 60.0, fill="#0B1E32", outline="")

    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    # Shapes and Text for Details
    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)
    canvas.create_rectangle(
        0.0,
        60.0,
        960.0,
        90.0,
        fill="#D3D3D3",
        outline=""
    )

    backImg = PhotoImage(
        file=relative_to_assets("back.png"))
    backButton = Button(
        image=backImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_theatreSelection(),
        relief="flat"
    )
    backButton.place(
        x=919.0,
        y=22.0,
        width=16.0,
        height=20.0
    )

    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        highlightthickness=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        command=lambda: close_window_bookinghistory(),
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    canvas.place(x=0, y=0)
    movie_label = Label(
        text=str(movieName),
        bg="#E5E5E5",
        font=("Cinzel", 20),
        justify="center",
    )
    movie_label.pack(side="top", pady=(90, 0))  # Adjust padding

    showtime_and_theatre_label = Label(
        text=f"Time: {time}     Theatre: {theatreName}",
        bg="#E5E5E5",
        font=("Mohave", 16),
        justify="center",
    )
    showtime_and_theatre_label.pack(side="top", pady=(10, 0))

    num_seats_label = Label(text="Number of Seats to Book:",
                            bg="#E5E5E5", font=("Mohave", 18))
    num_seats_label.pack(side="top", pady=(40, 0))

    num_seats = 1  # Default number of seats

    create_num_seats_selection()

    seat_frame = Frame(window)
    seat_frame.pack()

    for col in range(13):  # Adjust columns
        seat_frame.grid_columnconfigure(col, pad=5)

    for row in range(13):  # Adjust rows
        seat_frame.grid_rowconfigure(row, pad=5)

    seat_matrix = create_seat_matrix()

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    canvas.create_text(
        40.0,
        49.0,
        anchor="nw",
        text="Seat Selection",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )

    window.resizable(False, False)
    window.mainloop()


def ticket():
    global user
    window = Tk()
    window.title("Cinemate")
    window.geometry("960x540")
    window.configure(bg="#FFFFFF")
    window.title("Ticket Printing")

    def close_window_homepage():
        window.destroy()
        homepage()
        window.protocol("WM_DELETE_WINDOW", close_window_homepage)

    def close_window_bookinghistory():
        window.destroy()
        bookinghistory()
        window.protocol("WM_DELETE_WINDOW", close_window_bookinghistory)

    # Open the JSON file for reading and writing (r+ mode)
    with open("DSA Sem-3 Cinemate Project\\browse.json", "r+") as f:
        data = json.load(f)  # Load the existing data from the JSON file
        # Generate a unique string using user information and random letters
        str3 = str(user) + "_" + random.choice(string.ascii_letters) + \
            random.choice(string.ascii_letters)

        # Add a new entry to the data with user, movie, theatre, time, and seats information
        data[str3] = [movieName, theatreName, time, seats]

        # Move the file pointer to the beginning of the file
        f.seek(0)
        f.truncate()  # Truncate (clear) the existing file content

        # Write the modified data back to the JSON file with proper indentation
        json.dump(data, f, indent=4)

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="flat",
    )

    canvas.create_rectangle(0.0, 0.0, 960.0, 60.0, fill="#0B1E32", outline="")

    canvas.create_text(
        40.0,
        10.0,
        anchor="nw",
        text="CINEMATE",
        fill="#FFFFFF",
        font=("Monoton", 24 * -1)
    )

    pop_image = PhotoImage(file=relative_to_assets("pop.png"))
    pop = canvas.create_image(
        207.0,
        30.0,
        image=pop_image)

    signinImg = PhotoImage(
        file=relative_to_assets("signin.png"))
    signinButton = Button(
        image=signinImg,
        borderwidth=0,
        highlightthickness=0,
        text=str(user),
        font=("Bungee", 10 * -1),
        fg="#FFFFFF",
        compound="center",
        command=lambda: close_window_bookinghistory(),
        relief="flat"
    )
    signinButton.place(
        x=830.0,
        y=19.0,
        width=65.0,
        height=25.0
    )

    backImg = PhotoImage(
        file=relative_to_assets("back.png"))

    backButton = Button(
        image=backImg,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: close_window_homepage(),
        relief="flat"
    )
    backButton.place(
        x=919.0,
        y=22.0,
        width=16.0,
        height=20.0
    )
    canvas.place(x=0, y=0)
    ticket_back = PhotoImage(file=relative_to_assets("ticket_back (2).png"))
    ticket_label_back = Label(image=ticket_back, bg="#FFFFFF")
    # Initialize the flag to determine whether to display the back side of the ticket
    show_ticket_back = False

    # Function to update flags and display elements on the ticket
    def update_flag_and_display_elements():
        nonlocal show_ticket_back
        show_ticket_back = True  # Update the show_ticket_back flag to True

        # Remove the existing ticket label
        ticket_label.destroy()

        # Place various labels and elements on the ticket
        ticket_label_back.place(x=x_center + 40, y=y_center + 38)
        audi_label.place(x=260, y=346)
        audi_label2.place(x=435, y=373)
        booking_id_label.place(x=285, y=225)
        seat_label.place(x=260, y=382)
        seat_label2.place(x=565, y=375)
        seat_label3.place(x=730, y=285)
        time_label.place(x=230, y=413)
        time_label2.place(x=440, y=403)
        movie_name_label.place(x=510, y=305)
        thank_you.place(x=300, y=490)

    style = ttk.Style()
    style.configure("TButton", font=("Mohave", 20, "bold"),
                    background="#FFFFFF", justify="center")
    ticket = ttk.Button(
        text="Your Ticket",
        style="TButton",
        command=update_flag_and_display_elements
    )

    # Shapes and Text for Details
    ticket_image = PhotoImage(file=relative_to_assets("ticket_front.png"))
    ticket_label = Label(image=ticket_image, bg="#FFFFFF")
    audi = random.randint(1, 4)
    booking_id = "".join(random.choices(
        string.ascii_uppercase + string.digits, k=7))
    audi_label = Label(
        text=f"{audi}",
        bg="#FFFFFF",
        font=("Nokora", 15),
        justify="center",
    )
    audi_label2 = Label(
        text=f"{audi}",
        bg="#FFFFFF",
        font=("Nokora", 15),
        justify="center",
    )
    booking_id_label = Label(
        text=f"{booking_id}",
        bg="#30444c",
        font=("Nokora", 15),
        fg="#FFB6C1",
        justify="center",
    )
    seat_label = Label(
        text=f"{data[str3][3]}",
        bg="#FFFFFF",
        font=("", 13),
        justify="center",
    )
    seat_label2 = Label(
        text=f"{data[str3][3]}",
        bg="#FFFFFF",
        font=("", 13),
        justify="center",
    )
    seat_label3 = Label(
        text=f"{data[str3][3]}",
        bg="#FFFFFF",
        font=("", 13),
        justify="center",
    )
    movie_name_label = Label(
        text=f"{data[str3][0]}",
        bg="#FFFFFF",
        font=("Nokora", 15),
        justify="center",
    )
    time_label = Label(
        text=f"{data[str3][2]}",
        bg="#FFFFFF",
        font=("Nokora", 15),
        justify="center",
    )
    time_label2 = Label(
        text=f"{data[str3][2]}",
        bg="#FFFFFF",
        font=("Nokora", 15),
        justify="center",
    )

    thank_you = Label(
        text="✅ Thank you for your purchase!",
        bg="#3CB043",
        font=("Bungee", 12),
        justify="right",
        fg="#FFFFFF",
    )

    ticket.place(x=420, y=80)
    canvas_width = 960  # Width of the canvas
    canvas_height = 600  # Height of the canvas
    rectangle_width = 740  # Width of the gray rectangle
    rectangle_height = 312

    x_center = (canvas_width - rectangle_width) / 2
    y_center = (canvas_height - rectangle_height) / 2

    # Create a light gray rectangle behind the photo with extra width and height
    gray_rectangle = canvas.create_rectangle(
        x_center + 5,  # Centered x position
        y_center + 20,  # Centered y position
        x_center + rectangle_width + 40,  # Set width to 740
        y_center + rectangle_height + 20,  # Set height to 312
        fill="#EAEAEA",  # Light gray color
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        125.0,
        75.0,
        image=image_image_1
    )

    canvas.create_text(
        25.0,
        49.0,
        anchor="nw",
        text="Ticket Printing",
        fill="#FFFFFF",
        font=("Bungee", 20 * -1)
    )

    ticket_label.place(x=x_center + 40, y=y_center + 38)
    window.mainloop()


login()
