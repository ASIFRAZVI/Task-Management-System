# Introduction
Welcome to the project documentation for our task management API built using Django and Django REST Framework. This API provides a robust backend solution for user authentication, task management, and various user interactions. The goal of this project is to create an efficient and user-friendly platform that allows users to register, log in, manage their tasks, and perform various operations seamlessly.

# Getting Started:

1. git clone https://github.com/ASIFRAZVI/Task-Management-System.git
2. Software dependencies : Django, Python, Django REST framework, PostgreSQL, Swager.
3. Latest releases : v1
4. API references : http://{host}:{port}/v1/api/schema/swagger-ui/

#setup environment:
create .env file and take reference from example.env

# Build and Test
1. cmd: python -m venv venv 
2. cmd: source venv/bin/activate
3. cmd: pip install -r requirements.txt
4. cmd: python manage.py migrate
5. cmd: start.bat

#API guide

# API endpoints
1.  register user

- Endpoint : POST /v1/api/auth/signup/
request body
{
  "name": "string",
  "email": "user@example.com",
  "password": "string",
  "phone_number": 9353580260,
}

response:
 ohoo! user registered! code: 201

error :
400 bad request and error message

2. login user
the login endpoint responsible for log in user by comparing hashed password and generation and storing jwt aceess, refresh token in cookies.

- enpoint: POST /v1/api/auth/signin/

body:
{
    "email": "user@example.com",
    "password": "string"
}

response:
200 ok and access and refresh token in cookies.

error:
400 bad request and error message
400 user not activated

3. logout User

this endpoint will log out user by removing access and refresh token from cookies.

- endpoint: POST /v1/api/auth/signout/

response:
200 user logged out

error:
400 bad request and error message

4. resend otp to mail
this endpoint will resend otp to user's registered mail.

endpoint : POST v1/api/auth/resend-otp/

body:
{
    "email": "user@example.com"
}

response:
200 otp resent to mail

error:
400 bad request and error message

5. verify otp

this endpoint will verify otp sent to user's registered mail and mark user as active user .

- endpoint : POST v1/api/auth/verify-otp/

validity : 10 mins
body:
{
    "email": "user@example.com"
    "otp": 253427
}

response:
200 User verified

error:
400 bad request and error message

6. add Tasks
this end point responsible for creation user's task.

endpoint : POST /v1/api/task-mgmt/task/

body:
{
  "title": "string",
  "description": "string",
 
}

response:
201 task created

error:
400 bad request and error message

7. get all task

this end point responsible for getting all user's expenses.

endpoint : GET /v1/api/task-mgmt/task/

response:
200 list of all task

error:
400 error and error message

8. get task by id

this end point responsible for getting user's task by task uuid.

endpoint : GET /v1/api/task_mgmt/task/{task-uuid}/

response:
200 task by id obj

error:
400 error message

9. update task

this end point responsible for updating user's task by task uuid.

endpoint : PATCH /v1/api/task-mgmt/task/{task-uuid}/

body:
{
  "title": "string",
  "description": "updated task",
  
}

response:
200 task updated

error:
400 error message

10. delete task

this end point responsible for deleting user's task by task uuid.

endpoint : DELETE /v1/api/task-mgmt/task/{task-uuid}/

response:
204 task deleted

error:
400 error message


# Future Improvements (need to be implemented)
1. Add pagination to get all tasks and other endpoints.
2. Implement rate limiting to prevent abuse. (Throttling)
3. Implement password reset and forgot password feature.
4. caching techniques to improve performance.
5. query optimization for better performance.

Portfolio- https://asifrazvi.netlify.app/
resume- https://drive.google.com/file/d/1bKf1jR58ANq0sxqUJtWhxvbiKT9kF4G7/view?usp=drive_link

email- masifraza.asif@gmail.com
ph- 9353580260

Thankyou!

