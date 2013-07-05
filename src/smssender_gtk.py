#! /usr/bin/env python
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- #!/usr/bin/python
#
# main.py
# Copyright (C) 2013 Polonkai Gergely <gergely@polonkai.eu>
# 
# smssender-gtk is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# smssender-gtk is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys, json, urllib, httplib


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/smssender_gtk.ui"
#UI_FILE = "/usr/local/share/smssender_gtk/ui/smssender_gtk.ui"


class GUI:
	def __init__(self):

		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')

		window.show_all()

	def destroy(window, self):
		Gtk.main_quit()

	def send_button_clicked_cb(self, button):
		url = self.builder.get_object('url_entry').get_text()
		username = self.builder.get_object('username_entry').get_text()
		password = self.builder.get_object('password_entry').get_text()
		rcpt = self.builder.get_object('recipient_entry').get_text()
		
		messageBuffer = self.builder.get_object('message_text').get_buffer()
		message = messageBuffer.get_text(messageBuffer.get_start_iter(), messageBuffer.get_end_iter(), True)

		rpc = json.dumps({"id": 1, "method": "login", "params": [ username, password ] })

		headers = {"Content-Type": "application/json", "Accept": "application/json", "Content-Encoding": "utf-8"}
		conn = httplib.HTTPConnection("localhost", 80)
		conn.request("POST", url, rpc, headers)
		response = json.loads(conn.getresponse().read())

		token = response['result']

		rpc = json.dumps({"id": 2, "method": "send", "params": [token, rcpt, message, []]})

		conn.request("POST", url, rpc, headers)
		print conn.getresponse().read()
def main():
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
	sys.exit(main())

