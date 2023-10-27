import json
import os
import random
from tabulate import tabulate


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node  # type: ignore

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def save(self):
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.data)
            temp = temp.next
        return lst

    def fetch_by_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative.")
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        raise IndexError("Index out of range.")


# Path to User Data
pathUserData = r' '
# Path to Browse Data
pathBrowseData = r' '

# GLOBAL
# List of Hollywood Movies with Theatres and Timings
hollywoodMovies = {
    "The Shawshank Redemption": [["AMC Theatres", "9:00 AM"], ["Regal Cinemas", "10:15 AM"], ["Cinemark", "1:30 PM"], ["Cinepolis", "4:45 PM"], ["Showcase Cinemas", "7:00 PM"]],
    "The Godfather": [["Harkins Theatres", "10:00 AM"], ["Marcus Theatres", "1:15 PM"], ["Vue Cinemas", "4:30 PM"], ["Empire Cinemas", "7:45 PM"], ["Laemmle Theatres", "10:00 PM"]],
    "The Dark Knight": [["AMC Theatres", "10:30 AM"], ["Odeon Cinemas", "1:45 PM"], ["Cineplex Cinemas", "5:00 PM"], ["Landmark Cinemas", "8:15 PM"], ["PVR", "11:30 PM"]],
    "Pulp Fiction": [["Cinemark", "11:00 AM"], ["Harkins Theatres", "2:15 PM"], ["ArcLight Cinemas", "5:30 PM"], ["Pacific Theatres", "8:45 PM"], ["INOX", "12:00 AM"]],
    "Schindler's List": [["Regal Cinemas", "11:30 AM"], ["Cinema City", "2:45 PM"], ["Vue Cinemas", "6:00 PM"], ["Marcus Theatres", "9:15 PM"], ["Cinepolis", "1:30 AM"]],
    "Forrest Gump": [["Empire Cinemas", "9:00 AM"], ["Laemmle Theatres", "11:15 AM"], ["Showcase Cinemas", "2:30 PM"], ["AMC Theatres", "5:45 PM"], ["PVR", "9:00 PM"]],
    "Fight Club": [["Harkins Theatres", "9:30 AM"], ["Cineplex Cinemas", "12:45 PM"], ["Regal Cinemas", "4:00 PM"], ["Cinemark", "7:15 PM"], ["Pacific Theatres", "10:30 PM"]],
    "Inception": [["Cinemark", "10:00 AM"], ["PVR", "1:15 PM"], ["ArcLight Cinemas", "4:30 PM"], ["Marcus Theatres", "7:45 PM"], ["Cinema City", "11:00 PM"]],
    "The Matrix": [["Vue Cinemas", "10:30 AM"], ["INOX", "1:45 PM"], ["Laemmle Theatres", "5:00 PM"], ["Cinepolis", "8:15 PM"], ["Cineplex Cinemas", "12:30 AM"]],
    "Gladiator": [["Cinema City", "11:00 AM"], ["Cinemark", "2:15 PM"], ["Harkins Theatres", "5:30 PM"], ["Empire Cinemas", "8:45 PM"], ["Regal Cinemas", "12:00 AM"]],
    "The Lord of the Rings: The Fellowship of the Ring": [["Showcase Cinemas", "11:30 AM"], ["PVR", "2:45 PM"], ["Vue Cinemas", "6:00 PM"], ["AMC Theatres", "9:15 PM"], ["INOX", "1:30 AM"]],
    "Titanic": [["Pacific Theatres", "9:00 AM"], ["Cinepolis", "11:15 AM"], ["Marcus Theatres", "2:30 PM"], ["Cinemark", "5:45 PM"], ["Laemmle Theatres", "9:00 PM"]],
    "Jurassic Park": [["Cineplex Cinemas", "9:30 AM"], ["Regal Cinemas", "12:45 PM"], ["Cinema City", "4:00 PM"], ["Harkins Theatres", "7:15 PM"], ["ArcLight Cinemas", "10:30 PM"]],
    "Avatar": [["INOX", "10:00 AM"], ["Empire Cinemas", "1:15 PM"], ["PVR", "4:30 PM"], ["Cineplex Cinemas", "7:45 PM"], ["Cinemark", "11:00 PM"]],
    "Star Wars: Episode IV - A New Hope": [["Marcus Theatres", "10:30 AM"], ["Vue Cinemas", "1:45 PM"], ["AMC Theatres", "5:00 PM"], ["Regal Cinemas", "8:15 PM"], ["Pacific Theatres", "12:30 AM"]],
    "The Avengers": [["Cinepolis", "11:00 AM"], ["Laemmle Theatres", "2:15 PM"], ["Cinemark", "4:30 PM"], ["Cinema City", "7:45 PM"], ["Showcase Cinemas", "11:00 PM"]],
    "Jaws": [["Harkins Theatres", "11:30 AM"], ["PVR", "2:45 PM"], ["INOX", "5:00 PM"], ["Cineplex Cinemas", "8:15 PM"], ["Vue Cinemas", "12:30 AM"]],
    "E.T. the Extra-Terrestrial": [["Regal Cinemas", "9:00 AM"], ["Cinemark", "11:15 AM"], ["Pacific Theatres", "2:30 PM"], ["Empire Cinemas", "5:45 PM"], ["Marcus Theatres", "9:00 PM"]],
    "Casablanca": [["Cineplex Cinemas", "9:30 AM"], ["Cinema City", "12:45 PM"], ["Cinemark", "4:00 PM"], ["PVR", "7:15 PM"], ["Laemmle Theatres", "10:30 PM"]],
    "Gone with the Wind": [["AMC Theatres", "10:00 AM"], ["Showcase Cinemas", "1:15 PM"], ["INOX", "4:30 PM"], ["Regal Cinemas", "7:45 PM"], ["Vue Cinemas", "11:00 PM"]],
    "Black Panther": [["Empire Cinemas", "10:30 AM"], ["Marcus Theatres", "1:45 PM"], ["Harkins Theatres", "5:00 PM"], ["ArcLight Cinemas", "8:15 PM"], ["Cinema City", "12:30 AM"]]
}

