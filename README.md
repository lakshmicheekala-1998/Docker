RESTful Web Service-using-docker- Python + Flask
This repository is on RESTful service using Docker, Python and Flask. For the front end I have used HTML which display data from Json.

Files Included Python Application(app.py), DockerFile, and HTML File About the application So this is a Python application with a hardcode Json data (foods.json) and it consists of 4 GET API menthods.

The application end points used are
/foodList/ : Gets list of the menu.
/foodList/string:Calories/' : Gets list of menu with a particular Calories.
/foodList/string:Calories/string:Protein/ : Gets list of menu with a particular Calories and Protien.
/foodList/string:Calories/string:Protein/string:Carbs : Gets list of menu with a particular Calories, Protien and Carbs.

We then create a Docker file and build and run it to create a Docker Container which will fetch us the above data.

Steps to follow Unzip the file. Go to root of that folder and then run that path in cmd once the cmd opens, then run the below command

pip install flask
pip install flask-restful
Once these two dependencies are installed then in that we write the command to build and run Docker container

Build the image using command: docker build -t flaskapp .

Run the Docker container using the command: docker run -d -p 5000:5000 flaskapp

We have used 5000 as Python works on this default port.
