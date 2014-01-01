#!/usr/bin/env python

# -*- coding: utf-8 -*-

# run.py

import wx
#import xbmc_linux_remote
import requests
import json
from websocket import create_connection

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
		result = send_request('Up')
		if result != 'OK':
			print result

	def downButton(self, event):
		result = send_request('Down')
		if result != 'OK':
			print result

	def leftButton(self, event):
		result = send_request('Left')
		if result != 'OK':
			print result

	def rightButton(self, event):
		result = send_request('Right')
		if result != 'OK':
			print result

	def selectButton(self, event):
		result = send_request('Select')
		if result != 'OK':
			print result

	def backButton(self, event):
		result = send_request('Back')
		if result != 'OK':
			print result

def send_request(move):
	headers = {'Content-Type' : 'Contentapplication/json', 'User-Agent' : 'rhys-xbmc-remote'}
	data = {'jsonrpc':'2.0','id': 1}
	data['method'] = 'Input.'+move
	data_json = json.dumps(data)
	
	#websocket method
	#ws = create_connection("ws://192.168.0.4:9090/jsonrpc?request=", headers=headers)
	#ws.send(data_json)
	#response =  ws.recv()

	#http method
	url = 'http://192.168.0.4:10000/jsonrpc?request='
	r = requests.get(url+data_json, headers=headers)
	response = r.content

	rj = json.loads(response)
	#print rj

	if 'error' in rj.keys():
		return(rj['error']['message'])
	else:
		return('OK')

if __name__ == '__main__':
	app = wx.App()
	Interface(None, title='XBMC Remote')
	app.MainLoop()