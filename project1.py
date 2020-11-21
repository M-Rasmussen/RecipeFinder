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
import model as mod


app = flask.Flask(__name__)


@app.route('/',methods=['post','get'])
def searchfood():
    ingredientsSP=[]
    instructionsSP=[]
    if request.method=='POST':
        ### call request api function
        a=request.form.get('search')
        foodId=mod.itemSearch(a)
    else:
        foodId=mod.itemRandom()
    
    json_body2=mod.getRecipe(foodId)
            #####USE ID gathered from foodID API and then parse the information from the API and store it in variables declared above
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
    
    tweeter=mod.twitterCall(nameSP)
    
    if tweeter != "error":
        return flask.render_template("index.html", iName = nameSP, iPic = picSP, iServing=servingSizeSP, iMinutes=prepTimeSP, iIngredients=ingredientsSP, iInstructions=instructionsSP, itweeterName=tweeter["tweetUserName"], itweeterText=tweeter["tweetText"], itweeterDate=tweeter["tweetDate"], iLink=linkSP )
    else:        
        return flask.render_template("failcase.html")
                ##Fail safe to prevent endless loop, if it gets to this case then I should really make a 404 page but have not yet... EXTREME EDGE CASE THOUGH
if __name__=='__main__':    
    app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True,
    use_reloader=True
    )
