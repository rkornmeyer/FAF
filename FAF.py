#!/usr/bin/python
import os
import sys
import pprint
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
    print '\n       \n'
    print '\n       \n'
    print '\n       \n'
    print '\n  99) Exit the Firmware Analysis Framework\n'

# main menu
    main_menu_choice = (raw_input('Enter Menu Choice: '))
    return main_menu_choice


main_menu_choice = main_Menu()
# funny
if main_menu_choice == "hugs":
    print "Have you given someone a hug today? Remember a hug can change the world."
    pause = raw_input("\nPlease give someone a hug then press {return} to continue.")

# quit out
if main_menu_choice == 'exit' or main_menu_choice == "99" or main_menu_choice == "quit":
    sys.exit()


    # load FAF
if main_menu_choice == '1':
    print '\n [1]Normal Binwalk Scan'
    print '\n [2]Filtered Binwalk Scan'
    sub_menu_choice = (raw_input('Enter Choice: '))
    if sub_menu_choice == '1':
        with Binwalk() as bw:
            pprint.PrettyPrinter().pprint(bw.scan(path_to_firmware))
    elif sub_menu_choice == '2':
        binwalk = Binwalk()
        binwalk.filter.include(raw_input('Enter Filter to search: '))
        binwalk.scan(path_to_firmware)
        binwalk.cleanup()
    else:
        print "No choices entered going back to main menu!"
        main_Menu()


#load fasttrack
#if main_menu_choice == '2':


##third party modules
#if main_menu_choice == '3':

##update metasploit
#if main_menu_choice == '4':

#update set
#if main_menu_choice == '5':


#credits
#if main_menu_choice == '6':


##update config
##if main_menu_choice == '7#