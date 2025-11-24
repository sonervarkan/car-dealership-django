# Car Dealership Django Project

A full-stack car listing and filtering platform built with Django, MySQL, Cloudinary, Bootstrap, and jQuery/AJAX.
Users can register, log in, add cars, upload images to Cloudinary, and filter vehicles dynamically using multiple criteria.

## Features
### Authentication

User Registration & Login (Django Auth)

Login-required access for adding cars

Automatic redirect after login/logout

### Car Management

Add cars with:

Brand

Model

Gear Type

Fuel Type

Color

Year

Price

Image upload (stored on Cloudinary)

### Advanced Car Filtering (AJAX)

Filter by:

Brand

Model

Gear Type

Fuel Type

Year

AJAX endpoints dynamically update dropdown lists

Filtered results displayed with images

### Image Slider on Homepage

Auto-playing slider showing cars and their images

Next image → next car looping animation

### Cloudinary Integration

All uploaded images stored using Cloudinary Storage

Fully integrated with Django’s default file storage system

### UI / Styling

Mobile-friendly Bootstrap layout

Custom navbar & form styling

## Tech Stack
````
Layer	Technologies
Backend	Django 5, Python
Frontend	Bootstrap 5, HTML, CSS, jQuery
Database	MySQL
Media Storage	Cloudinary (cloudinary & cloudinary_storage)
Authentication	Django Auth System
````
## Project Structure
````
car_dealership_django/
│
├── car_dealership_django/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── car_dealership_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   ├── admin.py
│   ├── migrations/
│   ├── static/
│   │   └── car_dealership_app/
│   │       ├── css/
│   │       │   ├── filter.css
│   │       │   ├── main.css
│   │       │   ├── navbar.css
│   │       │   └── slider.css
│   │       └── script/
│   │           ├── filter.js
│   │           ├── script.js
│   │           └── slider.js
│   │
│   ├── templates/
│   │   └── car_dealership_app/
│   │       ├── index.html
│   │       ├── base.html
│   │       ├── add-car.html
│   │       ├── filter-results.html
│   │       └── registration/
│   │           ├── login.html
│   │           └── register.html
│
├── manage.py
└── requirements.txt  (opsiyonel)

````
## Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-repo/car-dealership-django.git
cd car-dealership-django

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install required packages
pip install -r requirements.txt

4️⃣ Configure your MySQL database

Create a database:

CREATE DATABASE car_dealership_django;


Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'car_dealership_django',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

5️⃣ Add Cloudinary credentials

In settings.py:

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your-cloud-name',
    'API_KEY': 'your-api-key',
    'API_SECRET': 'your-api-secret'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

6️⃣ Run migrations
python manage.py migrate

7️⃣ Create an admin user
python manage.py createsuperuser

8️⃣ Start the server
python manage.py runserver

## Important URLs
````
URL	Description
/	Homepage (Slider + Filter System)
/add-car/	Add car (requires login)
/register/	User registration
/login/	User login
/logout/	Logout
/admin/	Django Admin Panel
````
## API Endpoints (AJAX)
````
Endpoint	Purpose
/get_models_by_brand/	Fetch models by brand
/get_gear_type_by_model_brand/	Fetch gear types
/get_fuel_type_by_brand_model_gear_type/	Fetch fuel types
/get_filter_results/	Return filtered cars
````
## Image Upload (Cloudinary)

Car images are uploaded using:

img_url = models.ImageField(upload_to='')


And served via:

{{ img.img_url.url }}

## Slider Logic (static/car_dealership_app/script/slider.js)

Cycles through cars & images every 1.5 seconds

Updates:

Brand

Model

Year

Image

## Future Improvements

Pagination for car listings

User profile page

Multiple image upload

Admin-level car management

API endpoints (Django REST Framework)

## License

This project currently has no license.

