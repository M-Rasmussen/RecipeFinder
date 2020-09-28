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

app = flask.Flask(__name__)


@app.route('/',methods=['post','get'])
def searchfood():
    ###Variables being that will store information to pass through the flask API
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
    checker=0
    failCounter=0
    fAILSafty = 0
    
    ##########get reandom number so if one puts in the same recipe a different one will show up
    ranNum=random.randint(0,9)
    ################IF the user fills out the form
    
    if request.method=='POST':
        a=request.form.get('search')
        urlSearch="https://api.spoonacular.com/recipes/complexSearch?query="+a+"&number=10&apiKey={}".format(spoonacular_key)
        responseSearch = requests.get(urlSearch)
        json_bodySearch = responseSearch.json()
        ###get id of the dish that was searched for, checker is the flag
        checker=1
    else:
        #####if the user does not fill out the form, but refreshes the page and wants to get a random recipe
        urlRefresh="https://api.spoonacular.com/recipes/random?number=10&apiKey={}".format(spoonacular_key)
        responseRefresh = requests.get(urlRefresh)
        json_bodyRefresh = responseRefresh.json()
        ####Will return 10 random recipies variables. Checker is a flag
        checker=0
    while fAILSafty==0:
        ####WHile loop with flag of 10 becasue although my code is inefficent and gets a random number, i will cut off the amount of times I call the api so I do not get in a endless loop and use the quota
        try:
            ###If one of the Recipes is missing information or the tweet call fails, generate new random number and pick a new recipe to parse
            tweetText="NONE"
            ranNum=random.randint(0,9)
            #### Have this so if the page is refreshed then use one, and if the user enters, then it will address that.
            if checker ==1:
                foodId=(json.dumps(json_bodySearch["results"][ranNum]["id"],indent=2))
            else:
                foodId=(json.dumps(json_bodyRefresh["recipes"][ranNum]["id"],indent=2))
            
            #####USE ID gathered from foodID API and then parse the information from the API and store it in variables declared above
            url2 = "https://api.spoonacular.com/recipes/"+foodId+"/information?apiKey={}".format(spoonacular_key)
            response2 = requests.get(url2)
            json_body2 = response2.json()
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
            
            ###make the title of recipe a hashtag
            
            tweetnameSearch=nameSP.replace(" ","")
            ####Search Twitter API, try 3 different variations of the code for it. 
            tweets=tweepy.Cursor(auth_api.search, q=nameSP, lang="en").items(1)
            for tweet in tweets:
                tweetText=tweet.text
                tweetUserName=tweet.user.screen_name
                tweetDate=tweet.created_at
            if tweetText=="NONE":
                tweets=tweepy.Cursor(auth_api.search, q=tweetnameSearch, lang="en").items(1)
                for tweet in tweets:
                    tweetText=tweet.text
                    tweetUserName=tweet.user.screen_name
                    tweetDate=tweet.created_at
                if tweetText=="NONE":
                    tweets=tweepy.Cursor(auth_api.search, q=a, lang="en").items(1)
                    for tweet in tweets:
                        tweetText=tweet.text
                        tweetUserName=tweet.user.screen_name
                        tweetDate=tweet.created_at
            ###IF all was sucessfull return information to flask
            return flask.render_template("index.html", iName = nameSP, iPic = picSP, iServing=servingSizeSP, iMinutes=prepTimeSP, iIngredients=ingredientsSP, iInstructions=instructionsSP, itweeterName=tweetUserName, itweeterText=tweetText, itweeterDate=tweetDate, iLink= linkSP)
        except:
            ##Try again with new recipe that was gained from the search, will repeate if gets here. 
            failCounter=failCounter+1
            if failCounter>9:
                fAILSafty=1
                ##Fail safe to prevent endless loop, if it gets to this case then I should really make a 404 page but have not yet... EXTREME EDGE CASE THOUGH
if __name__=='__main__':    
    app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True,
    use_reloader=True
    )
