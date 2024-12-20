# REST API for the Russian Federation of Sports Tourism 
### Overview

This repository contains the backend for a mobile application designed to simplify the process of submitting data about mountain passes for the Russian Federation of Sports Tourism.
The application allows users to submit detailed information about their hiking experiences, which is then verified and stored by FSTR moderators.

### Key Features

Data Submission: Users can submit detailed information about mountain passes, including coordinates, difficulty ratings, and photos.
Data Verification: FSTR moderators can review and approve submitted data.
Data Access: Users can view their submitted data and search for information about other passes.
RESTful API: A well-structured REST API handles all data interactions.

### Technologies Used
Python3<br>
Django<br>
Django Rest Framework<br>
Json<br>


### API Endpoints

GET /submitData/: Retrieves a list of all submitted mountain passes.<br>
POST /submitData/: Submits data for a new mountain pass.<br>
GET /submitData/{id}: Retrieves details about a specific mountain pass.<br>
PATCH /submitData/{id}: Updates an existing mountain pass (if status is "new").<br>
GET /api/submitData/user__email=<str:email>: Retrieves all submissions for a specific user.<br>

### Data Structure

A typical JSON payload for a mountain pass submission:

```json
JSON

{
    "id": 1,
    "user_id": {
        "id": 1,
        "email": "user1@gmail.com",
        // ...
    },
    "coords_id": {
        "id": 1,
        "latitude": "23.23423400",
        // ...
    },
    // ... other fields
}
