from os import system

system('touch ~/lanLog.txt')

system('nmap -sn 192.168.1.* < ~/lanLog.txt')
