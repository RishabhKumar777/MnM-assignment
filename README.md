# Methods-Mastery-assignment
This readme file can be used to understand how to run the scripts involved. The artifacts of the assignment are already in the project
1. Python scripts (data_etl folder as well as test folder)
2. SQLite database named posts.db (currently this database already has data in it)
3. README.md file which you are currently reading
4. Dockerfile (Bear in mind, Github actions already creates/updates this docker image for you which is rishabhk777/etl-container:latest)

## Setup github project
Open terminal/IntelliJ and clone project  
`git clone git@github.com:RishabhKumar777/methods-mastery-assignment.git`  
Open up project in terminal/IDE
## Create Virtual Environment [not necessary but you need to install requirements.txt]
The first step is to create a virtual environment

`python -m venv {name of your venv}`  
`source {name of your venv}/bin/activate`

## Install Requirements File
Once you have your virtual environment in place, install all the requirements for the project

`pip install -r requirements.txt`  

## Run the Script processing_data.py Locally
`python data_etl/processing_data.py`  

## Github Actions [Testing ETL test cases as well as dockerizing]
Whenever you push code of any kind, github actions will run tests as well as update the docker image to run stuff locally with the docker image. NO MANUAL INTERVENTION REQUIRED HERE TO CREATE THE DOCKER IMAGE. Benefit of this is that the docker image remains updated with your latest code pushed to your master/main branch. Code on other branches for now will have to be manually dockerized by using the Dockerfile in the project. THIS IS ALSO RUNNING THE TEST CASES FOR ALL THE CLASSES.

## Run Script through Docker container
whenever you push code, a docker image gets built with the name rishabhk777/etl-container:latest 
to run the code and get posts.db (if it already exists in your project, the github action copies it to the docker image too)
`docker run -v $(pwd):/host rishabhk777/etl-container:latest`  
This will get you posts.db locally. Keep in mind, ideally I would want this to upload something to the cloud but for assignment purposes, I am keeping it local  

## Testing Creation and Insertion of Records into sqlite database
posts.db in the project is currently having all the rows already inserted. IF you want to test out that functionality through docker, first delete the file locally and then dockerize the container with a push to the branch/ running the above steps. Logs will provide you with enough details to understand what is being loaded as new/old records.
