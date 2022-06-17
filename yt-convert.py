from pytube import YouTube

youtube_link = input("Input the youtube url of the video that you \
would to convert to audio: ")

yt = YouTube(youtube_link)

# confirmation 
print(f'Is this the correct title of the youtube video? \n "{yt.title}" \n')
confirm = input("Type Y/y for yes or N/n for no: ")
proceed = False

# loop through video confirmation process until user agrees
while (proceed == False):

    if (confirm.lower() == 'y'):
        proceed = True

    elif (confirm.lower() == 'n'):
        youtube_link = input("Retype the youtube url of the video that you \
would to convert to audio: ")
        print(f'Is this the correct title of the youtube video? \n "{yt.title}" \n')
        confirm = input("Type Y/y for yes or N/n for no: ")

yt = YouTube(youtube_link)