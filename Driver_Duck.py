#!/usr/bin/env python3

'''
    driver_duck.py is a program for reading data streams from drivers.
    Copyright (C) 2017 Zian Smtih     Authors: denkweise9

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see https://www.gnu.org/licenses/.
'''

import subprocess, sys, io, time, os, struct
sysc = subprocess.os.system ; sleep = time.sleep 
encoding = os.device_encoding ; byteio = io.BytesIO
listdir = os.listdir
# obj = byteio(b'data here') ; obj.getvalue() ;
# struct will be used for lower level injections, among other things

#devpath and catpath are both set to None by default, and will just use the path given from the user.
#This can be useful in rare but possible situations.


def driver_duck():
    catpath = None # This is a virtual path that leads to a specific data source.
    devpath = None # This is the directory that may contain one or many places you wish to capture data
    datapath = "/home/driver_duck/"   # This is the directory where the data capture file is saved.
    running = True

    if not (sys.platform.startswith("linux")):
        print("Sorry, but Driver_Duck only works on GNU/Linux for the time being.")
        sleep(2)
    else:
        print("Welcome to Driver_Duck!\n")
        print("Driver_duck is a long term GNU project.")

    def OSRead(path):  #this is not by any means finished
        while True:
            try:
                for each in path:
                    print("The output is: {0},    It's hex value is {1},    It's binary is {2}".format(each_output, hex(each_output), tobinary(each_output)))
            except(KeyboardInterrupt, OSError):
                driver_duck() 


    def listpath(path):
        return listdir(path)

    def path_setup():
        answer = input("Would you like to setup catpath and devpath? y/n: \nYou can set these up later if you choose 'n'\n")
        answer = answer.casefold().strip()
        if answer == 'n':
            pass

        elif answer == 'y':
            catpath = input("Enter the absolute path for catpath\n")
            devpath = input("Enter the absolute path for devpath\n")

        elif answer == 'quit':
            sys.exit()

        else:
            print("Invalid syntax, y or n\n")
            path_setup()

    def tobinary(number):
        number = int(bin(number) [2:])
        return number

    path_setup()

    while running: 
        try:

            print("If you need more information on driver_duck, use 'help' or 'listops'.")
            print("If you need more information on your system for driver_duck, use:\nlistd, dumpkeys, diskstats, cpuinfo, listdr, listpath or show catpath/devpath.")  
            print("If you already know exactly where you need to get your data, you may begin grabbing data with read raw, read binary, read io.")
            print("In rare occasions, you might need the assistence of catpat/devpath when reading. Use 'read custom', which will use both catpath and devpath.")
            print("To quit, simply type 'quit'")
            choice = input("What would you like to do?  \n")
            choice = choice.casefold().strip()

            if choice == "show catpath":
                if catpath != None:
                    print("The catpath currently is: {0}".format(catpath))
                else:
                    print("catpath is None")

            elif choice == 'change catpath':
                if catpath:
                    catpathnew = input("Please enter the directory path to the new value of catpath. Current Value: {0} ".format(catpath))
                    catpath = catpathnew
                    print("Now the catpath is {0}".format(catpath))

                else:
                    answer = input("catpath isn't set. Would you like to set it? y/n\n")
                    answer = answer.casefold().strip()
                    if answer == 'y':
                        catpath = input("Enter the new path for catpath\n")
                        
                    elif answer == 'n':
                        pass
                    else:
                        print("Either you gave invalid input, or an error occured.")
            
            elif choice == 'listdr':
                print(sysc("cat /proc/crypto")) 

            elif choice == 'cpuinfo':
                print(sysc("cat /proc/cpuinfo"))

            elif choice == 'diskstats':
                print(sysc("cat /proc/diskstats"))

            elif choice == "show devpath":
                if not isinstance((devpath), (None)):
                    print("The devpath currently is: {0}".format(devpath))
                else:
                    print("devpath is None")

            elif choice == 'change devpath':
                
                if not isinstance((devpath), (None)):
                    devpathnew = input("Please enter the directory path to the new value of devpath. Current Value: {0} ".format(devpath))
                    devpath = devpathnew
                    print("Now the devpath is {0}".format(devpath))               

                else:
                    answer = input("devpath isn't set. Would you like to set it? y/n")
                    answer = answer.strip().casefold()
                    if answer == 'y':
                        devpath = input("Enter the new path for devpath\n")
                        
                    elif answer == 'n':
                        pass
                    else:
                        print("Either you gave invalid input, or an error occured.")

            elif (choice == 'devinfo') or (choice == 'catinfo'):
                print("If you were using a laptop to read data begin sent to two external devices, catpath and devpath might help")
                print("catpath is where you are reading, devpath is the device that is the source of the data.")
            

            elif choice == None:
                print("parameters for driver_duck are 'quit', 'read', 'listd','listops','change catpath' 'show catpath', or 'help'")  # needs work        
                print("")  
      

            elif choice == 'quit':
                print("Thanks for using driver-duck! Goodbye!\n")
                sys.exit()

            elif choice == 'help':
                sysc('clear')
                # Give basic's and common path locations to users.
                print("Driver_Duck is designed to be able to give the user information on the drivers/protocols being used by their device/s")
                print("parameters for driver_duck are 'read raw', 'read io', 'read binary', 'listd','listops','change catpath' 'show catpath', 'help',")
                print("")
                print("If you need more information on specific commands, type 'listops' which is short for 'list options'")
                # We need to implement the 'write' function. Not included yet
                print("driver_duck can not read from all streams off the bat yet, but does work with some.")
                print("Common paths to devices include:")
                print("/dev/input/mouse0")
                print("/dev/usb/hiddev0")   #improve help for the user.
                print("/dev/video0")



            elif choice == 'listops':
                print("")

                #info on reading commands
                print("'read raw' will just read the input of the device as is.")
                print(" This may not always work as different drivers have different integer bases. Such as binary and hexadecimal.")
                print("'read custom' will allow you to use more customized settings when opening files or streams if you are not familair with python")
                print("'read binary' will use the builtin 'rb' function with python to open the data interpreted as binary.")
                print("This is the most reliable way to read data, and will display the data in three formats:")
                print("Decimal, Hexidecimal, Binary.  This is done to make it easier for you to interpret the data gathered.")        
                #info on system commands
                print("'dumpkeys' will ask the OS you're using to give the data used by the keyboard.")
                print("listd will read /proc/bus/input/devices to find common devices automatically.")
                print("cpuinfo will read /proc/cpuinfo")
                print("listdr will read /proc/crypto, and display the names to some drivers")
                print("diskstats will read /proc/diskstats")
                print("listpath will use os.listdir(path) and tell you all the items in that directory. Useful for finding other paths to find data streams.")
                print("With elevated privlages, you can sometimes find hidden items in a directory.\n")
                #info on driver_duck commands
                print("'pathinfo' or 'devinfo' will give you more information on catpath and devpath\n")
            elif choice == ('pathinfo' or 'devinfo'):       
                #info on catpath/devpath
                print("catpath is the path you specifically read data from, devpath is the device where the data is.")
                print("Suppose you're using a laptop to start reading from a connection on a microcontroller, or a raspberry pi, ")
                print("Using catpath and devpath can help you in reading other devices. If you're just reading mouse drivers on a laptop,")
                print("You probably won't need it.\n")

                print("'show catpath' with show the current file that driver_duck will read to get known devices.")
                print("'change catpath' will change where driver_duck looks to read data.")
                print("'change devpath' will change the directory where driver_duck looks for data.")
                print("'change devpath' will change the value of devpath\n")
                pass
      

            elif choice == 'dumpkeys':
                print(sysc("dumpkeys"))
                print("According to your system, these are the signals used by your keyboard\n")
                pass
                
            
            elif choice == 'listpath':
                path = input("Enter the path to the directory\n")
                listpath(path)
        
            
            
        # This code should help the user find the path to the device/devices available
            elif choice == 'listd':
                print(sysc("cat /proc/bus/input/devices"))   
                print("These are the devices with the handles used that could be found by automatically by driver_duck\n")
                pass
                

        
    
            elif choice == 'read binary':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                print("This will read the data in binary, with no buffering, no encoding.")
                print("If you save the data into a file, it will be written as binary as well")
                path = None; towrite = None;
                while not isinstance((path), (str)) or not isinstance((towrite), (str)):
                    try:
                        path = input('Please enter the path of the device to read from:  \n')
                        towrite = input("Do you want to save the gathered data to a file? y/n ")
                    except(KeyboardInterrupt):
                        sys.exit()

                towrite = towrite.casefold().strip()

                if towrite == 'n':
                    pass
                elif towrite == 'y':
                    file_path = input("Enter the absolute path to the file you want to write to.\n")
                    outputlist = []
                    spacing = 0
                    bytes_received = []
                    bytelist = []
                 
                    driver = io.open(path, 'rb', buffering = 0, encoding = None,)

                    with open(file_path, 'w') as write_file:
                        while True:
                            try:
                                for each_output in driver.read(True):
                                    bytes_received.append(each_output)
                                    outputlist.append(outputlist)
                                    print("The output is: {0},    It's hex value is {1},    It's binary is {2}".format(each_output, hex(each_output), tobinary(each_output)))
                                    #write_file.write(bytes(str(outputlist), 'utf-8'))
                                    write_file.write(str(outputlist))
                                    if len(bytes_received) == 8:
                                        for each_byte in bytes_received:
                                            bytelist.append(each_byte)
                                            spacing += 1
                                            if spacing == 2:
                                                sys.stdout.write('\n')
                                                bytelist.append(' ')
                                                spacing = 0
                                   
                            except(KeyboardInterrupt):
                                write_file.close()
                                sys.exit()
                else:
                    print("Error with checking write option occured")

                spacing = 0
                bytes_received = []
                bytelist = []
                

                driver = io.open(path, 'rb', buffering = 0, encoding = None,)

                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received.append(each_output)
                            print("The output is: {0},    It's hex value is {1},    It's binary is {2}".format(each_output, hex(each_output), tobinary(each_output)))
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    bytelist.append(each_byte)
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        bytelist.append(' ')
                                        spacing = 0
                    except(OSError):
                        print("OSError occured\n")
                        try:
                            OSRead(driver)  #Will make updates later. fails on /dev/video0,  I need to make OSRead()
                        except(OSError):
                            driver_duck()
                    except(FileNotFoundError):
                        file_path = input("Enter the absolute path to the file you want to write to.\n")

                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                     #data.close()
                        driver.close()
                        driver_duck()


            elif choice == 'read custom':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                print("This will read the data in custom settings.")
                print("This opton uses both devpath and catpath")
                if catpath == None:
                    catpath = input('Please enter the path of the data to read from:  \n')
                if devpath == None:
                    devpath = input('Please enter path of the device to read from: \n')
                ls = input("Do you want to view the directory of devpath? yes/no " )
                if str(ls.casefold().strip()) == 'yes':
                    sysc("ls {0}".format(devpath))

                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                print("This will read the data in binary, with no buffering, no encoding.")
                path = None; towrite = None;
                while not isinstance((path), (str)) or not isinstance((towrite), (str)):
                    try:
                        path = input('Please enter the path of the device to read from:  \n')
                        towrite = input("Do you want to save the gathered data to a file? y/n ")
                    except(KeyboardInterrupt):
                        sys.exit()
                towrite = towrite.casefold().strip()
                if towrite == 'n':
                    pass
                elif towrite == 'y':
                    file_path = input("Enter the absolute path to the file you want to write to.\n")

                    spacing = 0
                    bytes_received = []
                    bytelist = []
                  
                    read_settings = input("Enter reading settings, like 'rb'\n")
                    buffering = input("Enter buffering settings, like True, False or None\n")
                    encoding = input("Enter encoding, like 'utf-8' or None\n")
                    driver = io.open(catpath, buffering_setting, encoding)
                    with open(file_path, 'w') as write_file:
                        while True:
                            try:
                                for each_output in driver.read(True):
                                    bytes_received.append(each_output)
                                    outputlist.append(bytes_received)
                                    print("The output is: {0}".format(each_output))
                                    #write_file.write(bytes(str(outputlist), 'utf-8'))
                                    write_file.write(str(outputlist))
                                    if len(bytes_received) == 8:
                                        for each_byte in bytes_received:
                                            bytelist.append(each_byte)
                                            spacing += 1
                                            if spacing == 2:
                                                sys.stdout.write('\n')
                                                bytelist.append(' ')
                                                spacing = 0
                                   
                            except(KeyboardInterrupt):
                                write_file.close()
                                sys.exit()
                else:
                    print("Error with checking write option occured")

                spacing = 0
                bytes_received = []
                bytelist = []
                read_settings = input("Enter reading settings, like 'rb'\n")
                buffering = input("Enter buffering settings, like True, False or None\n")
                encoding = input("Enter encoding, like 'utf-8' or None\n")
                
                driver = io.open(catpath, buffering_setting, encoding)

                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received.append(each_output)
                            print("The output is: {0}".format(each_output))
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    bytelist.append(each_byte)
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        bytelist.append(' ')
                                        spacing = 0

                    except(FileNotFoundError):
                        file_path = input("Enter the absolute path to the file you want to write to.\n")

                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                     #data.close()
                        driver.close()
                        driver_duck()






        

            elif choice == 'read raw':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                print("This will read the data in binary, with no buffering, no encoding.")
                path = None; towrite = None;
                while not isinstance((path), (str)) or not isinstance((towrite), (str)):
                    try:
                        path = input('Please enter the path of the device to read from:  \n')
                        towrite = input("Do you want to save the gathered data to a file? y/n ")
                    except(KeyboardInterrupt):
                        sys.exit()
                towrite = towrite.casefold().strip()
                if towrite == 'n':
                    pass
                elif towrite == 'y':
                    file_path = input("Enter the absolute path to the file you want to write to.\n")

                    with bytes(file_path, 'w') as write_file:
                        while True:
                            try:
                                for each_output in driver.read(True):
                                    bytes_received.append(each_output)
                                    outputlist.append(bytes_received)
                                    print("The output is {0}".format(each_output))
                                    #write_file.write(bytes(str(outputlist), 'utf-8'))
                                    write_file.write(str(outputlist))
                                    if len(bytes_received) == 8:
                                        for each_byte in bytes_received:
                                            bytelist.append(each_byte)
                                            spacing += 1
                                            if spacing == 2:
                                                sys.stdout.write('\n')
                                                bytelist.append(' ')
                                                spacing = 0
                                   
                            except(KeyboardInterrupt):
                                write_file.close()
                                sys.exit()
                else:
                    print("Error with checking write option occured")

                spacing = 0
                bytes_received = []
                bytelist = []
                
                driver = io.open(path, 'r', encoding = None,) # don't use rb

                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received.append(each_output)
                            print("The output is {0}".format(each_output))
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    bytelist.append(each_byte)
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        bytelist.append(' ')
                                        spacing = 0

                    except(FileNotFoundError):
                        file_path = input("Enter the absolute path to the file you want to write to.\n")

                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                     #data.close()
                        driver.close()
                        break
                


        except(KeyboardInterrupt):
            print("Thank you for using GNU driver_duck.py!\n")
            sys.exit()

#New exception for Windows needed here.



#closing
if __name__ == "__main__":
    driver_duck()
