from win11toast import toast
from time import sleep
# simple notification
# toast("this is supraaa","got it?",icon="C:\\Users\\adars\\Downloads\\rollsroyce_front_view_headlights_136993_1280x720.jpg",image="C:\\Users\\adars\\Downloads\\toyota_supra_white_79799_1152x864.jpg",audio="ms-winsoundevent:Notification.Default",button="Dismiss")
# time.sleep(2)
# toast("hello","click to open url",on_click="https://adarshportfolio.blogspot.com/2023/03/news-extractor.html")

# buttons
toast("click to open url",app_id='Project Pals',on_click="https://adarshportfolio.blogspot.com/2023/03/news-extractor.html",buttons=['approve','dismiss','other'])


# playing msuic and open folder
# buttons = [
#     {'activationType': 'protocol', 'arguments': 'C:\\Users\\adars\\Documents\\music\\That Guy.mp3', 'content': 'Play'},
#     {'activationType': 'protocol', 'arguments': 'file:///C:/Windows/Media', 'content': 'Open Folder'}
# ]
# toast('Music Player', 'Download Finished', buttons=buttons)

# input
# toast('Hello', 'Type anything', input='reply', button='Send')
# {'arguments': 'http:Send', 'user_input': {'reply': 'Hi there'}}

# toast('Hello', 'Type anything', input='reply', button={'activationType': 'protocol', 'arguments': 'http:', 'content': 'Send', 'hint-inputId': 'reply'})
# {'arguments': 'http:', 'user_input': {'reply': 'Hi there'}}

# options in input
# toast('Hello', 'Which do you like?', selection=['Apple', 'Banana', 'Grape'], button='Submit')
# {'arguments': 'dismiss', 'user_input': {'selection': 'Grape'}}

# for just notification


# toast(app_id="adarsh",)
# from time import sleep

# from win11toast import notify
# a = 0
# # while a<1:
# notify('',
#        ' ',
#        app_id='Project Pals',
#        input='', button='Send',
#        icon="C:\\Users\\adars\\Pictures\\Screenshots\\Screenshot 2023-03-28 204407.png")
# # sleep(1)



0


# notify(progress={
#     'title': 'YouTube',
#     'status': 'Downloading...',
#     'value': '0',
#     'valueStringOverride': '0/15 videos'
# })
# for i in range(1, 15+1):
#     sleep(1)
#     update_progress({'value': i/15, 'valueStringOverride': f'{i}/15 videos'})

# update_progress({'status': 'Completed!'})
