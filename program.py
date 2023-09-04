import PySimpleGUI as psg
import cv2 as cv
import numpy as np
import vlc
from sys import platform as PLATFORM
import programhelper
import mp4class

psg.theme('darkgray12')
psg.set_options(font=("Arial Bold", 14))
colors = (psg.theme_background_color(), psg.theme_background_color())

#display(IFrame(r'C:\Medal\Clips\League of Legends\MedalTVLeagueofLegends20230417154836.mp4', '100%', '600px'))

layout = [
  [psg.Input(default_text='Video URL or Local Path (no quotes):', size=(30, 1), key='-VIDEO_LOCATION-'), psg.Button('load')],
  [psg.Image('', size=(300, 170), key='-VID_OUT-')],
  [programhelper.btn('previous'), programhelper.btn('play'), programhelper.btn('next'), programhelper.btn('pause'), programhelper.btn('stop')],
  [psg.Text('Load media to start', key='-MESSAGE_AREA-')]
]

window = psg.Window('Mini Player', layout, element_justification='center', finalize=True, resizable=True)
window['-VID_OUT-'].expand(True, True)                # type: sg.Element


#window = psg.Window('Form', layout, size=(715,400))

inst = vlc.Instance()
list_player = inst.media_list_player_new()
media_list = inst.media_list_new([])
list_player.set_media_list(media_list)
player = list_player.get_media_player()
if PLATFORM.startswith('linux'):
    player.set_xwindow(window['-VID_OUT-'].Widget.winfo_id())
else:
    player.set_hwnd(window['-VID_OUT-'].Widget.winfo_id())


while True:
  event, values = window.read(timeout=1000)
  print (event, values)

  if event == psg.WIN_CLOSED:
     break
  if event == 'play':
        list_player.play()
  if event == 'pause':
        list_player.pause()
  if event == 'stop':
        list_player.stop()
  if event == 'next':
        list_player.next()
        list_player.play()
  if event == 'previous':
        list_player.previous()      # first call causes current video to start over
        list_player.previous()      # second call moves back 1 video from current
        list_player.play()
  if event == 'load':
    if values['-VIDEO_LOCATION-'] and not 'Video URL' in values['-VIDEO_LOCATION-']:
        media_list.add_media(values['-VIDEO_LOCATION-'])
        list_player.set_media_list(media_list)
        window['-VIDEO_LOCATION-'].update('Video URL or Local Path:') # only add a legit submit

    # update elapsed time if there is a video loaded and the player is playing
  if player.is_playing():
    print('is playing')
    window['-MESSAGE_AREA-'].update("{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(player.get_time()//1000, 60),*divmod(player.get_length()//1000, 60)))
  else:
    window['-MESSAGE_AREA-'].update('Load media to start' if media_list.count() == 0 else 'Ready to play media' )
 
  cap = cv.VideoCapture(r"C:\Users\Tailer\source\repos\teamfight-helper\clips\clip1.mp4")
  if (cap.isOpened()== False): 
    print("didn't open")
    break
  else:
     print('opened')

  if event == psg.WIN_CLOSED or event == 'Exit':
    break
window.close()
