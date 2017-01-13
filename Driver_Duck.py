# Copyright 2017, Zian Smtih
#
# This file is part of driver_duck. A program/project to work with drivers.
#
# driver_duck is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or

# Copyright 2017, Zian Smtih
#
# This file is part of driver_duck. A program/project to work with drivers.
#
# driver_duck is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Driver_Duck is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Affero GNU General Public License for more details.
#
# You should have received a copy of the Affero GNU General Public License
# along with driver_duck.  If not, see <http://www.gnu.org/licenses/>.
#

#driver_duck is a program that was designed to be able to read input from drivers on devices. 
#(And hopefully, if you already know your driver protocol, you can insert input to get a desired effect.
#Driver duck's default settings are to read from binary and without an assumed integer base.
#The goal of Driver duck is to confirm that a device uses a driver protocol, or to reverse engineer driver protocols.
#The goal of Driver duck is to make a program that can pick up data from multiple drivers. 
#It attempts to give out raw data, as well as data converted to an easier to read format. 
#It is NOT desgined to give pretty output, rather, we just want reliable infromation that our driver gives.

# Things that conflict with basic concept of driver_duck:
    
#1) If it assumes a device path, it is wrong.
#2) If it assumes an int base, it is wrong.
#3) If it works with only mouse drivers but not microphone driver inputs, it's wrong (it should be portable with other drivers).
#4) If the capture of original traffic has errors, it's wrong.
#5) If it is incredibly slow, it's wrong.
#6) If the data the user wishes to write to the device is incorrect, it's wrong
#7) If the program damages the drivers or device in any way, it's wrong.
#8) If it utilizes non-gnu software, it's wrong.


import subprocess, sys, io, time; sysc = subprocess.os.system ; sleep = time.sleep ;

def driver_duck():
    catpath = None
    devpath = None

    if sys.platform != 'linux' and 'linux2':
        print("Sorry, but Driver_Duck only works on Linux for the time being.")
        sleep(2)
    else:
        print("Welcome to Driver_Duck!")
        print("\n")


    while True: 
        try:   
            choice = input("What would you like to do? ask help, quit, listd, listops, dumpkeys, change catpath, show catpath, read raw, or read binary? ")
            choice = choice.strip().lower()

            if choice == "show catpath":
                if catpath != None:
                    print("The catpath currently is: {0}".format(catpath))
                else:
                    print("catpath is None")

            elif choice == 'change catpath':
                if catpath == catpath:
                    catpathnew = str(input("Please enter the directory path to the new value of catpath. Current Value: {0} ".format(catpath)))
                    catpath = catpathnew
                    print("Now the catpath is {0}".format(catpath))
                    
               
                else:
                    answer = input("catpath isn't set. Would you like to set it? y/n")
                    answer = answer.strip().lower()
                    if answer == 'y':
                        catpath = str(input("Enter the new path for catpath"))  
                        
                    elif answer == 'n':
                        pass
                    else:
                        print("Either you gave invalid input, or an error occured.")
             
             

            elif choice == None:
                print("parameters for driver_duck are 'quit', 'read', 'listd','listops','change catpath' 'show catpath', or 'help'")  # needs work        
                print("")  
      

            elif choice == 'quit':
                print("Thanks for using driver-duck! Goodbye!")
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
                print("You can alter this path by changing the value of CATPATH.")
                print("'change_path' or 'change path' will both open up a input section for you to change the value of CATPATH")
                print("'read raw' will just read the input of the device as is. This may not always work.")
                print("'read binary' will use the builtin 'rb' function with python to open the data as binary. This does not mean your data will be in all '10101's.")
                print("'dumpkeys' will ask the OS you're using to give the data used by the keyboard.")
                print("'show catpath' with show the current file that driver_duck will read to get known devices.")
                print("'change catpath' will change where driver_duck looks for known devices")
                print("")
      

            elif choice == 'dumpkeys':
                print(sysc("dumpkeys"))
                print("According to your system, these are the signals used by your keyboard")
                pass
                
            

        
            
            
        # This code should help the user find the path to the device/devices available
            elif choice == 'listd':
                print(sysc("cat /proc/bus/input/devices"))   
                print("These are the devices with the handles used that could be found by automatically by Driver_duck")
                

        
    
            elif choice == 'read binary':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                path = input('Please enter the path of the device to read from:  ')
                spacing = 0
                bytes_received = []
                driver = open('{0}'.format(path),'rb')
       
                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received += [each_output]
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    sys.stdout.write(str(each_byte))
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        spacing = 0
                        stuff = sys.stdout.write(repr(each_output))
                    #output = hex(stuff)
                        print("The current bytes_received are {0}".format(bytes_received))
                        print("The current data given from each_output is ".format(each_output))
                    #data.write(str(stuff))
                        sys.stdout.write('\n')
                        sys.stdout.flush()
       
                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                    #data.close()
                        driver.close()
                        break
        

            elif choice == 'read raw':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                path = input('Please enter the path of the device to read from:  ')
                spacing = 0
                bytes_received = []
                driver = open('{0}'.format(path),'rb', buffering = 0)  #raw io buffering used.
       
                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received += [each_output]
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    sys.stdout.write(str(each_byte))
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        spacing = 0
                        stuff = sys.stdout.write(repr(each_output))
                    #output = hex(stuff)
                        print("The current bytes_received are {0}".format(bytes_received))
                        print("The current data given from each_output is ".format(each_output))
                    #data.write(str(stuff))
                        sys.stdout.write('\n')
                        sys.stdout.flush()
       
                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                     #data.close()
                        driver.close()
                        break

#this read io needs work, with a 'read io bytes' option added.
            elif choice == 'read io':
                print("Once driver_duck starts reading, it will keep reading until given a keyboard interrupt, or Ctrl+C")
                path = input('Please enter the path of the device to read from:  ')
                spacing = 0
                bytes_received = []
                driver = io.open('{0}'.format(path),'rb', buffering = 0, encoding = None,)  #raw io buffering used.
       
                while True:
                    try:
                        for each_output in driver.read(True):
                            bytes_received += [each_output]
                            if len(bytes_received) == 8:
                                for each_byte in bytes_received:
                                    sys.stdout.write(str(each_byte))
                                    spacing += 1
                                    if spacing == 2:
                                        sys.stdout.write('\n')
                                        spacing = 0
                        stuff = sys.stdout.write(repr(each_output))
                    #output = hex(stuff)
                        print("The current bytes_received are {0}".format(bytes_received))
                        print("The current data given from each_output is ".format(each_output))
                    #data.write(str(stuff))
                        sys.stdout.write('\n')
                        sys.stdout.flush()
       
                    except(KeyboardInterrupt, EOFError, UnboundLocalError):
                        print("Encountered a KeyboardInterrupt, UnboundLocalError or a EOFError")
                     #data.close()
                        driver.close()
                        break
            else:
                print("I'm sorry. Either you gave invalid input or an Internal Error has occured.")

        except(KeyboardInterrupt, EOFError, UnboundLocalError):
            break
            sys.exit()







#closing
if __name__ == "__main__":
    driver_duck()
