import subprocess
import os.path


def sync_lyrics_to_audio(song_filename):
    song_title = os.path.splitext(song_filename)[0]  # remove extension from title
    text_filename = song_title + '.txt'
    output_filename = song_title + '.json'

    command = ['python', '-m', 'aeneas.tools.execute_task', song_filename, text_filename,
               'task_language=eng|os_task_file_format=json|is_text_type=plain', output_filename]

    print 'Executing Aeneas lyric-audio sync'

    try:
        output = subprocess.check_output(command)
    except subprocess.CalledProcessError as exc:
        print exc.output

    print 'Aeneas complete, synced lyrics in JSON'

