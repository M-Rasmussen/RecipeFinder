import sys
import os
import flask
from flask import Flask, request
import random
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import tweepy
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv

'''Path to load Keys and to initilize them'''
dotenv_path = join(dirname(__file__), 'project1.env')
load_dotenv(dotenv_path)

twitter_consumer_key=os.environ['TWIITER_CONSUMER_KEY']
twitter_consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']
twitter_access_token=os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
spoonacular_key = os.environ['SPOONACULAR_KEY']

'''Autheticate Twitter API'''
auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
auth_api = API(auth)

'''date_since'''
date_since="2015-01-01"


'''Search Spoonacular'''
'''
url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(spoonacular_key)

response = requests.get(url)
json_body = response.json()
#Variables being that will store information to pass through the flask API
nameSP=""
picSP=""
linkSP=""
prepTimeSP=""
servingSizeSP=""
instructionsSP=[]
ingredientsSP=[]
tweetText="NONE"
tweetUserName="NONE"
tweetDate="NONE"

foodId=(json.dumps(json_body["results"][0]["id"],indent=2))

#USE ID gathered from foodID API and then parse the information from the API and store it in variables declared above
url2 = "https://api.spoonacular.com/recipes/"+foodId+"/information?apiKey={}".format(spoonacular_key)
response2 = requests.get(url2)
json_body2 = response2.json()
#print(json.dumps(json_body2, indent=2))
for item in json_body2["extendedIngredients"]:
    ingredientsSP.append(item["original"]) 
    
for instructOut in json_body2["analyzedInstructions"]:
    for instructIn in instructOut["steps"]:
        instructionsSP.append(instructIn["step"])
        
nameSP=json_body2["title"]
picSP=json_body2["image"]
linkSP=json_body2["spoonacularSourceUrl"]
servingSizeSP=json_body2["servings"]
prepTimeSP=json_body2["readyInMinutes"]

#make the title of recipe a hashtag
tweetname=nameSP.replace(" ","")
tweetSearch="#"+tweetname

print("*******************")
print(nameSP)
print(picSP)
print(linkSP)
print(servingSizeSP)
for x in ingredientsSP:
    print(x)
for y in instructionsSP:
    print(y)
print(tweetSearch)

tweets=tweepy.Cursor(auth_api.search, q=tweetSearch, lang="en").items(1)
for tweet in tweets:
    tweetText=tweet.text
    tweetUserName=tweet.user.screen_name
    tweetDate=tweet.created_at
'''    

app = flask.Flask(__name__)


@app.route('/',methods=['post','get'])
def searchfood():
    '''Variables being that will store information to pass through the flask API'''
    nameSP=""
    picSP=""
    linkSP=""
    prepTimeSP=""
    servingSizeSP=""
    instructionsSP=[]
    ingredientsSP=[]
    tweetText="NONE"
    tweetUserName="NONE"
    tweetDate="NONE"
    a=""
    '''IF the user fills out the form'''
    if request.method=='POST':
        a=request.form.get('search')
        url="https://api.spoonacular.com/recipes/complexSearch?query="+a+"&number=10&apiKey={}".format(spoonacular_key)
        response = requests.get(url)
        json_body = response.json()
        
        '''get reandom number so if one puts in the same recipe a different one will show up'''
        ranNum=random.randint(0,9)
        foodId=(json.dumps(json_body["results"][ranNum]["id"],indent=2))
        
    else:
        '''if the user does not fill out the form, but refreshes the page and wants to get a random recipe''' 
        url="https://api.spoonacular.com/recipes/random?number=1&apiKey={}".format(spoonacular_key)
        response = requests.get(url)
        json_body = response.json()
        foodId=(json.dumps(json_body["recipes"][0]["id"],indent=2))

    ''' USE ID gathered from foodID API and then parse the information from the API and store it in variables declared above'''
    url2 = "https://api.spoonacular.com/recipes/"+foodId+"/information?apiKey={}".format(spoonacular_key)

    response2 = requests.get(url2)
    json_body2 = response2.json()
    print("**************************")
    print(json.dumps(json_body2, indent=2))
    print("**************************")    
    for item in json_body2["extendedIngredients"]:
        ingredientsSP.append(item["original"]) 
        
    for instructOut in json_body2["analyzedInstructions"]:
        for instructIn in instructOut["steps"]:
            instructionsSP.append(instructIn["step"])
            
    nameSP=json_body2["title"]
    picSP=json_body2["image"]
    linkSP=json_body2["spoonacularSourceUrl"]
    servingSizeSP=json_body2["servings"]
    prepTimeSP=json_body2["readyInMinutes"]
    
    '''make the title of recipe a hashtag'''
    tweetnameSearch=nameSP.replace(" ","")
   
    
    print("*******************")
    print(nameSP)
    print(picSP)
    print(linkSP)
    print(servingSizeSP)
    for x in ingredientsSP:
        print(x)
    for y in instructionsSP:
        print(y)
    print(tweetnameSearch)
    
    tweets=tweepy.Cursor(auth_api.search, q=tweetnameSearch, lang="en",since=date_since).items(1)
    for tweet in tweets:
        tweetText=tweet.text
        tweetUserName=tweet.user.screen_name
        tweetDate=tweet.created_at
    print(tweetText)
    print(a)
    if tweetText=='NONE' and a !="":
        tweets=tweepy.Cursor(auth_api.search, q=a, lang="en",since=date_since).items(1)
        for tweet in tweets:
            tweetText=tweet.text
            tweetUserName=tweet.user.screen_name
            tweetDate=tweet.created_at
    return flask.render_template("index.html", iName = nameSP, iPic = picSP, iServing=servingSizeSP, iMinutes=prepTimeSP, iIngredients=ingredientsSP, iInstructions=instructionsSP, itweeterName=tweetUserName, itweeterText=tweetText, itweeterDate=tweetDate, iLink= linkSP)


if __name__=='__main__':    
    app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True,
    use_reloader=True
    )
