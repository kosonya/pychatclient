# -*- coding: utf-8 -*-

import gtk

#label = gtk.Label("Nice label")

class SettingsDialog(gtk.Dialog):
    def __init__(self, ip_port = "", nick = ""):
        gtk.Dialog.__init__(self, u"Настройки",
                   None,
                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                   (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                    gtk.STOCK_OK, gtk.RESPONSE_OK))

        self.ip_port_label = gtk.Label(u"IP:порт сервера")
        self.ip_port_entry = gtk.Entry()
        self.ip_port_entry.set_text(ip_port)
        self.nick_label = gtk.Label(u"Ник в чате")
        self.nick_entry = gtk.Entry()
        self.nick_entry.set_text(nick)
        
        self.labels_box = gtk.VBox()
        self.labels_box.pack_start(self.ip_port_label)
        self.labels_box.pack_start(self.nick_label)
        
        self.entry_box = gtk.VBox()
        self.entry_box.pack_start(self.ip_port_entry)
        self.entry_box.pack_start(self.nick_entry)
        
        self.main_hbox = gtk.HBox()
        self.main_hbox.pack_start(self.labels_box)
        self.main_hbox.pack_start(self.entry_box)
        
        self.vbox.pack_start(self.main_hbox)
        
        self.show_all()
        
    def get_ip_port(self):
        return self.ip_port_entry.get_text()
    
    def get_nick(self):
        return self.nick_entry.get_text()
    
def main():
    dialog = SettingsDialog("8.8.8.8:31415", "etomoynick")
    response = dialog.run()
    print response
    if response == gtk.RESPONSE_OK:
        print dialog.get_ip_port()
        print dialog.get_nick()
    dialog.destroy()
    
if __name__ == "__main__":
    main() 