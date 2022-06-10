import pytube

def request_song (name):

    
    s = pytube.Search(str(name))
    yt = pytube.YouTube(s.results[0].watch_url)
    tag=yt.streams.filter(only_audio=True)[0].itag
    stream = yt.streams.get_by_itag(tag)
    stream.download(filename=str((s.results[0]).video_id)+".mp4")

request_song("closer")