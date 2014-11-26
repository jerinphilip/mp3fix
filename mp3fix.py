#!/usr/bin/python2

import sys
import urllib, urllib2
import json

def searchalbum(query):
    """Tries to Retrieve data off the Internet"""
    link = "http://api.gaana.com/?type=search&subtype=search_song&key="+query;
    page = urllib2.urlopen(link)
    data = json.load(page)
    return data;


def searchsong(query):
    """Tries to Retrieve data off the Internet"""
    link = "http://api.gaana.com/?type=search&subtype=search_song&key="+query;
    page = urllib2.urlopen(link)
    data = json.load(page)
    return data;

def decrypt(data):
    """Converts to valid info"""
    for i in data["tracks"]:
        print i["track_title"];
        for artist in i["artist"]:
            print artist["name"]
        print i["album_title"]
        print "\n"
y = raw_input()
x = searchsong(y)
decrypt(x)
