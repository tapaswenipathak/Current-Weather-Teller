from Tkinter import *
import tkMessageBox
import requests
import json
import sys

class App (object):
  def __init__(self):
    self.root = Tk ()
    self.root.geometry ("300x300")
    self.root.wm_title ("Weather")
    self.label = Label (self.root, text= "Enter your city.")
    self.label.pack ()
    self.entrytext = StringVar ()
    Entry(self.root, textvariable = self.entrytext).pack ()
    self.buttontext = StringVar ()
    self.buttontext.set ("Tell me")
    Button(self.root, textvariable = self.buttontext, command = self.clicked1).pack ()
    self.label = Label (self.root, text = "")
    self.label.pack ()
    self.root.mainloop ()
  def clicked1 (self):
    input = str (self.entrytext.get ())

	#Your Location
    location = str (input)

	#Request Open Weather Map API
    r = requests.get ('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&APPID=6666130415ceb458dab7847805deea80')
    
	#Loading JSON
    j = json.loads (r.text)
	
	#Extract the temperature
    temperature = str ( j['main']['temp'] - 273 ) + "C"
    
	#Output
    result = temperature
    self.label.configure (text = result)

  def button_click (self, e):
    pass


	
App ()
