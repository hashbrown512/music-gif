import json
import youtubeToAudio
import lyricScraper
import audioLyricSyncer

# Read in JSON to get youtube URL
with open("urlsAndTitles.json", "r") as data_file:
    jsonData = json.load(data_file)

youtube_url = jsonData["youtube_url"]  # set youtube URL
song_filename = youtubeToAudio.youtube_to_audio(youtube_url)  # download audio, get the filename
lyricScraper.scrape_lyrics(song_filename)  # scrape Bing for lyrics and output to txt
audioLyricSyncer.sync_lyrics_to_audio(song_filename)  # sync lyrics with audio and output to JSON
print 'DONE'
