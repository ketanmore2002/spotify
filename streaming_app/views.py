from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.files import File


from .songs import request_song
from .models import *
import pytube

import random

# Create your views here.

def index(requests):

    songs = music.objects.all()

    song = music.objects.all()[0:12]

    return render(requests, 'base/index.html',{"songs":songs,"song":song})


def search_name(name):

        s = pytube.Search(str(name))
        yt = pytube.YouTube(s.results[0].watch_url)

    
        tag=yt.streams.filter(only_audio=True)[0].itag
        stream = yt.streams.get_by_itag(tag)
        stream.download(filename=str((s.results[0]).video_id)+".mp4",output_path="streaming_app/temp_song")

        title = s.results[0].metadata[0]["Song"]
        video_id =s.results[0].video_id
        thumbnail_url = s.results[0].thumbnail_url
        author = s.results[0].metadata[0]["Artist"]
        pb = str(s.results[0].publish_date)
        publish_date = pb[:-9]
        length = s.results[0].length

        import os.path
        SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

        song = open((SITE_ROOT+"/temp_song/"+video_id + ".mp4"), 'rb')

        obj=music.objects.create(title = title,video_id = video_id,thumbnail_url = thumbnail_url,author = author,publish_date = publish_date,length = length)
        obj.song.save(name + ".mp4", File(song))

        return redirect("/search/"+str(s.results[0].video_id))






def index(requests):

    songs = music.objects.all()

    song = music.objects.all()[0:12]

    this_weeks_top = music.objects.all()[0:7]

    new_hits = music.objects.all()[0:7]

    return render(requests, 'base/index.html',{"songs":songs,"song":song,"this_weeks_top":this_weeks_top,"new_hits":new_hits})



def play(requests,video_id):

    songs = music.objects.all().filter(video_id = video_id)

    random_songs = music.objects.all()

    random_songs =  random.sample(list(random_songs), k=10)


    return render(requests, 'player/index.html',{"songs":songs, "random_songs": random_songs})


def search(requests):

    songs = music.objects.all()

    if requests.method == "POST":

        song_name = requests.POST["song_name"]

        s = pytube.Search(str(song_name))
        
        if music.objects.all().filter(video_id = s.results[0].video_id).exists():
            print("yesss!")
            return redirect("/play/"+str(s.results[0].video_id))

        else:
            search_name(song_name)
            return redirect("/play/"+ s.results[0].video_id)

    return render(requests, 'base/albums-store.html',{"songs":songs})