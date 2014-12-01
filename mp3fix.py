#!/usr/bin/python2
import sys
import urllib, urllib2
import json
import eyed3

def search_album(query):
    """Tries to Retrieve data off the Internet"""
    link = "https://api.gaana.com/?type=search&subtype=search_song&key="+query;
    page = urllib2.urlopen(link)
    data = json.load(page)
    return data;


def search_song(query):
    """Tries to Retrieve data off the Internet"""
    link = "http://api.gaana.com/?type=search&subtype=search_song&key="+query;
    page = urllib2.urlopen(link)
    data = json.load(page)
    return data;

def get_artwork(link):
    image = urllib2.urlopen(link)
    print link
    tmpfile = open("temp.jpg", "w+")
    tmpfile.write(image.read())
    tmpfile.close()
    return image.read()


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

def write_alter(filename, data):
    tag = eyed3.id3.tag.Tag()
    tag.link(filename)
    tag.setVersion([2,3,0])
    tag.addImage(0x08, "temp.jpg")
    tag.setArtist(date["artist"][0]["name"])
    tag.setTitle(data["track_title"])
    tag.setAlbumTitle(data["album_title"])
    tag.update()


def write(filename, data):
    af = eyed3.load(filename)
    af.tag.artist = data["artist"][0]["name"]
    af.tag.album = data["album_title"]
    af.tag.album_artist = data["artist"][1]["name"]
    af.tag.title = data["track_title"]
    af.tag.genre = data["gener"]["name"]
    af.tag.comments = "Cleaned by mp3fix"
    print data["artwork_large"]
    image = urllib2.urlopen(data["artwork_large"])
    af.tag.images.set(3, open("temp.jpg", "rb+").read(), "image/jpeg");
    af.tag.save()
    read_song(filename)
    print "Successfully Written"


def read_song(filename):
    af = eyed3.load(filename)
    print af.tag.title+","+af.tag.album+","+af.tag.artist

def scan_folder(path):
    """Scans a folder for mp3s """
    print "Currently does nothing!"

def start_process(filename):
    read_song(filename)
    song_title = raw_input()
    result = search_song(song_title)
    selection = decrypt(result)
    write(filename, result["tracks"][selection])

start_process("t.mp3")
