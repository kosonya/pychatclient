# -coding: utf-8 -*-

import threading
import gobject
import socket

class Connecter(threading.Thread):
    def __init__(self, ip_port, chat_area, queue):
        threading.Thread.__init__(self)
        self.chat_area = chat_area
        self.ip_port = ip_port
        self.queue = queue
            
    def run(self):
        #FIXME Не прекращает попытки содениения с сервером при измерении настроек.
        try:
            self.ip, self.port = self.ip_port.split(":")
            self.port = int(self.port)
            try:
                gobject.idle_add(self.info_print, "Trying to connect to " + self.ip + ":"
                             + str(self.port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect( (self.ip, self.port) )
                gobject.idle_add(self.info_print, "Connected to " + self.ip + ":"
                             + str(self.port))
                while True:
                    message = self.queue.get()
                    s.send(message)
                    self.queue.task_done()
                s.close()    
            except Exception as e:
                gobject.idle_add(self.info_print, "Error: " + str(e))
        except Exception as e:
            gobject.idle_add(self.info_print, "Error: " + str(e))
        
        
    def info_print(self, text):
        self.chat_area.add_text(text)
        return False
    