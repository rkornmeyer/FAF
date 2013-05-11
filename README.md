FAF
===

Firmware Analysis Framework


The framework at the present point will assume that binwalk,firmware-mod-kit and qemu installed and set up properly. This framework will be designed to automate the processes and scripts found here : http://pauldotcom.com/wiki/index.php/EmbeddedDevices  .  It will contain a config file that will contain the location of the firmware you are analyzing and the Firmware mod kit fmk dir location. Once the config file is done, it will take basic numeric input from the command line much like SET. When you choose a process to launch, it will launch a new terminal window to record and copy the data findings.

https://github.com/rkornmeyer/FAF/blob/master/FAF.py

Credits :
Major Credit to Craig Heffner at http://www.devttys0.com/ without his firmware mod kit and binwalk, this framework would not work at all.
Paul Asadoorian for always guiding in the right direction, and his years of wisdom and knowledge in the arena of embedded devices.




Menu



----------------------------

Physical Interrogation

---------------------------

[1] Binwalk Analysis

    -Standard Binwalk Scan: no argument scan for binwalk on firmware

    -Binwalk Filter Scan : Filter out all strings but the one specified

   

[2] Command Line Analysis

    -basic strings analysis : strings -8 firmware.bin  | grep "^/" | less

    -basic typs of grepping for info based on input with grep: grep --binary-files=text -bi "vxworks" ram.bin# grep --binary-files=text -bi -A 50 "password" ram.bin

[3] Extract RootFS -  use firmware mod kit to extract the root file system to the default /fmk dir

[4] Chroot Environment on RootFS - will pop a new terminal to execute chroot commands with qemu

[5] Clean up - removes fmk dir and any temp files binwalk created

----------------------

Network Interrogation

----------------------

-coming soon-

nmap scans

find authentication bypass