# List of Bollywood Movies with Theatres and Timings
bollywoodMovies = {
    "Sholay": [["PVR Cinemas", "9:00 AM"], ["INOX", "11:15 AM"], ["Cinepolis", "1:30 PM"], ["Wave Cinemas", "3:45 PM"], ["Carnival Cinemas", "6:00 PM"]],
    "Dilwale Dulhania Le Jayenge": [["BIG Cinemas", "10:00 AM"], ["Fun Cinemas", "12:15 PM"], ["SRS Cinemas", "2:30 PM"], ["Mukta A2 Cinemas", "4:45 PM"], ["Cinemax", "7:00 PM"]],
    "Kabhi Khushi Kabhie Gham": [["Miraj Cinemas", "11:00 AM"], ["Cinemax", "1:15 PM"], ["City Pride", "3:30 PM"], ["CineMAX", "5:45 PM"], ["Satyam Cineplexes", "8:00 PM"]],
    "3 Idiots": [["Wave Cinemas", "9:30 AM"], ["PVR Cinemas", "11:45 AM"], ["INOX", "2:00 PM"], ["Cinepolis", "4:15 PM"], ["Carnival Cinemas", "6:30 PM"]],
    "Kuch Kuch Hota Hai": [["Mukta A2 Cinemas", "10:30 AM"], ["City Pride", "12:45 PM"], ["Fun Cinemas", "3:00 PM"], ["BIG Cinemas", "5:15 PM"], ["Miraj Cinemas", "7:30 PM"]],
    "Lagaan": [["Cinemax", "10:00 AM"], ["SRS Cinemas", "12:15 PM"], ["Satyam Cineplexes", "2:30 PM"], ["PVR Cinemas", "4:45 PM"], ["INOX", "7:00 PM"]],
    "Chak De! India": [["CineMAX", "10:30 AM"], ["Carnival Cinemas", "12:45 PM"], ["Wave Cinemas", "3:00 PM"], ["Mukta A2 Cinemas", "5:15 PM"], ["City Pride", "7:30 PM"]],
    "Mughal-e-Azam": [["PVR Cinemas", "11:00 AM"], ["Fun Cinemas", "1:15 PM"], ["Cinepolis", "3:30 PM"], ["Satyam Cineplexes", "5:45 PM"], ["Carnival Cinemas", "8:00 PM"]],
    "Dil Chahta Hai": [["Mukta A2 Cinemas", "11:30 AM"], ["INOX", "1:45 PM"], ["Cinemax", "4:00 PM"], ["BIG Cinemas", "6:15 PM"], ["Miraj Cinemas", "8:30 PM"]],
    "Baahubali: The Beginning": [["CineMAX", "9:00 AM"], ["Satyam Cineplexes", "11:15 AM"], ["PVR Cinemas", "1:30 PM"], ["City Pride", "3:45 PM"], ["Wave Cinemas", "6:00 PM"]],
    "Baahubali 2: The Conclusion": [["INOX", "9:30 AM"], ["Carnival Cinemas", "11:45 AM"], ["Cinemax", "2:00 PM"], ["Fun Cinemas", "4:15 PM"], ["Mukta A2 Cinemas", "6:30 PM"]],
    "Padmaavat": [["BIG Cinemas", "9:00 AM"], ["Wave Cinemas", "11:15 AM"], ["Miraj Cinemas", "1:30 PM"], ["PVR Cinemas", "3:45 PM"], ["INOX", "6:00 PM"]],
    "Kesari": [["City Pride", "10:00 AM"], ["CineMAX", "12:15 PM"], ["SRS Cinemas", "2:30 PM"], ["Cinemax", "4:45 PM"], ["Satyam Cineplexes", "7:00 PM"]],
    "Bajrangi Bhaijaan": [["Cinepolis", "10:30 AM"], ["Carnival Cinemas", "12:45 PM"], ["Wave Cinemas", "3:00 PM"], ["BIG Cinemas", "5:15 PM"], ["Miraj Cinemas", "7:30 PM"]],
    "PK": [["PVR Cinemas", "11:00 AM"], ["INOX", "1:15 PM"], ["CineMAX", "3:30 PM"], ["SRS Cinemas", "5:45 PM"], ["Fun Cinemas", "8:00 PM"]],
    "Sultan": [["Mukta A2 Cinemas", "11:30 AM"], ["City Pride", "1:45 PM"], ["Satyam Cineplexes", "4:00 PM"], ["Cinemax", "6:15 PM"], ["Cinepolis", "8:30 PM"]],
    "Dangal": [["Wave Cinemas", "9:30 AM"], ["PVR Cinemas", "11:45 AM"], ["INOX", "2:00 PM"], ["Carnival Cinemas", "4:15 PM"], ["Cinemax", "6:30 PM"]],
    "Kabir Singh": [["CineMAX", "10:30 AM"], ["Miraj Cinemas", "12:45 PM"], ["SRS Cinemas", "3:00 PM"], ["Fun Cinemas", "5:15 PM"], ["Mukta A2 Cinemas", "7:30 PM"]],
    "Uri: The Surgical Strike": [["BIG Cinemas", "10:00 AM"], ["Wave Cinemas", "12:15 PM"], ["Cinemax", "2:30 PM"], ["Satyam Cineplexes", "4:45 PM"], ["PVR Cinemas", "7:00 PM"]],
    "K.G.F: Chapter 1": [["Cinepolis", "9:00 AM"], ["INOX", "11:15 AM"], ["Carnival Cinemas", "1:30 PM"], ["Wave Cinemas", "3:45 PM"], ["Miraj Cinemas", "6:00 PM"]],
    "Mission Mangal": [["Wave Cinemas", "6:15 PM"], ["Cinemax", "8:30 PM"], ["City Pride", "10:45 PM"], ["Fun Cinemas", "12:00 AM"], ["BIG Cinemas", "2:15 AM"]]
}

