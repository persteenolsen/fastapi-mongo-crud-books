# Python + FastAPI + MongoDB at Atlas

An API handles Books, Addresses and Users

Last updated:

- 30-04-2025

Python Version local:

- 3.12.1

Python Version at Vercel:

- 3.12

# Get startet

Clone the repository

```
Create a virtual environment

```
python -m venv <name_of_venv>

```

Go to the virtual environment's directory and activate it

For Windows:

```
Scripts/activate

```

Install the requirements

```
pip3 install -r requirements.txt

```

Swagger documentation

FastAPI provides the Swagger documentation of the API where you can perform CRUD operations

To access the documentation, we must run uvicorn

```
uvicorn main:app --reload

```

If everything works fine, the message “Project connected to the MongoDB database!” will show

The FastAPI and Swagger documentation is now available at 

`http://127.0.0.1:8000/docs`

You can go to the MongoDB at Atlas to test your data

Happy use of FastAPI :-)

