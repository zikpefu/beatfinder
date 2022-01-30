import json
from pytube import YouTube
import os

yt = YouTube('https://www.youtube.com/watch?v=16y1AkoZkmQ')
  
video = yt.streams.filter(only_audio=True).first()
  
destination = '.'
os.chdir('/tmp')

out_file = video.download()

filename = 'Boney M - Rasputin (Sopot Festival 1979) (VOD).mp3'

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

val = os.path.isfile('/tmp/' + filename)

def lambda_handler(event, context):
    # TODO implement
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }