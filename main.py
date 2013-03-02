# -*- coding: utf-8 -*-

import gtk
import simpledialog

class MessageArea(gtk.ScrolledWindow):
    def __init__(self, editable=False):
        gtk.ScrolledWindow.__init__(self)
        
        self.text = ""
        
        self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.textbuffer = gtk.TextBuffer()

        self.textview = gtk.TextView(self.textbuffer)
        self.textview.set_wrap_mode(gtk.WRAP_WORD)
        self.textview.set_editable(False)
        self.add(self.textview)
        
    def set_text(self, text):
        self.textbuffer.set_text(text)
        
    def get_text(self):
        return self.textbuffer.get_text()
    
    def add_text(self, text):
        self.text += '\n' + text
        self.set_text(self.text)

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(300,300)
        self.set_title(u"Наш крутой чат")
        self.mainbox = gtk.VBox()
        self.add(self.mainbox)
        
        self.chat_area = MessageArea(editable = False)
        self.mainbox.pack_start(self.chat_area)
        
        self.settings_button = gtk.Button(u"Настройки")
        self.mainbox.pack_start(self.settings_button)
        self.settings_button.connect("clicked", self.on_settings_button_clicked)
        
        self.connect("destroy", lambda _: gtk.main_quit())
        self.show_all()
        
    def on_settings_button_clicked(self, widget):
        settings_dialog = simpledialog.SettingsDialog()
        response = settings_dialog.run()
        if response == gtk.RESPONSE_OK:
            print settings_dialog.get_ip_port()
            print settings_dialog.get_nick()
            self.chat_area.add_text(settings_dialog.get_ip_port())
            self.chat_area.add_text(settings_dialog.get_nick())

        settings_dialog.destroy()

def main():
    window = MainWindow()
    gtk.main()

if __name__ == "__main__":
    main()