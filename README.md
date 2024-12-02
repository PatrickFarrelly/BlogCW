# Blog Application

An application built with Django. This application enables users to register for an account, login and once logged in, authenticated users may create and edit blogs as well as comment on them.

---

## Features

- **User Authentication**: Login, logout, and register functionality.
- **Blog Management**: Create, update, delete, and view blogs.
- **Commenting System**: Authenticated users can add comments to blogs.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **pip**: Python's package manager (typically bundled with Python).
- **Pillow**: Python Imaging Library for handling image uploads (installed automatically via `requirements.txt`).

---

## Installation

Follow the steps below to set up the project locally.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Blogs
```

### Step 3: Set Up a Virtual Environment

```bash
python -m venv myenv
```
On Windows:

```bash
myenv\Scripts\activate
```
On macOS/Linux:

```bash
source myenv/bin/activate
```
### Step 4: Install and Upgrade pip

```bash
python -m pip install --upgrade pip
```
### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```
### Step 6: Apply Database Migrations

```bash
python manage.py migrate
```
### Step 7: Create a Superuser
Create a superuser to access the Django admin panel (this is optional)

```bash
python manage.py createsuperuser
```

### Step 8: Run the Development Server

```bash
python manage.py runserver
```
Visit the app in your browser at http://127.0.0.1:8000/.

### Project Structure
Below is an overview of the project structure:

```plaintext 
BlogCW/
├── Blogs/
│   ├── Blog/
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   ├── blogs/
│   │   │   │   ├── base.html
│   │   │   │   ├── blogs.html
│   │   │   │   ├── confirm_delete.html
│   │   │   │   ├── create_blog.html
│   │   │   │   ├── login.html
│   │   │   │   ├── logout.html
│   │   │   │   ├── register.html
│   │   │   │   ├── update_blog.html
│   │   │   │   └── view_blog.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

### License
This project is licensed under the MIT License.