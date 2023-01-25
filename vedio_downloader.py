from pytube import YouTube, Playlist


def download(v_link):
    youtubeObject = YouTube(v_link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download('Downloads')
    except:
        print("An error has occurred\n")
    print("Download is completed successfully\n")


links = []
statu = int(input('For downloading playlist press"0", for one by one press "1".\n'))
if statu == 1:
    num = int(input('How many videos do you want to download :\n'))
    for i in range(num):
        link = input("Enter the YouTube video link: \n")
        links.append(link)
    for j in range(num):
        download(links[j])
elif statu == 0:
    link = input("Enter the YouTube playlist link: \n")
    playlist = Playlist(link)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video_url in playlist.video_urls:
        download(video_url)
