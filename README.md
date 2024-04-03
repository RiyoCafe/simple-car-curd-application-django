
## CRUD Application with Django and PostgreSQL

This repository contains a simple CRUD (Create, Read, Update, Delete) application built using Python Django framework, with PostgreSQL as the database backend. The application provides endpoints that can be accessed via HTTP requests, demonstrated using Postman.

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

- **Create**: `POST /api/cars/`
- **Read**: `GET /api/cars/` (Retrieve all resources)
- **Read**: `GET /api/cars/?id={}/` (Retrieve a specific resource)
- **Update**: `PATCH /api/cars/?id={}/` (Update a resource)
- **Delete**: `DELETE /api/cars/?id={}/` (Delete a resource)


