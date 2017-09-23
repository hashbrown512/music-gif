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
# gets total number of gifs returned
num_gifs = len(json.loads(jsonData)["data"])
# gets a URL for a random looping gif
jsonDict = json.loads(jsonData)["data"][random.randrange(0,num_gifs)]["images"]["looping"][u'mp4']
print "json Dict: ", jsonDict
