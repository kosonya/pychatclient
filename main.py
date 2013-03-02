# -*- coding: utf-8 -*-

import gtk
import simpledialog
import os
import gobject
import nettools
import Queue

class MessageArea(gtk.ScrolledWindow):
    def __init__(self, editable=False):
        gtk.ScrolledWindow.__init__(self)
        
        self.text = ""
        
        self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.textbuffer = gtk.TextBuffer()

        self.textview = gtk.TextView(self.textbuffer)
        self.textview.set_wrap_mode(gtk.WRAP_WORD)
        self.textview.set_editable(editable)
        self.textview.connect('size-allocate', self.on_size_changed)
        self.add(self.textview)
        
    def on_size_changed(self, widget, event, data=None):
        adj = self.get_vadjustment()
        adj.set_value( adj.upper - adj.page_size )
        
    def set_text(self, text):
        self.textbuffer.set_text(text)
        
    def get_text(self):
        start, end = self.textbuffer.get_bounds()
        return self.textbuffer.get_text(start, end)
    
    def add_text(self, text):
        self.text += '\n' + text
        self.set_text(self.text)

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(400,500)
        self.set_title(u"Наш крутой чат")
        self.mainbox = gtk.VBox()
        self.add(self.mainbox)
        
        self.chat_area = MessageArea(editable = False)
        self.mainbox.pack_start(self.chat_area)
        
        self.input_area = MessageArea(editable = True)
        self.mainbox.pack_start(self.input_area, padding = 10)
        
        self.buttons_box = gtk.HBox()
        
        self.settings_button = gtk.Button(u"Настройки")
        self.buttons_box.pack_start(self.settings_button, padding = 10, fill = False)
        self.settings_button.connect("clicked", self.on_settings_button_clicked)
  
        self.send_button = gtk.Button(u"Отправить")
        self.buttons_box.pack_start(self.send_button, padding = 10, fill = False)
        self.send_button.connect("clicked", self.on_send_button_clicked)

        self.mainbox.pack_start(self.buttons_box, padding = 10, fill = False)

        self.connect("destroy", lambda _: gtk.main_quit())
        self.show_all()
        
        if os.path.exists("./settings.txt"):
            f = open("settings.txt", "r")
            lines = f.readlines()
            f.close()
            if len(lines) != 2:
                settings_exist = False
            else:
                settings_exist = True
        else:
            settings_exist = False

        
        if not settings_exist:
            self.chat_area.add_text(u"Нет сохранённых настроек. Надо бы настроить.")
        else:
            self.ip_port = lines[0][:-1]
            self.nick = lines[1][:-1]
            self.chat_area.add_text(u'Прочитали из настроек сервер: ' + self.ip_port)
            self.chat_area.add_text(u'Прочитали из настроек ник: ' + self.nick)
            self.connect_to_server()
            
        
    def on_settings_button_clicked(self, widget):
        settings_dialog = simpledialog.SettingsDialog()
        response = settings_dialog.run()
        if response == gtk.RESPONSE_OK:
            self.ip_port = settings_dialog.get_ip_port()
            self.nick = settings_dialog.get_nick()
            self.chat_area.add_text(u"Настроен сервер: " + self.ip_port)
            self.chat_area.add_text(u"Настроен ник: " + self.nick)
            f = open("settings.txt", "w")
            f.write(self.ip_port + '\n')
            f.write(self.nick + '\n')
            f.close()
            self.connect_to_server()          
        settings_dialog.destroy()

    def on_send_button_clicked(self, widget):
        message = self.input_area.get_text()
        self.input_area.set_text("")
        self.queue.put(message)

    def connect_to_server(self):
        self.queue = Queue.Queue()
        connecter = nettools.Connecter(self.ip_port, self.chat_area, self.queue)
        connecter.start()

def main():
    gobject.threads_init()
    window = MainWindow()
    gtk.main()

if __name__ == "__main__":
    main()