userN = None  # Username
rlt_final_seats = []  # List of Seats Booked


# Initialize a 9x9 matrix of seats with '□' representing empty seats
seats = [['□' for _ in range(9)] for _ in range(9)]

# Randomly select and mark 25 seats as '■', representing booked seats
for i in range(25):
    row = random.randint(0, 8)  # Generate a random row index (0-8)
    col = random.randint(0, 8)  # Generate a random column index (0-8)
    seats[row][col] = '■'  # Mark the selected seat as '■' (booked)


# User
def user_data(x):
    # Define the filename for user data
    filename = pathUserData

    # Check if the file exists; if not, create an empty JSON file
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)

    # Open the file for reading and writing (r+ mode)
    with open(filename, "r+") as f:
        data = json.load(f)  # Load existing user data from the file
        data.update(x)  # Update user data with the provided data
        f.seek(0)  # Move the file pointer to the beginning of the file
        json.dump(data, f)  # Write the updated data back to the file


def booking_data(x):
    # Define the filename for booking data
    filename = pathBrowseData

    # Check if the file exists; if not, create an empty JSON file
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump({}, f)

    # Open the file for reading and writing (r+ mode)
    with open(filename, "r+") as f:
        data = json.load(f)  # Load existing booking data from the file
        data.update(x)  # Update booking data with the provided data
        f.seek(0)  # Move the file pointer to the beginning of the file
        json.dump(data, f)  # Write the updated data back to the file


