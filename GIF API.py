import urllib,json
import random

"""
Simple method that takes in a string, uses the GIPHY API and returns the json file for 25 gifs
related to the search word.
"""
def gifgetter(word):
    urlword =  word.replace(" ", "+") #take out spaces for url search
    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + urlword + "&api_key="
                                     "Yi4YMIrlGAlJQYnrY3vb0YljKGMiF5hM&limit=5").read())
    return data



jsonData = json.dumps(gifgetter("spongebob"), sort_keys=True, indent=4) #dump out json object.
print jsonData
# parses the json file to return a URL of a random gif from the gifs that are returned in the search
jsonDict = json.loads(jsonData)["data"][random.randrange(0,10)]["images"]["480w_still"]
# print jsonDict