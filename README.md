# Cinemate: A Movie Booking App

Cinemate is a Python-based movie booking application built using the Tkinter library. It simplifies the process of booking and managing movie tickets, providing a user-friendly interface for both customers and administrators. This README file provides an overview of the project and descriptions of the key files used in Cinemate.

## Project Description

Cinemate is designed to streamline the movie booking experience by offering the following features:

- **User-friendly interface**: Cinemate provides an intuitive interface that allows users to browse available movies, select showtimes, and book tickets effortlessly.

- **User registration and authentication**: Users can create accounts, log in, and securely manage their booking history.

- **Movie catalog**: The application offers a catalog of available movies, including details such as the movie's title, description, showtimes, and pricing.

- **Booking and payment**: Users can select their preferred showtimes, choose seats, and make _mock_ secure online payments for their tickets.

- **Admin panel**: Administrators have access to an admin panel that allows them to add, edit, or remove movies and showtimes. They can also view and manage user booking records.

## File Descriptions

### 1. `mainTK.py`

This file is the main entry point of the Cinemate application. It is responsible for launching the application and handling user interactions. The `mainTK.py` file creates the graphical user interface (GUI) using the Tkinter library and connects the application to the backend logic implemented in `main.py`.

### 2. `Project.py`

The `Project.py` file contains the backend logic for Cinemate. It manages user accounts, movie data, and booking functionality. This file communicates with the GUI created in `mainTK.py` and ensures the application's core functionality.

### 3. `userdata.json`

`userdata.json` is a JSON file that stores user account information, including usernames, passwords, and booking history. User data is loaded and saved from/to this file to maintain user accounts across sessions.

### 4. `browse.json`

`browse.json` is a JSON file used to store information about available movies, showtimes, and pricing. It acts as the database for movie-related data and is used to populate the movie catalog in the application.

## Getting Started

To run Cinemate on your local machine, follow these steps:

1. Ensure you have Python 3.11 installed on your system.

2. Clone or download the Cinemate project repository.

3. Install the required Python libraries by running the following command:

   ```bash
   pip install tk
   ```

4. Navigate to `Project.py` and change `pathUserData` and `pathBrowseData`, according to your directories.

5. Navigate to `mainTK.py` and change `ASSETS_PATH`, according to your directories. 

6. Run the `mainTK.py` file to start the Cinemate application:

   ```bash
   python mainTK.py
   ```

7. Explore and enjoy Cinemate!

## Contributing

If you'd like to contribute to the Cinemate project, please open an issue or create a pull request on the GitHub repository. We welcome contributions, bug fixes, and feature enhancements from the community.

## License

Cinemate is open-source under [MIT Liscense]. Feel free to use and modify the code according to the terms of the license.

## Contact

For questions or inquiries about Cinemate, you can contact us at [Srajan](mailto:srajansolanki04@gmail.com), [Varun](mailto:varunpatani2004356@gmail.com), [Priyanshi](mailto:priyanshifuriya@gmail.com).

We hope you enjoy using Cinemate to book your favorite movies with ease. Happy movie-watching! 🎥🍿
