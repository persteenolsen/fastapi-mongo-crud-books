# Python + FastAPI + MongoDB at Atlas

An API that handles Books, Addresses and Users

Last updated:

- 08-08-2025

Python Version local:

- 3.12.1

Python Version at Vercel:

- 3.12

# Get startet

- Clone the repository from my GitHub 

- Create a virtual environment by Powershell or VS Code:

"python -m venv <name_of_venv>"

- Go to the virtual environment's directory and activate it:

"Scripts/activate"

- Install the requirements:

"pip3 install -r requirements.txt"

# Swagger documentation / Testing the API

FastAPI provides the Swagger documentation of the API where you can perform CRUD operations

To access the documentation, we must run uvicorn:

"uvicorn main:app --reload"

If everything works fine, the message “Project connected to the MongoDB database!” will show the FastAPI and Swagger documentation is now available at: 

`http://127.0.0.1:8000/docs`

- Use the Swagger for Create a Document in the MongoDB and try to perform other CRUD operations

- You can go to the MongoDB at Atlas to test your data in the DB / Collections / Documents

When you make a change to the models and start run the Web App the MongoDB should be updated

# Deployment to Vercel

- Take a look at the file "vercel.json"

- Create a Project at Vercel from your repository at GitHub with the code of this FastAPI

- Create the envirement variables from .env at Vercel with the connection to MongoDB at Atlas

- Make a commit to your GitHub

- Go to Vercel and check that the build and deployment happened and your site is in Production

Happy use of FastAPI :-)

