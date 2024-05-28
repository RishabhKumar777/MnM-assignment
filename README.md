# Methods-Mastery-assignment
This readme file can be used to understand how to run the scripts involved

## Setup github project
Open terminal/IntelliJ and clone project  
`git clone git@github.com:RishabhKumar777/methods-mastery-assignment.git`  
Open up project in terminal/IDE
## Create Virtual Environment
The first step is to create a virtual environment

`python -m venv {name of your venv}`  
`source {name of your venv}/bin/activate`

## Install Requirements File
Once you have your virtual environment in place, install all the requirements for the project

`pip install -r requirements.txt`  

## Run the Script processing_data.py Locally
`python data_etl/processing_data.py`  

## Github Actions
Whenever you push code of any kind, github actions will run tests as well as update the docker image to run stuff locally.

## Run Script through Docker container
whenever you push code, a docker image gets built with the name rishabhk777/etl-container:latest 
to run the code and get posts.db (if it already exists in your project, the github action copies it to the docker image too)
`docker run -v $(pwd):/host rishabhk777/etl-container:latest`  
This will get you posts.db locally. Keep in mind, ideally I would want this to upload something to the cloud but for assignment purposes, I am keeping it local  

## Testing Creation and Insertion of Records into sqlite database
posts.db is currently having all the rows already inserted. IF you want to test out that functionality through docker, first delete the file locally and then dockerize the container with a push to the branch. Logs will provide you with enough details to understand what is being loaded as new/old records.
