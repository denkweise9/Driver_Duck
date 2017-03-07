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

import subprocess, sys, io, time, os; 
sysc = subprocess.os.system ; sleep = time.sleep ; 
encoding = os.device_encoding ; byteio = io.BytesIO
# obj = byteio(b'data here') ; obj.getvalue() ;

#devpath and catpath are both set to None by default, and will just use the path given from the user.
#This can be useful but in rare but possible situations.


def driver_duck():
    catpath = None # This is a virtual path that leads to a specific data source.
    devpath = None # This is the directory that may contain one or many places you wish to capture data
    datapath = "/home/driver_duck/"   # This is the directory where the data capture file is saved.
    running = True
    print("Driver_duck is a long term project.") 
    if not (sys.platform.startswith("linux")):
        print("Sorry, but Driver_Duck only works on Linux for the time being.")
        sleep(2)
    else:
        print("Welcome to Driver_Duck!\n")
        print("Driver_duck is a long term GNU project.")

    path_setup()

    while running: 
        try:

            print("If you need more information on driver_duck, use 'help' or 'listops'.")
            print("If you need more information on your system for driver_duck, use listd, dumpkeys, or show catpath/devpath.")  
            print("If you already know exactly where you need to get your data, you may begin grabbing data with read raw, read binary, read io.")
            print("In rare occasions, you might need the assistence of catpat/devpath when reading. Use 'read custom', which will use both catpath and devpath.")
            choice = input("What would you like to do?  \n")
            choice = choice.casefold().strip()

            if choice == "show catpath":
                if catpath != None:
                    print("The catpath currently is: {0}".format(catpath))
                else:
                    print("catpath is None")

            elif choice == 'change catpath':
                if catpath == catpath:
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
                    devpathnew = input("Please enter the directory path to the new value of devpath.\n")
                    devpath = devpathnew
                    print("Now the devpath is {0}".format(devpath))
               

                else:
                    answer = input("devpath isn't set. Would you like to set it? y/n")
                    answer = answer.strip().casefold()
                    if answer == 'y':
                        devpath = input("Enter the new path for devpath")
                        
                    elif answer == 'n':
                        pass
                    else:
                        print("Either you gave invalid input, or an error occured.")


            elif choice == None:
                print("parameters for driver_duck are 'quit', 'read', 'listd','listops','change catpath' 'show catpath', or 'help'")  # needs work        
                print("")  
      

            elif choice == 'quit':
                print("Thanks for using driver-duck! Goodbye!\n")
                break
            

            elif choice == 'help':
        #Give basic's and common path locations to users.
                print("Driver_Duck is designed to be able to give the user information on the drivers/protocols being used by their device/s")
                print("parameters for driver_duck are 'read raw', 'read io', 'read binary', 'listd','listops','change catpath' 'show catpath', 'help',")
                print("")
                print("If you need more information on specific commands, type 'listops' which is short for 'list options'")
 #  We need to implement the 'write' function. Not included yet
                print("")
                print("Common paths to devices include:")
                print("/dev/input/mouse0")
                print("/dev/usb/hiddev0")   #improve help for the user.
                print("")



            elif choice == 'listops':
                print("listd will read /proc/bus/input/devices to find common devices automatically.")
                print("")
                
                print("'read raw' will just read the input of the device as is. This may not always work.")
                print("'read binary' will use the builtin 'rb' function with python to open the data as binary. This does not mean your data will be in all '10101's.")
                print("'dumpkeys' will ask the OS you're using to give the data used by the keyboard.")
                print("'show catpath' with show the current file that driver_duck will read to get known devices.")
                print("'change catpath' will change where driver_duck looks to read data.")
                print("'change devpath' will change the directory where driver_duck looks for data.")
                print("'change devpath' will change the value of devpath\n")
                pass
      

            elif choice == 'dumpkeys':
                print(sysc("dumpkeys"))
                print("According to your system, these are the signals used by your keyboard\n")
                pass
                
            

        
            
            
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
                
                driver = io.open(path, 'rb', buffering = 0, encoding = None,)

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
                read_settings = input("Enter reading settings, like 'rb'\n")
                buffering = input("Enter buffering settings, like True, False or None\n")
                encoding = input("Enter encoding, like 'utf-8' or None\n")
                
                driver = io.open(catpath, buffering_setting, encoding)

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








def path_setup():
    answer = input("Would you like to setup catpath and devpath? y/n: \nYou can set these up later if you choose 'n'\n")
    answer = answer.casefold().strip()
    if answer == 'n':
        pass
    elif answer == 'y':
        catpath = input("Enter the absolute path for catpath\n")
        devpath = input("Enter the absolute path for devpath\n")
    else:
        print("Invalid syntax, y or n\n")
        path_setup()
#New exception for Windows needed here.



#closing
if __name__ == "__main__":
    driver_duck()
