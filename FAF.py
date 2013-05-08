#!/usr/bin/python
import os
import sys
import pprint
import subprocess
from binwalk import Binwalk

# check where we are
#if os.path.isdir("/usr/share/setoolkit"):
#	#if not os.path.isfile("se-toolkit"):
#		#os.chdir("/usr/share/setoolkit")
#
#check where we are and load default directory
#if os.path.isdir("/usr/share/set"):
# #   #if not os.path.isfile("se-toolkit"):
# #      #os.chdir("/usr/share/set")
#   #     #sys.path.append("/usr/share/set")


print '''
#########################################
# The Firmware Analysis Framework       #
# Written by: Robert Kornmeyer          #
#         !!!MUST RUN AS ROOT!!!        #
#########################################
'''
# this is the main menu structure for FAF

# main menu

# grab the operating system
path_to_firmware = raw_input('Enter the path to firmware: ')


def main_Menu():
    print '\n[1] Binwalk Scans\n'
    print '\n[2] Command Line Analysis\n'
    print '\n[3] File System Manipulation\n'
    print '\n       \n'
    print '\n  99) Exit the Firmware Analysis Framework\n'
    main_menu_choice = (raw_input('Enter Menu Choice: '))
    return main_menu_choice


while 1:
    main_menu_choice = main_Menu()
    if main_menu_choice == 'exit' or main_menu_choice == "99" or main_menu_choice == "quit":
        sys.exit()
    if main_menu_choice == '1':
        print '\n [1]Normal Binwalk Scan'
        print '\n [2]Filtered Binwalk Scan'
        print '\n [99] Main Menu'
        sub_menu_choice = (raw_input('Enter Choice: '))
        if sub_menu_choice == '1':
            with Binwalk() as bw:
                pprint.PrettyPrinter().pprint(bw.scan(path_to_firmware))
                main_Menu()
        elif sub_menu_choice == '2':
            with Binwalk() as binwalk:
                binwalk.filter.include(raw_input('Enter Filter to search: '))
                print (binwalk.scan(path_to_firmware))
                main_Menu()
        elif sub_menu_choice == '99':
            main_Menu()
            print "No choices entered going back to main menu!"
            main_Menu()
    if main_menu_choice == '2':
        print '\n[1] Basic Analysis: Strings\n'
        print '\n[2] Grep Analysis\n'
        sub_menu_choice = (raw_input('Enter Choice: '))
        if sub_menu_choice == '1':
            string_to_search = raw_input('What string to search for?')
            subprocess.call("strings -8 " + path_to_firmware + " | grep " + string_to_search + " | less", shell=True)
        if sub_menu_choice == '2':
            string_to_search = raw_input('What string to search for?')
            subprocess.call("grep --binary-files=text -bi " + string_to_search + ' ' + path_to_firmware, shell=True)
##third party modules
if main_menu_choice == '3':
        print '\n[1] Mod Kit Extraction\n'
        print '\n[2] Chroot into RootFS\n'
        sub_menu_choice = (raw_input('Enter Choice: '))
        if sub_menu_choice == '1':

            subprocess.call()

        if sub_menu_choice == '2':
            subprocess.call("grep --binary-files=text -bi " + string_to_search + ' ' + path_to_firmware, shell=True)


##update metasploit
#if main_menu_choice == '4':

#update set
#if main_menu_choice == '5':


#credits
#if main_menu_choice == '6':


##update config
##if main_menu_choice == '7#