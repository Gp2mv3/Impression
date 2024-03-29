#!/usr/bin/python2.7

import os
import re
import time
import pickle

config = {
    "sleep": 0,
    "refresh-conf": 0,
    "printname": "",
    "verbose": 0,
    }

i = 1

print "Welcome in this small print utility."
print "It checks files in ./files directory to print them (only PDF). After printing, they are moved to the printed directory."
print "To configure this utility you can edit print.conf"

while "a" == "a":
    if i > config['refresh-conf']:
        i = 0
        with open("print.conf", 'rb') as fileC:
            conf = pickle.Unpickler(fileC)
            config = conf.load()
            if config["verbose"]:
                print "Config refreshed: ",config

    files = os.listdir('./files')
    if len(files) > 0:

        if config["verbose"]:
            print "Files found !"
        
        for f in files: 
            found = 0
            path = "./files/"+f
        
            if re.search('.pdf',path) != None:
                cmd = "AcroRd32.exe /t "+path
                found = 1
            elif re.search('.png',path) != None:
                cmd = "i_view32 "+path+" /print"
                found = 1
            elif re.search('.jpg',path) != None:
                cmd = "i_view32 "+path+" /print"
                found = 1

            if found == 1:   
                os.popen(cmd)
                os.rename(path, './printed/'+f)
                
    i = i + 1
    time.sleep(config["sleep"])
