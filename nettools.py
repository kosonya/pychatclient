# -coding: utf-8 -*-

import threading
import gobject
import socket
import mytypes

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
                waiter = Waiter(self.chat_area, s, self.queue)
                waiter.start()
                while True:
                    message = self.queue.get()
                    if message.type == "text":
                        s.send(message.content)
                        self.queue.task_done()
                    elif message.type == "command" and message.content == "disconnect":
                        break
                s.close()    
            except Exception as e:
                gobject.idle_add(self.info_print, "Error: " + str(e))
        except Exception as e:
            gobject.idle_add(self.info_print, "Error: " + str(e))
        
        
    def info_print(self, text):
        self.chat_area.add_text(text)
        return False
    
    
class Waiter(threading.Thread):
    def __init__(self, chat_area, s, queue):
        threading.Thread.__init__(self)
        self.s = s
        self.chat_area = chat_area
        self.q = queue

    def info_print(self, text):
        self.chat_area.add_text(text)
        return False
        
    def run(self):
        while True:
            message = self.s.recv(1024)
            if not message:
                break
            gobject.idle_add(self.info_print, message)
        msg = mytypes.Message()
        msg.type = "command"
        msg.content = "disconnect"
        self.q.put(msg)
        gobject.idle_add(self.info_print, "Disconnected")
        
        