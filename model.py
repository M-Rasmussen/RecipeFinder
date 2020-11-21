'''Module Class'''
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

dotenv_path = join(dirname(__file__), "project1.env")
load_dotenv(dotenv_path)

twitter_consumer_key = os.environ["TWIITER_CONSUMER_KEY"]
twitter_consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
twitter_access_token = os.environ["TWITTER_ACCESS_TOKEN"]
twitter_access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
spoonacular_key = os.environ["SPOONACULAR_KEY"]

"""Autheticate Twitter API"""
auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
auth_api = API(auth)


def item_search(ans):
    '''gets a list of items that contain that key word'''
    url_search = (
        "https://api.spoonacular.com/recipes/complexSearch?query="
        + ans
        + "&number=5&apiKey={}".format(spoonacular_key)
    )
    response_search = requests.get(url_search)
    json_body = response_search.json()
    ran_num = random.randint(0, 4)
    food_id = json.dumps(json_body["results"][ran_num]["id"], indent=2)
    return food_id


def item_random():
    ''' Gets of list of random items'''
    url_refresh = "https://api.spoonacular.com/recipes/random?number=5&apiKey={}".format(
        spoonacular_key
    )
    response_refresh = requests.get(url_refresh)
    json_body = response_refresh.json()
    ran_num = random.randint(0, 4)
    food_id = json.dumps(json_body["recipes"][ran_num]["id"], indent=2)
    return food_id


def get_recipe(food_id):
    '''get food recipe'''
    url = (
        "https://api.spoonacular.com/recipes/"
        + food_id
        + "/information?apiKey={}".format(spoonacular_key)
    )
    response = requests.get(url)
    json_body2 = response.json()
    return json_body2


def twitter_call(name_sp):
    ''' Twitter Call Statemetns'''
    tweetdict = {"tweetText": "NONE", "tweetUserName": "NONE", "tweetDate": "NONE"}
    tweets = tweepy.Cursor(auth_api.search, q=name_sp, lang="en").items(1)
    for tweet in tweets:
        tweetdict["tweetText"] = tweet.text
        tweetdict["tweetUserName"] = tweet.user.screen_name
        tweetdict["tweetDate"] = tweet.created_at
    if tweetdict["tweetText"] == "NONE":
        tweet_name_search = name_sp.replace(" ", "")
        tweets = tweepy.Cursor(auth_api.search, q=tweet_name_search, lang="en").items(1)
        for tweet in tweets:
            tweetdict["tweetText"] = tweet.text
            tweetdict["tweetUserName"] = tweet.user.screen_name
            tweetdict["tweetDate"] = tweet.created_at
    if tweetdict["tweetText"] == "NONE":
        return "error"
    return tweetdict
