#!/usr/bin
import os
from time import sleep

os.system("clear")
try:
    color = {"red":'\033[1;31m', "cyan":'\033[1;36m', "end":'\033[m'}
        
    
    def lin():
        print('{}={}'.format(color["cyan"], color["end"]) * 77)
        
    
    def author():
        print('Creat by {}Crazy{}!'.format(color["red"], color["end"]))
      
        
    def time1():
        print('5')
        sleep(1)
        print('4')
        sleep(1)
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
            
    
      
    def menu():
        print("""
        [0] Exit.
        [1] Install the Metasploit and execult.
         """)
         
                 
    lin()
    print("""
     ___  ___ _____  _____   ___           _____ ______   ___   ________   __
     |  \/  ||  ___||_   _| / _ \         /  __ \| ___ \ / _ \ |___  /\ \ / /
     | .  . || |__    | |  / /_\ \        | /  \/| |_/ // /_\ \   / /  \ V / 
     | |\/| ||  __|   | |  |  _  |        | |    |    / |  _  |  / /    \ /  
     | |  | || |___   | |  | | | |        | \__/\| |\ \ | | | |./ /___  | |  
     \_|  |_/\____/   \_/  \_| |_/         \____/\_| \_|\_| |_/\_____/  \_/  
                                   ______                                    
                                  |______|                                   """)
    lin()
    author()
  
    menu()
    
    option = int(input('What do you want? '))
    
    if option == 1:
        try:
            print('the installation will start in 5 seconds...')
            sleep(5)
            os.system("pkg install unstable-repo ; pkg install metasploit")
            print('\nMetasploit successfully installed!')
            sleep(3)
            print('starting metasploit in ...')
            sleep(1)
            time1()
            print('starting...')
            sleep(1)
        except:
            print("{}erro{}!".format(color["red"], color["end"]))
        else:
            os.system("msfconsole")
    else:
        exit()
except:
    print("{}Saindo...{}".format(color["red"], color["end"])) 
       
