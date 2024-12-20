# Swagger Documentation for Russian Federation of Sports Tourism API
### Info:

**Title:** Russian Federation of Sports Tourism API
**Version:** 1.0
**Swagger:** Swagger file is available

openapi.json
### Description:

This API provides functionalities for managing mountain pass data for the Russian Federation of Sports Tourism. Users can submit information about their hiking experiences, moderators can review and approve submissions, and users can access their data or search for other passes.

### Paths:

1. /submitData (GET)

Summary: Retrieves a list of all submitted mountain passes.
Description: Returns a paginated list of submitted mountain passes. Moderation status and other details are included.
Responses:
200 (OK): A JSON array containing mountain pass objects.
401 (Unauthorized): If the request is not authorized.
2. /submitData (POST)

Summary: Submits data for a new mountain pass.
Description: Creates a new mountain pass entry with the provided information. User authentication is required.
Request Body:
Required:
application/json: A JSON object representing the new mountain pass data. Refer to the Models section for details.
Responses:
201 (Created): The newly created mountain pass object with its generated ID.
400 (Bad Request): Invalid data provided.
401 (Unauthorized): If the request is not authorized.
3. /submitData/{id} (GET)

Summary: Retrieves details about a specific mountain pass.
Description: Returns a single mountain pass object based on the provided ID.
Parameters:
Path Parameter:
id (integer): The unique identifier of the mountain pass.
Responses:
200 (OK): The requested mountain pass object with all details.
404 (Not Found): The mountain pass with the specified ID does not exist.
4. /submitData/{id} (PATCH)

Summary: Updates an existing mountain pass (if status is "new").
Description: Allows updating specific fields of a mountain pass entry, only if its status is "new". User authentication and authorization are required.
Parameters:
Path Parameter:
id (integer): The unique identifier of the mountain pass.
Request Body:
Required:
application/json: A JSON object containing only the fields that need to be updated.
Responses:
200 (OK): The updated mountain pass object with its new details.
400 (Bad Request): Invalid data provided or attempt to update a non-new status pass.
401 (Unauthorized): If the request is not authorized.
404 (Not Found): The mountain pass with the specified ID does not exist.
5. /api/submitData/user__email=<str:email> (GET)

Summary: Retrieves all submissions for a specific user.
Description: Returns a list of mountain passes submitted by a user identified by their email address. User authentication is required.
Parameters:
Path Parameter:
email (string): The email address of the user whose submissions you want to retrieve.
### Responses:
200 (OK): A JSON array containing mountain pass objects submitted by the user.
401 (Unauthorized): If the request is not authorized.
404 (Not Found): The user with the specified email address does not have any submissions.


