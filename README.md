# Fulthrottle Python / Django task

This is guide or documentation for application which describes about users and their activites. users have multipe activites with range from start time to end time recorded. Those are listed in api under members. Also there are commands used in command line interface which populates data from databases.  

This application is hosted in heroku with public repo github.

server supports only api 

Github repository : https://github.com/j7sai/fulthrottletask.git

# Custom management commands
  -> Two commands are for activities.
  
  -> To get specific user activities , we must pass argument 'id'.
  
     python manage.py get_user_activities 13
   
  -> To get all users activites, no arguments required.
  
     python mange.py get_user_activites
    
# REST API for user and activites
  -> This endpoint serves json format data, users with fields name, timezone and their activities. Activity periods is an another model        has relation with user with fields start time and end time.
  
     endpoint:   https://useractivites.herokuapp.com/useractivites/
