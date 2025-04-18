#! /usr/bin/python3

from tkinter import *
from tkinter import messagebox
import os
import sys
import subprocess
from crontab import CronTab
import getpass
import threading
import time

"""############ Variables & Defaults"""

username = getpass.getuser()
EC_IO_FILE = '/sys/kernel/debug/ec/ec0/io'

path_to_script = os.path.dirname(os.path.abspath(__file__))
my_filename = os.path.join(path_to_script, "conf.txt")
check_1 = os.path.exists(my_filename)
if check_1 == False:
	open(my_filename, "w").close()
	subprocess.call(['chmod', '0777', my_filename])
	conf_file = open(my_filename, "w")
	conf_file.write('0')
	conf_file.close()
conf_file_a = open(my_filename, "r")
mode = int(conf_file_a.read(1))
conf_file_a.close()

fm, offset, y = 12, 0, 100
monitoring = 0
temp_c = 0
temp_g = 0
temp_c_m = 100
temp_g_m = 100
ifu = 0
v = []
check = os.path.exists("/etc/modprobe.d/GUI-MSI-DC-L-ec_sys.conf")


def read_EC():
	vr = []
	with open(EC_IO_FILE,'r+b') as file:
		file.seek(0x98)
		if int(file.read(1).hex(),16) == 128:
			file.seek(0x98)
			vr.insert(0, int(file.read(1).hex(),16))
		else:
			file.seek(0xf4)
			vr.insert(0, int(file.read(1).hex(),16))
		file.seek(114)
		vr.insert(1, int(file.read(1).hex(),16))
		file.seek(115)
		vr.insert(2, int(file.read(1).hex(),16))
		file.seek(116)
		vr.insert(3, int(file.read(1).hex(),16))
		file.seek(117)
		vr.insert(4, int(file.read(1).hex(),16))
		file.seek(118)
		vr.insert(5, int(file.read(1).hex(),16))
		file.seek(119)
		vr.insert(6, int(file.read(1).hex(),16))
		file.seek(120)
		vr.insert(7, int(file.read(1).hex(),16))
		file.seek(138)
		vr.insert(8, int(file.read(1).hex(),16))
		file.seek(139)
		vr.insert(9, int(file.read(1).hex(),16))
		file.seek(140)
		vr.insert(10, int(file.read(1).hex(),16))
		file.seek(141)
		vr.insert(11, int(file.read(1).hex(),16))
		file.seek(142)
		vr.insert(12, int(file.read(1).hex(),16))
		file.seek(143)
		vr.insert(13, int(file.read(1).hex(),16))
		file.seek(144)
		vr.insert(14, int(file.read(1).hex(),16))
	return vr
    
def write_EC(v):
	with open(EC_IO_FILE,'w+b') as file:
		if v[0] == 128:
			file.seek(0x98)
			file.write(bytes((128,)))
			file.seek(0xf4)
			file.write(bytes((0,)))
		else:
			file.seek(0x98)
			file.write(bytes((0,)))
			file.seek(0xf4)
			file.write(bytes((v[0],)))
		file.seek(114)
		file.write(bytes((v[1],)))
		file.seek(115)
		file.write(bytes((v[2],)))
		file.seek(116)
		file.write(bytes((v[3],)))
		file.seek(117)
		file.write(bytes((v[4],)))
		file.seek(118)
		file.write(bytes((v[5],)))
		file.seek(119)
		file.write(bytes((v[6],)))
		file.seek(120)
		file.write(bytes((v[7],)))
		file.seek(138)
		file.write(bytes((v[8],)))
		file.seek(139)
		file.write(bytes((v[9],)))
		file.seek(140)
		file.write(bytes((v[10],)))
		file.seek(141)
		file.write(bytes((v[11],)))
		file.seek(142)
		file.write(bytes((v[12],)))
		file.seek(143)
		file.write(bytes((v[13],)))
		file.seek(144)
		file.write(bytes((v[14],)))
	return



"""########################################## Advanced Mode"""

def advanced_on():
	v = []
	v = read_EC()

	vr = [140, 50, 55, 65, 75, 85, 95, 100, 55, 65, 75, 85, 90, 95, 100]
	write_EC(vr)
	return
	
if __name__ == "__main__":
	advanced_on()
