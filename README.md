# Spy Cat Agency - Django Project

## Overview
This is a Django-based web application for managing spy cats, missions, and targets for the Spy Cat Agency. It includes functionality to add, update, and delete cats, missions, and targets, with validation for the cats' breed, salary, name.

## Technologies Used
- Django 5.1.3
- SQLite (default db)
- Python 3.11.3
- Django REST Framework 
- requests
- VS Code 

## Setup Instructions

### Prerequisites
- Python 3.*
- pip
- Virtual environment (optional)

### 1. Clone the repository

```bash
git clone https://github.com/GilGirusanda/SpyCatAgency.git
```
Go to the repo directory

### 2. Set up a virtual env (optional)

```bash
python3 -m venv env
source env/bin/activate
```
\*On Windows use
```bash
env\Scripts\activate

(activate.bat if CMD, and activate.ps1 if PowerShell)
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply db migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)
Just set `admin` both for name and password, ignore email, and confirm weak password by entering `y`.
```bash
python manage.py createsuperuser
```

### 6. Run the dev server
Port is 8000. You can change port in `uri` variable of Postman's collection.
```bash
python manage.py runserver 8000
```

# API Endpoints
The following API endpoints are available for interacting with the SCA system:

## Cats

- POST /cats/: create a new spy cat.

- GET /cats/: list all spy cats.

- GET /cats/{id}/: get details of a specific cat.

- PUT /cats/{id}/: update a specific cat.

- DELETE /cats/{id}/: remove a cat from the system.

## Missions

- POST /missions/: Create a new mission with associated targets by a single request. (BOTH with cat OR no cat)

- GET /missions/: List all missions.

- GET /missions/{id}/: retrieve details of a specific mission.

- POST /missions/{id}/assign_cat/: couple cat with a mission (if cat has no missions and if the mission's not already been assigned to the other cat)

- DELETE /missions/{id}/: delete a mission (only if not assigned to a cat).

## Targets

- PATCH /targets/{id}/complete/: Mark a target as completed.

- PATCH /cat/api/targets/{id}/update-notes/: Update target notes.

---
# Postman access

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/37632251-48112f17-59fd-48cc-925c-6cf16087e23d?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D37632251-48112f17-59fd-48cc-925c-6cf16087e23d%26entityType%3Dcollection%26workspaceId%3D988009fd-3ead-457d-b56a-478adbd77641)