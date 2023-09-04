# Health Knowledge Base 💊

## Description

This is a Django-based web application that serves as a health catalog for medications and diseases. Users can browse the list of medications and diseases, see detailed information for each, and search using filters.

## Features

- List medications
- Medication details, including diseases it can treat
- List diseases
- Disease details, including medications for treatment
- Search medications and diseases using `django-filters`
- Pagination for easier navigation

## Technologies Used

- Python 3.x
- Django 3.x
- SQLite (default Django database)
- django-filters for search capabilities

## Installation

### Prerequisites

- Python 3.x
- Pip
- Virtualenv (optional but recommended)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/kaluzhskaia/knowledge_base.git
    ```

2. Navigate to the project directory:
    ```bash
    cd knowledge_base
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        .\\venv\\Scripts\\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the migrations:
    ```bash
    python manage.py migrate
    ```

6. Load the data into the database:
    ```bash
    python manage.py load_health_data your_json_file.json
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

    The application should be available at `http://127.0.0.1:8000/`.

## Usage

- Navigate to `/medications/` to view a list of medications. You can use the search bar to filter the medications based on their name or description.
- Navigate to `/diseases/` to view a list of diseases. Use the search bar to filter the diseases by name.
- Pagination controls are available at the top and the bottom of medication and disease lists.

## Screenshots



<img width="1419" alt="image" src="https://github.com/Kaluzhskaia/knowledge_base/assets/16777799/0724b0d8-e3e1-4522-9f2a-52e3043b85be">
<img width="926" alt="image" src="https://github.com/Kaluzhskaia/knowledge_base/assets/16777799/b10ab6c6-e01a-4ee9-b5e4-cf2c475b0a01">



