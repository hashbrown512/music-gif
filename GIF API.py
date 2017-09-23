import urllib,json
import random


def gif_json(word):
  """
  Takes in a string of words, uses the GIPHY API and returns the json file for 25 gifs
  related to the search phrase.
  """
  url_word =  word.replace(" ", "+") #take out spaces for url search
  data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + url_word + "&api_key="
                                   "Yi4YMIrlGAlJQYnrY3vb0YljKGMiF5hM&limit=5").read())
  return data



def phrase_to_url(word):
  """
  Input: word or phrase of words
  Output: the gif url for the json file
  """
  jsonData = json.dumps(gif_json(word), sort_keys=True, indent=4) #dump out json object.
  # print jsonData
  # gets total number of gifs returned
  num_gifs = len(json.loads(jsonData)["data"])
  # gets a URL for a random looping gif
  jsonDict = json.loads(jsonData)["data"][random.randrange(0,num_gifs)][u'images'][u'original'][u'url']
  # [random.randrange(0,num_gifs)]["original"]["url"][u'mp4']
  return jsonDict

def gif_urls(lyrics):
  """
  Input: list of lyrics, where each element in the list is a string of the line from the song
  Output: a list of gif urls
  """
  urls = []
  for line in lyrics:
    urls.append(phrase_to_url(line))
  return urls


print gif_urls(["Hey, I just met you",
"and this is crazy",
"but here's my number",
"so call me maybe"])