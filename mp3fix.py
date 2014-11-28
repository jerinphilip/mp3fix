#!/usr/bin/python2
import sys
import urllib, urllib2
import json
import eyed3

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
    x = 0
    for i in data["tracks"]:
        print x,": ",
        x = x + 1
        print i["track_title"]+",",
        for artist in i["artist"]:
            print artist["name"]+",",
        print i["album_title"]
    k = raw_input()
    return int(k)


def writesong(filename, data):
    tag = eyeD3.Tag()
    tag.link(filename)
    tag.setversion([2,3,0])
    tag.setArtist(data["artist"][0]["name"])
    tag.setAlbum(data["album_title"])
    tag.setAlbumArtist(data["artist"][1]["name"])
    tag.setTitle(data["track_title"])
    af.tag.save()

def readsong(filename):
    af = eyed3.load(filename)
    print af.tag.title+","+af.tag.album+","+af.tag.artist

def scanfolder(path):
    """Scans a folder for mp3s """
    print "Currently does nothing!"
    


y = raw_input()
readsong(y)
q = raw_input()
x = searchsong(q)
z = decrypt(x)
writesong(y, x["tracks"][z])