def login_check():
    global userN  # Declare userN as a global variable to store the username
    userN = input("Enter Username: \n")  # Prompt the user to enter a username
    str2 = input("Enter Password: \n")  # Prompt the user to enter a password

    with open(pathUserData, 'r') as f:  # Open the user data file for reading
        data = json.load(f)  # Load user data from the file

    flag = False  # Initialize a flag to track if the username is found in the data

    # Iterate through the user data to check the username and password
    for user, passw in data.items():
        if userN == user:
            flag = True
            if str2 == passw:
                print("LOGIN SUCCESSFUL.")
                print("WELCOME")
            else:
                print("INCORRECT PASSWORD")
                print("The Passwords Are Case Sensitive")
                print("Please try again.")
                input("Press any key to continue...")
                os.system('CLS')
                login_check()

    if not flag:
        print("INVALID USERNAME OR PASSWORD")
        print("The Data Is Case Sensitive")
        print("Please try again.")
        input("Press any key to continue...")
        os.system('CLS')
        login_check()


def acc_create(str1, str2):
    # Open the user data file for reading and writing (r+ mode)
    with open(pathUserData, 'r+') as f:
        data = json.load(f)  # Load user data from the file

    flag = False  # Initialize a flag to track account creation status

    # Iterate through the user data to check if the username already exists
    for user, passw in data.items():
        if str1 == user:
            if str2 == passw:
                print("Account Already Exists!")
                print("Please Login.")
                input("Press any key to continue...")
                login_check()  # Redirect to the login function
                flag = True
                break
            else:
                print("Username Taken.")
                flag = True
                input("Press any key to continue...")
                os.system('CLS')  # Clear the console screen
                # Recursive call to create a new account
                acc_create(str1, str2)
                break

    if not flag:
        data[str1] = str2  # Add the new account to the user data
        user_data(data)  # Update the user data in the file
        print("ACCOUNT CREATED SUCCESSFULLY.")


# Movie Booking
def movie_selection_suggestions():
    # Display language options
    print("1. Hindi")
    print("2. English")

    # Prompt the user to choose a language
    choice = int(input("Please Select Movie Language: "))

    if choice == 1:
        lst = []  # Initialize a list to store movie suggestions
        for i, j in enumerate(bollywoodMovies):
            # Prompt the user to enter a movie search query
            search = input("Search your Movie: ")
            for i in bollywoodMovies:
                # Check if the query matches the beginning of any movie name
                if search[0:3].lower() in i.lower():
                    lst.append(i)  # Add matching movies to the list
            # Generate serial numbers for movie suggestions
            srno = [i + 1 for i in range(0, len(lst))]
            # Display movie suggestions in a tabulated format
            print(tabulate(zip(srno, lst), headers=[
                  'Serial No.', 'Movies'], tablefmt='psql'))
            print("")
            break

    elif choice == 2:
        lst = []  # Initialize a list to store movie suggestions
        for i, j in enumerate(hollywoodMovies):
            # Prompt the user to enter a movie search query
            search = input("Search your movie: ")
            for i in hollywoodMovies:
                # Check if the query matches the beginning of any movie name
                if search[0:3].lower() in i.lower():
                    lst.append(i)  # Add matching movies to the list
            # Generate serial numbers for movie suggestions
            srno = [i + 1 for i in range(0, len(lst))]
            # Display movie suggestions in a tabulated format
            print(tabulate(zip(srno, lst), headers=[
                  'Serial No.', 'Movies'], tablefmt='psql'))
            break
    else:
        # Display a message for an invalid language choice
        print("Invalid Choice")


def createMovies(lst):
    # Prompt the user to enter a movie name
    movieName = input('Enter Movie Name: ')
    # Add the movie name to the provided list (dictionary) as a key with a value of None
    lst[movieName] = None
    # Return the updated list and the movie name
    return lst, movieName


def deleteMovies(lst):
    # Prompt the user to enter a movie name for deletion
    movieName = input('Enter Movie Name: ')
    # Delete the movie name key from the provided list (dictionary)
    del lst[movieName]
    # Return the updated list
    return lst


