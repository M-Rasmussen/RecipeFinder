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
    urlSearch="https://api.spoonacular.com/recipes/complexSearch?query="+a+"&number=10&apiKey={}".format(spoonacular_key)
    responseSearch = requests.get(urlSearch)
    json_bodySearch = responseSearch.json()
    return json_bodySearch
def itemRandom():
    #Gets of list of random items
    urlRefresh="https://api.spoonacular.com/recipes/random?number=10&apiKey={}".format(spoonacular_key)
    responseRefresh = requests.get(urlRefresh)
    json_bodyRefresh = responseRefresh.json()
    return json_bodyRefresh