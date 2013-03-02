# -*- coding: utf-8 -*-

import gtk
import simpledialog

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(300,300)
        self.set_name(u"Наш крутой чат")
        self.mainbox = gtk.VBox()
        self.add(self.mainbox)
        
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
        settings_dialog.destroy()

def main():
    window = MainWindow()
    gtk.main()

if __name__ == "__main__":
    main()