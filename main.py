# -*- coding: utf-8 -*-

import gtk

def main():
    window = gtk.Window()
    window.set_default_size(300,300)
    window.set_name(u"Наш крутой чат")
    window.connect("destroy", lambda _: gtk.main_quit())
    window.show_all()
    gtk.main()

if __name__ == "__main__":
    main()