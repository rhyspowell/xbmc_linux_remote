#!/usr/bin/env python

# -*- coding: utf-8 -*-

# run.py

import wx
#import xbmc_linux_remote
import requests
import json

class Interface(wx.Frame):

	def __init__(self, parent, title):
		super(Interface, self).__init__(parent, title=title, size=(250, 250))

		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):

		#menubar = wx.MenuBar()
		#fileMenu = wx.Menu()
		#menubar.Append(fileMenu, '&File')
		#self.SetMenuBar(menubar)


		vbox = wx.BoxSizer(wx.VERTICAL)
		#self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
		#vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
		upButton = wx.Button(self, label='Up')
		upButton.Bind(wx.EVT_BUTTON, self.upButton)
		downButton = wx.Button(self, label='Down')
		downButton.Bind(wx.EVT_BUTTON, self.downButton)
		leftButton = wx.Button(self, label='Left')
		leftButton.Bind(wx.EVT_BUTTON, self.leftButton)
		rightButton = wx.Button(self, label='Right')
		rightButton.Bind(wx.EVT_BUTTON, self.rightButton)
		selectButton = wx.Button(self, label='Select')
		selectButton.Bind(wx.EVT_BUTTON, self.selectButton)
		backButton = wx.Button(self, label='Back')
		backButton.Bind(wx.EVT_BUTTON, self.backButton)

		gs = wx.GridSizer(3, 3, 5, 5)

		gs.AddMany( [(backButton, 0, wx.EXPAND),
			(upButton, 0, wx.EXPAND),
			(wx.StaticText(self), wx.EXPAND),
			(leftButton, 0, wx.EXPAND),
			(selectButton, 0, wx.EXPAND),
			(rightButton, 0, wx.EXPAND),
			(wx.StaticText(self), wx.EXPAND),
			(downButton, 0, wx.EXPAND),
			(wx.StaticText(self), wx.EXPAND) ])

		vbox.Add(gs, proportion=1, flag=wx.EXPAND)
		self.SetSizer(vbox)

		

	def upButton(self, event):
		send_request('Up')

	def downButton(self, event):
		send_request('Down')

	def leftButton(self, event):
		send_request('Left')

	def rightButton(self, event):
		send_request('Right')

	def selectButton(self, event):
		send_request('Select')

	def backButton(self, event):
		send_request('Back')

def send_request(move):
	url = 'http://192.168.0.4:10000/jsonrpc?request='
	headers = {'Content-Type' : 'Contentapplication/json', 'User-Agent' : 'rhys-xbmc-remote'}
	data = {'jsonrpc':'2.0','id': 1}
	data['method'] = 'Input.'+move
	data_json = json.dumps(data)
	#print url+data_json
	r = requests.get(url+data_json, headers=headers)
	#print r.content
	#print r.headers
	if r.status_code != 200:
		return('There has been some kind of issue. Status = '+r.status_code)

if __name__ == '__main__':
	app = wx.App()
	Interface(None, title='XBMC Remote')
	app.MainLoop()