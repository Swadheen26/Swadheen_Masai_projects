print("Enter:'1' To downlod the Audio🔊 file of the given link")
print("Enter:'2' To downlod the Video🎥 file of the given link")

user=int(input("Enter Your Choice:"))

if user == 1:
    from pytube import YouTube

    link = input("Enter Video link:")
    yt = YouTube(link)

    audio = yt.streams.get_audio_only()
    audio.download()
    
    print("Audio Downloaded Successfully !")

if user == 2:
    from pytube import YouTube

    link = input("Enter Video link:")
    yt = YouTube(link)

    videos = yt.streams.all()
    vid = list(enumerate(videos))
    for i in vid:
        print(i)

    print()

    # path = r"C:\Users\Swadheen Prusty\Downloads"

    Opt = int(input("Choose the option you want to download:"))
    videos[Opt].download()

    # videos[Opt].download(path) # To download in respective path.

    print("Video Downloaded Successfully !")