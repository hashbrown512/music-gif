import subprocess


def youtube_to_audio(youtube_url):
    # Download audio file from youtube
    print 'Downloading audio'
    output = subprocess.check_output(('youtube-dl ' + youtube_url + ' -f bestaudio -o %(title)s.%(ext)s').split(" "))
    filename = None
    for line in output.splitlines():
        if "Destination" in line:
            idx = line.index("Destination: ") + 13
            filename = line[idx:]
        elif "has already been downloaded" in line:
            idx = line.index("[download] ") + 11
            filename = line[idx:-28]
    print 'Audio downloaded, returning the filename'
    return filename
