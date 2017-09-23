import urllib
import bs4
import os.path


def scrape_lyrics(song_filename):
    song_title = os.path.splitext(song_filename)[0]  # remove extension from filename to get song title
    song_search = song_title + ' lyrics'  # create the words to be searched in Bing
    url = "https://www.bing.com/search?" + urllib.urlencode({"q": song_search})  # create the Bing query

    print 'Searching for lyrics'

    # Perform Bing query and scrape the results for lyrics
    response = urllib.urlopen(url)
    html = response.read()
    soup = bs4.BeautifulSoup(html, "html.parser")
    my_p = soup.findAll("p", {"class": "b_paractl"})
    lyrics = ''
    for p in my_p:
        string = str(p).replace('<p class="b_paractl">', '')
        string = string.replace('<br/>', '\n')
        string = string.replace('</p>', '')
        lyrics += string

    print 'Lyrics parsed'

    # write out the lyrics to a txt file
    lyric_file = open(song_title + '.txt', 'w')
    lyric_file.write(lyrics)
    lyric_file.close()

    print 'Lyrics written to txt'

