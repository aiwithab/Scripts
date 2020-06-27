from pytube import YouTube

userProvidedLink = input('|Enter link of youtube video to download it :| ')
youtubeVideo = YouTube(userProvidedLink)

try:
    
    print(f'|Title| : {youtubeVideo.title}')
    print(youtubeVideo.streams.filter(progressive=True))

except:
    print('|An error occured while fetching video information kindly try again!|')

finally:
    print('|Chose quality of the video to download it.|')


tag = input('|Enter tag of video to download it :| ')

youtubeStreamVideo = youtubeVideo.streams.get_by_itag(tag)

print('|Downloading ....|')

try:

    youtubeStreamVideo.download()

except:

    print('Cant download video at this time try again later!')

print('|Video is ownloaded into your current directry!|')
