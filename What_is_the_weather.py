from tkinter import *
from tkinter import messagebox
import requests
import json
import sys

class App (object):
  def __init__(self):
    self.root = Tk ()
    self.root.geometry ("300x200")
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
    try:
    	temperature = str ( j['main']['temp'] - 273 )
    
	#Output
    	result = temperature[0:5]+"C"
    	self.label.configure (text = result)
	#enhancement #ourreviewfeature
    	if float(temperature[0:5])>35.00:
    		messagebox.showinfo("Our review","Its to hot there!!!\n"+result)
    	if float(temperature[0:5])<10.00:
    		messagebox.showinfo("Our review","Its to cold there!!!\n"+result)
    except KeyError:
    	messagebox.showinfo("Sorry","Match for this city not found")
  def button_click (self, e):
    pass


	
App ()
