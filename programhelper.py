import PySimpleGUI as psg
import cv2 as cv
import numpy as np
import vlc
from sys import platform as PLATFORM

def blank_frame():
    return psg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)\

def btn(name):  # a PySimpleGUI "User Defined Element" (see docs)
  return psg.Button(name, size=(6, 1), pad=(1, 1))

layout_frame1 = [
  [blank_frame()]
]

class eventHandler:
  def handle_event(self, event, values):
    if event == 'Play':
      self.list_player.play()
    elif event == 'Pause':
      self.list_player.pause()
    elif event == 'Stop':
      self.list_player.stop()
    elif event == 'Next':
      self.list_player.next()
      self.list_player.play()
    elif event == 'Previous':
      self.list_player.previous()
      self.list_player.previous()
      self.list_player.play()
    elif event == 'Load':
      if values['-VIDEO_LOCATION-'] and 'Video URL' not in values['-VIDEO_LOCATION-']:
        self.media_list.add_media(values['-VIDEO_LOCATION-'])
        self.list_player.set_media_list(self.media_list)
        self.window['-VIDEO_LOCATION-'].update('Video URL or Local Path:')

