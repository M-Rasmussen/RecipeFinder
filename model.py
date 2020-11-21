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


def itemSearch(a):
    #gets a list of items that contain that key word
    urlSearch="https://api.spoonacular.com/recipes/complexSearch?query="+a+"&number=5&apiKey={}".format(spoonacular_key)
    responseSearch = requests.get(urlSearch)
    json_bodySearch = responseSearch.json()
    ranNum=random.randint(0,4)
    foodId=(json.dumps(json_bodySearch["results"][ranNum]["id"],indent=2))
    return foodId
    
def itemRandom():
    #Gets of list of random items
    urlRefresh="https://api.spoonacular.com/recipes/random?number=5&apiKey={}".format(spoonacular_key)
    responseRefresh = requests.get(urlRefresh)
    json_bodyRefresh = responseRefresh.json()
    ranNum=random.randint(0,4)
    foodId=(json.dumps(json_bodyRefresh["recipes"][ranNum]["id"],indent=2))
    return foodId

def getRecipe(foodId):
    url2 = "https://api.spoonacular.com/recipes/"+foodId+"/information?apiKey={}".format(spoonacular_key)
    response2 = requests.get(url2)
    json_body2 = response2.json()
    return json_body2

def twitterCall(nameSP):
    #Twitter Call Statemetns
    tweetdict = {
        "tweetText":"NONE",
        "tweetUserName":"NONE",
        "tweetDate":"NONE"
        }
    tweets=tweepy.Cursor(auth_api.search, q=nameSP, lang="en").items(1)
    for tweet in tweets:
        tweetdict["tweetText"]=tweet.text
        tweetdict["tweetUserName"]=tweet.user.screen_name
        tweetdict["tweetDate"]=tweet.created_at
    if tweetdict["tweetText"]=="NONE":
        tweetnameSearch=nameSP.replace(" ","")
        tweets=tweepy.Cursor(auth_api.search, q=tweetnameSearch, lang="en").items(1)
        for tweet in tweets:
            tweetdict["tweetText"]=tweet.text
            tweetdict["tweetUserName"]=tweet.user.screen_name
            tweetdict["tweetDate"]=tweet.created_at
    if tweetdict["tweetText"]=="NONE":
        return "error"
    return tweetdict

    