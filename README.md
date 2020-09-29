
Link to Heroku Deployment
https://limitless-taiga-54667.herokuapp.com/


Download Flask to run this program
Download Python to run this program
Download Tweepy to run this program 

Use Flask to create app see https://flask.palletsprojects.com/en/0.12.x/quickstart/ for more information.

use static files along with HTML templates to create a front end that will generate new data. https://flask.palletsprojects.com/en/0.12.x/quickstart/#static-files

Create Developer account for Twitter api https://developer.twitter.com/en/docs

Set up Twitter API with Tweepy and search for Tweets, User, and Date https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/

Create a git repository Create a .gitignore file. Create a project1.env to store all of the secret keys and keys used for the twitter API. Put that file in the .gitignore file. Before running the program, make sure to source the project1.env. If this is not done, it will not work.

Create a Spoonacular api account. 

Use the Spoonacular api account to access the recipes. API notes for the spoonacular can be found here: https://spoonacular.com/food-api

Populate the static api files with information gathered from the spoonacular API along with the Twitter API calls. 

Create form in HTML to gather information to search for recipes. Use the Flask API to determine if the next api calls are for user input, or not:
https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

Create new template html page to act as a fail safe incase the user did not enter a valid recipe name, or if there are no recipes that match what the user asked. 

Create Heroku account: https://signup.heroku.com
Create requirements.txt file in the root folder of your project, where the python file is. List all the dependencies that are used in the app.
Create Procfile file that stores the command line that runs the program. This one is 
web: python project1.py

create a new heroku app and push this to it. 

Go to heroku and add the secret keys/ vars into it. https://devcenter.heroku.com/articles/config-vars

acknowledgement: 
Issue one: figure out a way to make sure that the Tweet always relates to the item of the recipe and not just random stuff. The way I went around it is look for the title first, then the string, and if the user entered it then what the user entered. However, if that all fails, it picks a new recipe along with a new tweet. This is not efficient at all, I would like to make it more efficient. I would also like to change the fail safe error page to make it do more than just state you messed up please try again. 
Issue 2: I would like to have gone to more of the more advanced edge cases, but didn't get to it. The API calls for searching individual items or recipies that contain it was in the API docs and I could have added it in fairly easily. I do find it difficult to actually think how if you start typing one thing something else would show up.
Issue 3: not using json to pass data, but instead using individual names of items while passing items through flask. 


Techinical Issues: One of the issues that I was having was how to display new information when you refreshed the app. Was a simple solution to include the python code in the def index(). I figured out how to do it by looking up the flask API.

Another Techinal issue was how to send all of the data needed to populate the each of the fields. I created a class, and then inserted all of the individual items into the class. When I pick an item to display by random, the list of all of the items, one is picked. Then I send the data of that in a dynamic way so it can handle different ones. I think using JSON would have been more efficient, and will convert it to that, but this was an easy example.

Techinal issue: didnt want to go in an infinite loop and use all of the credits if the information is missing on a recipe that I was randomly givin by the api, or if there was no tweet that mentioned that information. Put it in a loop, with a try catch. If something did not work, then the loop would redo the try catch. put in a condition at the bottom of the loop to make sure that this was not an issue. 

Had the same recipe keep coming up when you typed something in, used the spoonacular API call that I was using to get more recipies with that name used in it. Use a random number generator to pick which one it goes to. 

Twitter API was not finding any tweets with the recipe title, created multiple loops for it to search for multiple things, if it did not find any, then I had a try catch loop to find a new recipe to then find new information for it. 

When user input the form, I left the action blank so it will go to the base index, I did this with the restful web app becasue I did not know how to get to the new path that the information was stored on. By keeping the action blank it kept it the same. I found this out by looking up flask and forms. This was important because the dual action of searching for new recipe and refreshing the page will give you two different items. When you use the form, you should get a recipe that contains your search term. If you refresh the page, then the page should give you a completely random recipe. 
