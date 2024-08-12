# ToDo List Application

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

The ToDo List Application is a Python-based project developed using Django and Django REST Framework. It provides a backend for managing tasks, including functionalities for creating, editing, deleting, and marking tasks as completed. Authentication is handled through Django REST Framework, and the application uses SQLite3 for data storage.

## Features

- **Authentication**: Secure user authentication using Django REST Framework.
- **Add Tasks**: Users can add new tasks.
- **Edit Tasks**: Tasks can be edited.
- **Delete Tasks**: Tasks can be deleted.
- **Mark Tasks as Completed**: Users can mark tasks as completed.
- **Data Persistence**: Tasks are saved in an SQLite3 database, ensuring data persists across sessions.

## Technologies

- **Python**: Programming language.
- **Django**: Web framework for building the application.
- **Django REST Framework**: For authentication and API endpoints.
- **SQLite3**: Database for data storage.
- **HTML/CSS**: For the frontend, if applicable.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mayis999/todo.git
    ```
2. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Start the server** by running the `manage.py` script.
2. **Access the application** through your web browser at `http://localhost:8000` (or the URL provided by your application).
3. **Use the API endpoints** for managing tasks. Authentication is required to access certain endpoints.
