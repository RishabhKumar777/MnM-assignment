# methods-mastery-assignment
This readme file can be used to understand how to run the scripts involved

## setup github project
Open terminal/IntelliJ and clone project  
`git clone git@github.com:RishabhKumar777/methods-mastery-assignment.git`  
Open up project in terminal/IDE
## create virtual environment
The first step is to create a virtual environment

`python -m venv {name of your venv}`  
`source {name of your venv}/bin/activate`

## install requirements file
Once you have your virtual environment in place, install all the requirements for the project

`pip install -r requirements.txt`  

## run the script processing_data.py locally
`python data_etl/processing_data.py`  

## run script through Docker container
whenever you push code, a docker image gets built with the name rishabhk777/etl-container:latest 
to run the code and get posts.db
`docker run -v $(pwd):/host rishabhk777/etl-container:latest`  
This will get you posts.db locally. Keep in mind, ideally I would want this to upload something to the cloud but for assignment purposes, I am keeping it local
