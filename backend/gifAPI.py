import urllib, json
import random


# with open("testFiles/letsGetLost.json", "r") as data_file:
#     lyrics_json = json.load(data_file)
# print lyrics_json


def gif_json(phrase):
    """
    Input: string of lyrics of a line
    output: a json file of the top gifs related to the search

    uses the GIPHY API and returns the json file for 25 gifs
    related to the search phrase.
    """
    url_word = phrase.replace(" ", "+")  # take out spaces for url search
    data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + url_word + "&api_key="
                                                                                           "Yi4YMIrlGAlJQYnrY3vb0YljKGMiF5hM&limit=5").read())
    return data


def phrase_to_url(word):
    """
    Input: word or phrase of words
    Output: the gif url for the json file
    """
    json_data = json.dumps(gif_json(word), sort_keys=True, indent=4)  # dump out json object.
    # gets total number of gifs returned
    num_gifs = len(json.loads(json_data)["data"])
    # gets a URL for a random looping gif
    json_dict = json.loads(json_data)["data"][random.randrange(0, num_gifs)]["images"]["original"]["url"]
    # [u'images'][u'original'][u'url']
    # print 'JSON DICT: ' + json_dict
    return json_dict


def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i) < 128)


def parse_lyrics(lyrics):
    """
    Input: the json file of a song
    Output: a list of tuples containing the start time and the gif URL associated with each line in the song
    """
    print 'Searching for relevant GIFs'
    lines = []
    for lyricInfo in lyrics["fragments"]:
        # print lyricInfo
        duration = float(lyricInfo["end"]) - float(lyricInfo["begin"])
        lyric_phrase = lyricInfo["lines"][0]
        filtered_phrase = remove_non_ascii(lyric_phrase)
        # print 'lyric phrase: ' + lyric_phrase
        # print 'filter phrase: ' + filtered_phrase
        if filtered_phrase != "":
            lines.append((duration, phrase_to_url(filtered_phrase)))
    # print lines
    return lines


def gif_urls(lyrics):
    """
    Input: list of lyrics, where each element in the list is a string of the line from the song
    Output: a list of gif urls

    NOT CURRENTLY USED IN THE CODE
    """
    urls = []
    for line in lyrics:
        urls.append(phrase_to_url(line))
    return urls
