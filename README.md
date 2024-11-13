# Django Invoice API


This project provides a simple Invoice API implemented using Django and Django REST Framework. It supports basic CRUD operations for invoices.

## Setup Instructions

Follow these steps to set up and run the project on your local machine:

### Prerequisites


- Python 3.x
- pip (Python package installer)
- Virtual Environment (optional but recommended)


## Installation

1. Clone the repository:

bash
  https://github.com/devanshptl/DDA.git



2. Create a virtual environment (optional but recommended):
bash
 python -m venv venv
 

3. Activate the virtual environment:
  * On Windows:
  bash
  venv\Scripts\activate
  

* On macOS and Linux:
bash
source venv/bin/activate


4. Install dependencies:
bash
pip install -r requirements.txt


5. Navigate to the project directory:

bash
cd project



6. Apply migrations:
bash
python manage.py migrate


7. Run the development server:
bash
python manage.py runserver

8. Access the API
You can now access the API endpoints:

- Invoices List: http://127.0.0.1:8000/api/invoices/
- Admin Interface: http://127.0.0.1:8000/admin/ (Use the superuser credentials to log in)


   
## Assumptions Made During Implementation

### Database Assumptions:

- The project assumes that you are using a default SQLite database, which is set up out of the box. If you wish to use a different database (e.g., PostgreSQL or MySQL), you will need to configure it in settings.py and update the DATABASES setting accordingly.

### Django REST Framework:

- It is assumed that Django REST Framework (DRF) is installed and configured correctly for handling API views and routing. If it's not installed, you can install it by running:

bash
pip install djangorestframework


### API Functionality:

- The API uses a simple InvoiceViewSet to handle CRUD operations for invoices. This assumes that the necessary fields for an invoice (e.g., invoice number, date, amount) are defined in the Invoice model.

### Admin Interface:

- The project assumes the use of the Django Admin interface for managing invoices. The models are registered in the admin interface to enable the creation and management of invoices through the Django admin panel.

### No Authentication/Authorization:

- The project does not include authentication or authorization mechanisms by default. You can add token authentication or other methods depending on your project requirements.

### Version Compatibility:

- This project assumes that you are using Python 3.6 or above. If you are using a different version of Python, make sure the necessary adjustments are made.
