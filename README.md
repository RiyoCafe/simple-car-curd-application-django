
## CRUD Application with Django and PostgreSQL

This repository contains a simple CRUD (Create, Read, Update, Delete) application built using Python Django framework, with PostgreSQL as the database backend. The application provides endpoints that can be accessed via HTTP requests, demonstrated using Postman.
I have taken help from [PythonHacks](https://github.com/RekhuGopal/PythonHacks/tree/main/Django_REST_API) and [CURD app build](https://betterstack.com/community/guides/scaling-python/django-postgresql/)repository for developing this project.
### Features:

- CRUD functionality implemented for managing data.
- Utilizes PostgreSQL as the database for data storage.
- API endpoints tested using Postman.

### Getting Started:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RiyoCafe/simple-car-curd-application-django.git
   ```

2. **Set Up PostgreSQL Database**:
   - Create a PostgreSQL database.
   - Update the database settings in `settings.py` with your database credentials.

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access API Endpoints**:
   - Use Postman or any HTTP client to interact with the API endpoints.

### API Endpoints:

- **Create**: `POST /api/cars/add/`
- **Read**: `GET /api/cars/` (Retrieve all resources)
- **Read**: `GET /api/cars/{id}/` (Retrieve a specific resource)
- **Update**: `PATCH /api/cars/update/{id}/` (Update a resource)
- **Delete**: `DELETE /api/cars/delete/{id}/` (Delete a resource)