def addition_movie_details(movie_language, movie_name):
    # Create an empty linked list to store theatre and time details
    temp = Linked_list()

    # Prompt the user to enter the number of theatres
    ask = int(input('Enter Number of Theatres: '))

    # Iterate for each theatre
    for k in range(ask):
        # Prompt the user to enter theatre name and time
        theatre = input('Enter Theatre Name: ')
        time = input('Enter Time: ')

        # Insert the theatre and time details into the linked list
        temp.insert((theatre, time))

    # Save the linked list in the provided dictionary with the movie name as the key
    movie_language[movie_name] = temp.save()


def theatre_selection(movie_name):
    # Check if the provided movie name is in the Bollywood movies database
    if movie_name in bollywoodMovies:
        # Display the theatre and timing details for the selected Bollywood movie using tabulate
        print(tabulate(bollywoodMovies[movie_name], headers=[
              'Theatre Name', 'Timings'], tablefmt='psql'))
    # Check if the provided movie name is in the Hollywood movies database
    elif movie_name in hollywoodMovies:
        # Display the theatre and timing details for the selected Hollywood movie using tabulate
        print(tabulate(hollywoodMovies[movie_name], headers=[
              'Theatre Name', 'Timings'], tablefmt='psql'))
    else:
        # If the movie name is not found, inform the user and suggest movie selection
        print("No such Movie Found.")
        movie_selection_suggestions()


# Movie-Seat Booking
def print_seating_chart():
    # Display the column numbers for seats
    print("  1 2 3 4 5 6 7 8 9")
    # Iterate through the rows of the seating chart
    for i, row in enumerate(seats, start=1):
        # Print the row number
        print(i, end=" ")
        # Print the seats in the current row
        for seat in row:
            print(seat, end=" ")
        # Move to the next line for the next row
        print()


def seat_selection():
    # Input the number of seats to book
    no_of_seats = int(input("Enter the number of seats: "))

    # Continue until all seats are booked
    while no_of_seats != 0:
        # Input the row and column number for the seat
        row = int(input("Enter the row number: ")) - 1
        col = int(input("Enter the column number: ")) - 1

        # Check if the seat is available
        if seats[row][col] == '□':
            # Book the seat
            seats[row][col] = '■'
            rlt_final_seats.append(f'{row + 1}|{col + 1}')
            print()
            # Display the updated seating chart
            print_seating_chart()
            print()
        else:
            # Seat is already booked, prompt for another seat
            print("Seat already booked. Please select another seat.")
            no_of_seats += 1
        # Decrement the number of seats to book
        no_of_seats -= 1


def ticket_print(temp, tempUser):
    # Display the ticket details using the tabulate function
    print(tabulate([list(temp[tempUser].values())], headers=[
        'Movie Name', 'Theatre Name', 'Time', 'Seat Number'], tablefmt="fancy_grid"))

    # Print a confirmation message
    print("Your ticket has been booked")
    print("Thank you for booking with us")
    print("Enjoy your movie")

    # Update the booking data with the new booking
    booking_data(temp)


def booking_history(tempUser):
    # Define the path to the JSON file containing booking data
    filename = pathBrowseData

    # Read the data from the JSON file
    with open(filename, "r") as f:
        data = json.load(f)

        # Iterate through the keys (which are user names) in the data
        for i in data.keys():
            if tempUser in i:  # Check if the user name matches the current user
                # Create a new linked list to store the booking history
                insert_node_atend = Linked_list()
                # Insert the booking data into the linked list
                insert_node_atend.insert(data[i])
                # Display the booking history
                insert_node_atend.display()


