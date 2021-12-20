# TSAbaggagedetection
This is a TSA baggage detection project using tensorflow

The required dependecies of the project are mentioned in **[requirements.txt]** file. The python version of choice was Python 3.6

The Project aims to build a machine learning algorithm to detect dangerous objects in baggages in TSA atmosphere.

Tensorflow and Django are the main frameworks used for this project.

The project model is zipped as a file called saved_model.zip. This zip file has to be unpacked and deployed in the root directory.

To deploy the app, we need to type in few commands.

1. Go to the root folder and type in the command "python manage.py runserver". This will boot up the server.

Remember, the database used for this project is Mysql. The username and password configurations can be changed from setting.py file in "TSAbaggagedetection/luggageproject/"

2. Next execute "python manage.py migrate" to create the database structure.

The app is designed to work on port number 8000. If there is any change needed, then it could be modified in settings.py file. 

Once the port number is changed, remember to change the port number in the .html file in "TSAbaggagedetection/myapp/templates/index.html"

The root working URL of the app is http://localhost:8000/index
