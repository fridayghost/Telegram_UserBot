from pytube import YouTube
import os

def downloadYouTube(url, res, output_path = os.getcwd()):

    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4', res = res + "p").order_by('resolution').desc().first()
    try:
        yt.download(output_path = output_path)
    except:
        return "Error downloading the video. Please try again with a different resolution."
    return yt.title

# import youtube_dl
# import os
#
# def downloadYouTube(url, res):
#
#     try:
#         if res == "360":
#             format_code = "18"
#         elif res == "720":
#             format_code = "22"
#         else:
#             format_code = "137"
#
#
#         options = {'outtmpl': 'video.mp4', 'format': format_code}
#
#         try:
#             os.remove("video.mp4")
#         except:
#             pass
#
#         with youtube_dl.YoutubeDL(options) as ydl:
#             # ydl.download(url)
#             info_dict = ydl.extract_info(url, download=True)
#             video_url = info_dict.get("url", None)
#             video_id = info_dict.get("id", None)
#             video_title = info_dict.get('title', None)
#
#         return video_title
#     except:
#         return "Video download failed. Please try again with different resolution.\nPlease note 'only 360 and 720 resolutions are supported.'"

text = '''/yt https://www.youtube.com/watch?v=Hh0t2f2IU3s 360'''

url_res = text.replace("/yt",'').strip().split(" ")

print(downloadYouTube(url_res[0], url_res[1]))