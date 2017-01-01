# Copyright 2017, Zian Smtih
#
# This file is part of Driver_Duck. A program/project to work with drivers.
#
# Sloth is free software: you can redistribute it and/or modify
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
# along with Sloth.  If not, see <http://www.gnu.org/licenses/>.
#Driver duck is a program that was designed to be able to read input from drivers. 
#(And hopefully, if you already know your driver protocol, you can insert input to get a desired effect.
#Driver duck's default settings are to read from binary and without an assumed integer base.
#The goal of Driver duck is to confirm that a device uses a driver protocol, or to reverse engineer driver protocols.
#The goal of Driver duck is to make a program that can pick up data from multiple drivers. 
#It attempts to give out raw data, as well as data converted to an easier to read format. 
#It is NOT desgined to give pretty output, rather, we just want reliable infromation that our driver gives.

# Things that conflict with basic concept of Driver duck:
    
#1) If it assumes a device path, it is wrong.
#2) If it assumes an int base, it is wrong.
#3) If it works with only mouse drivers but not microphone driver inputs, it's wrong (it should be portable with other drivers).
#4) If the capture of original traffic has errors, it's wrong.
#5) If it is incredibly slow, it's wrong.
#6) If the data the user wishes to write to the device is incorrect, it's wrong
#7) If the program damages the drivers or device in any way, it's wrong.



#Please take note that this program is not done by any means.  However, it does currently offer capabilites as a tool.
#If you wish to contribute either code, time or knowledge, your efforts are valued as gold.





def driver_duck():
    print("If you need help with driver__duck then type 'help'.")
    choice = input("What would you like to do? list, write, dumpkeys, or read? ")

    if choice == None:
        print("parameters for driver_duck is 'read', 'list' or 'write'")  # needs work 
    choice = choice.strip().lower()
    #data = while open('/home/usr/Desktop/data.txt','w')
   

    if choice == 'help':
        print("Driver_Duck is designed to be able to give the user information on the drivers/protocols being used by their device/s")
        print("")   #improve help for the user.

    if choice == 'dumpkeys':
        if sys.platform == 'linux':
            sysc("dumpkeys")
            print("According to your system, these are the signals used by your keyboard")
        else:
            print("Sorry, currently 'dumpkeys' is only available on Linux Machines")
    
    if choice == 'list':
        sysc("cat /proc/bus/input/devices")   # This line should help the user find the path to the device, and devices available
        print(" These are the devices with the handles used that could be found by Driver_duck")
        
    
    if choice == 'read':
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
                sys.exit()

# below is all a prototype and not yet finished
'''
    if choice == 'write':
        path = input('Please enter the path to the device to write input to:  ')
        driver = open('{0}'.format(path),'wb')
        
        while True:
            try:
                driver.write(input())    #            
                
            except(KeyboardInterrupt):
                sys.exit()


'''