# Menus
def admin_menu():
    # Display the available options
    print("1. Add Movie Details")
    print("2. Delete Movie Details")
    print("3. Return")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Sub-menu for adding movie details
        print("1. Add Bollywood Movie")
        print("2. Add Hollywood Movie")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Call createMovies function for Bollywood movies
            lst, movie_name = createMovies(bollywoodMovies)
            print("Movie added successfully.\n")

            # Ask if user wants to add movie details
            askfordet = int(input("Do you want to add Movie Details?"))

            if askfordet == 1:
                # Call addition_movie_details for adding details
                addition_movie_details(bollywoodMovies, movie_name)
                input("Press any-key to continue...")
                os.system('CLS')

                # Return to the admin menu
                admin_menu()
            else:
                os.system('CLS')
                admin_menu()
        elif choice == 2:
            # Call createMovies function for Hollywood movies
            lst, movie_name = createMovies(hollywoodMovies)
            print("Movie added successfully.\n")

            # Ask if user wants to add movie details
            askfordet = int(input("Do you want to add Movie Details?"))

            if askfordet == 1:
                # Call addition_movie_details for adding details
                addition_movie_details(hollywoodMovies, movie_name)
                input("Press any-key to continue...")
                os.system('CLS')

                # Return to the admin menu
                admin_menu()
            else:
                os.system('CLS')
                admin_menu()
        else:
            print("Invalid Choice")
            os.system('CLS')

            # Return to the admin menu
            admin_menu()
    elif choice == 2:
        # Sub-menu for deleting movie details
        print("1. Delete Bollywood Movie")
        print("2. Delete Hollywood Movie")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Call deleteMovies function for deleting Bollywood movies
            deleteMovies(bollywoodMovies)
            input("Movie Deleted.")
            os.system('CLS')

            # Return to the admin menu
            admin_menu()
        elif choice == 2:
            # Call deleteMovies function for deleting Hollywood movies
            deleteMovies(hollywoodMovies)
            input("Movie Deleted.")
            os.system('CLS')

            # Return to the admin menu
            admin_menu()
        else:
            print("Invalid Choice")
            os.system('CLS')

            # Return to the admin menu
            admin_menu()
    elif choice == 3:
        os.system('CLS')

        # Return to the main menu
        main_menu()
    else:
        print("Invalid Choice")
        os.system('CLS')

        # Return to the admin menu
        admin_menu()


def user_menu(tempUser):
    # Display the available options
    print("1. Book Movie Ticket")
    print("2. View Booking History")
    print("3. Return")

    # Generate a temporary username for the current user, to be used in the booking data
    tempUserN = (
        tempUser + "_"
        + random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
        + random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    )

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Display available Bollywood movies
        print("Bollywood Movies")
        available_movies = [
            (movie,) for movie, value in bollywoodMovies.items() if value is not None]

        if available_movies:
            print("Recommended Movies:")
            print(tabulate(available_movies, headers=[
                "Movie Title"], tablefmt='psql'))
        else:
            print("No available movies found.")

        # Display available Hollywood movies
        print("Hollywood Movies")
        available_movies = [
            (movie,) for movie, value in hollywoodMovies.items() if value is not None]

        if available_movies:
            print("Recommended Movies:")
            print(tabulate(available_movies, headers=[
                "Movie Title"], tablefmt='psql'))
        else:
            print("No available movies found.")

        # Perform movie selection and ticket booking process
        movie_selection_suggestions()
        namemov = input("Enter the Name of the movie: ")
        theatre_selection(namemov)
        nameth = input("Enter the Name of the theatre: ")
        print_seating_chart()
        seat_selection()
        print_seating_chart()
        temp = {tempUserN: {"Movie Name": namemov, "Theatre Name": nameth,
                            "Time": "9:00 AM", "Seat Number": rlt_final_seats}}
        ticket_print(temp, tempUserN)
        input("\nPress any key to continue...")
        os.system('CLS')

        # Return to the user menu
        user_menu(tempUser)

    elif choice == 2:
        # Display booking history
        print("Booking History")
        booking_history(tempUser)
        input("\nPress any key to continue...")
        os.system('CLS')

        # Return to the user menu
        user_menu(tempUser)

    elif choice == 3:
        os.system('CLS')

        # Return to the main menu
        main_menu()

    else:
        print("Invalid Choice")
        os.system('CLS')

        # Return to the user menu
        user_menu(tempUser)


def main_menu():
    # Display the available options
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Admin option selected, so call admin_menu()
        print("Welcome Admin")
        admin_menu()
    elif choice == 2:
        # User option selected, so call user_menu()
        print("Welcome User")
        user_menu(userN)
    elif choice == 3:
        # Exit the program
        exit()
    else:
        # Handle invalid choice
        print("Invalid Choice")
        os.system('CLS')

        # Return to the main menu
        main_menu()


if __name__ == "__main__":
    # Program starts here
    print("🍿 WELCOME TO CINEMATE 🍿\n")
    start = True
    while start:
        # Display the available options
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        # Get the user's choice
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Option to log in
            login_check()
            os.system('CLS')

            # Call the main menu and set the loop flag to False
            main_menu()
            start = False
        elif choice == 2:
            # Option to create an account
            userN = input("Enter Username: \n")
            str2 = input("Enter Password: \n")
            acc_create(userN, str2)
            os.system('CLS')

            # Call the main menu and set the loop flag to False
            main_menu()
            start = False
        elif choice == 3:
            # Exit the program
            exit()
        else:
            # Handle invalid choice
            print("Invalid Choice")
            os.system('CLS')
