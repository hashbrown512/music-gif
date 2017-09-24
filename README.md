# GIF Music Video Maker
Authors:
Michael Blankenship,
Erik Yamada,
Harrison Brown,
Justin Fan

The backend completely works. Given the youtube URL, we download the audio file, scrape the web for lyrics, and sync the lyrics with the audio file. Then, we find relevant GIFs for each line of the lyrics and sync those GIFs with the audio. We ran into problems developing a front end which means none of this gets displayed.

In order to see what works, open **testTimestampedGifs.py** and give it a youtube url to a song and run the file! You must have the packages below installed.

We also registered the domain name **songiphy.com** since we are using the Giphy API. *Note: currently, songiphy.com does not host our content though

API Installations:

NEED TO INSTALL homebrew: 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

NEED TO INSTALL YoutubeDL:
hombrew style: brew install youtube-dl

NEED TO INSTALL safygiphy:
sudo pip install safygiphy

NEED TO INSTALL Aeneas: 
https://github.com/sillsdev/aeneas-installer/releases



