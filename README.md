create twitter developer user to gain access to the twitter API. 
write code to be able to access the twitter api -->twitter_consumer_key=os.environ['TWIITER_CONSUMER_KEY']
twitter_consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']
twitter_access_token=os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
auth_api = API(auth)
<--
Create a project1.env inorder to store your keys. ^^^ is how you will call the key tokens inorder for the python file to access the code. 
download tweepy from pip
download flask from pip
create class to hold each recipe
create object and hold the information of each of the recipies.
hard code the recipies in. 
Create list of all the recipe objects. 
Pick random number between 0 and 6 that picks one of the recipies.
The random number that is picked will represent one of the recipies that we have. 
Pass that information using the flask.render_template to the html. 
Also use the name of the recipe to search twitter using the twitter API.
Use the Cursor(Cursor(auth_api.search, q=[name of item], lang="en",since=[time]).items([items to return]). will return an object, go through that object and pull out the tweet.text to get context, tweet.user.screen_name to get the authors name, and tweet.created_at to get the time the tweet was made.
Pass these variables to the template in the flask.render_template call.
Create templates folder to hold the html files.
Create index.html file.
Wrote html code using bootstrap div to create coloums easier. 
Import the bootstrap libary
Create a static folder
create style.css
populate style.css with code to style the index.html website. 

