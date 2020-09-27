
Download Flask to run this program
Download Python to run this program
Download Tweepy to run this program
Use Flask to create app see https://flask.palletsprojects.com/en/0.12.x/quickstart/ for more information. 

use static files along wtih HTML templates to create a front end that will generate new data.
https://flask.palletsprojects.com/en/0.12.x/quickstart/#static-files

Create Developer account for Twitter api
https://developer.twitter.com/en/docs

Set up Twitter API with Tweepy and search for Tweets, User, and Date
https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

Create a git repository
Create a .gitignore file.
Create a project1.env to store all of the secret keys and keys used for the twitter API. 
Put that file in the .gitignore file. 
Before running the program, make sure to source the project1.env. If this is not done, it will not work. 

Techinical Issues:
One of the issues that I was having was how to display new information when you refreshed the app. Was a simple solution to include the python code in the def index(). I figured out how to do it by looking up the flask API.

Another Techinal issue was how to send all of the data needed to populate the each of the fields. I created a class, and then inserted all of the individual items into the class. When I pick an item to display by random, the list of all of the items, one is picked. Then I send the data of that in a dynamic way so it can handle different ones. I think using JSON would have been more efficient, and will convert it to that, but this was an easy example. 

Known issues of the app is that the tweets are just looking for the word, but I really should make sure that the tweet relates to the foot item. 
An other known issue is that the recipies are hard coded, and adding a new recipe is a tedious processes, so I am going to look to see if there is an easier way to accomplish that. 
