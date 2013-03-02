# -*- coding: utf-8 -*-

import gtk

#label = gtk.Label("Nice label")


dialog = gtk.Dialog(u"Настройки",
                   None,
                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                   (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT,
                    gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))

ip_port_label = gtk.Label(u"IP:порт сервера")
ip_port_entry = gtk.Entry()
nick_label = gtk.Label(u"Ник в чате")
nick_entry = gtk.Entry()

labels_box = gtk.VBox()
labels_box.pack_start(ip_port_label)
labels_box.pack_start(nick_label)

entry_box = gtk.VBox()
entry_box.pack_start(ip_port_entry)
entry_box.pack_start(nick_entry)

main_hbox = gtk.HBox()
main_hbox.pack_start(labels_box)
main_hbox.pack_start(entry_box)

dialog.vbox.pack_start(main_hbox)

#ip_port_hbox = gtk.HBox()
#ip_port_hbox.pack_start(ip_port_label)
#ip_port_hbox.pack_start(ip_port_entry)

#nick_hbox = gtk.HBox()
#nick_hbox.pack_start(nick_label)
#nick_hbox.pack_start(nick_entry)

#dialog.vbox.pack_start(ip_port_hbox)
#dialog.vbox.pack_start(nick_hbox)


dialog.show_all()
response = dialog.run()
dialog.destroy()