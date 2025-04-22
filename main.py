from fastapi import FastAPI
import uvicorn
#from dotenv import dotenv_values
import os
import os.path
from dotenv import load_dotenv
from pymongo import MongoClient
from routes.api import router as api_router
#config = dotenv_values(".env")

app = FastAPI()


load_dotenv()

ATLAS_URI = os.getenv('ATLAS_URI')

DB_NAME = os.getenv('DB_NAME')


app.mongodb_client = MongoClient(ATLAS_URI)
app.database = app.mongodb_client.get_database(DB_NAME)

print("Project connected to the MongoDB database!")

#@app.on_event("shutdown")
#def shutdown_db_client():
#    app.mongodb_client.close()

app.include_router(api_router)

if __name__ == '__main__': #this indicates that this a script to be run
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info", reload = True)
