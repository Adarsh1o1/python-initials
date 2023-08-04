from pytube import YouTube

SAVE_PATH = "C:\\Users\\adars\\Desktop" 

link="https://youtu.be/gtY_KPgHCWE"

yt = YouTube(link)
mp4files = yt.filter('mp4')

d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	d_video.download(SAVE_PATH)
except:
	print("Some Error!")
print("Downlaod Completed!")
