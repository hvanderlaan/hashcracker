#!/usr/bin/env python

# file     : mkpasswd.py
# purpose  : creating sha512 hashed passwords (like /etc/shadow)
#
# author   : harald van der laan
# date     : 2017/03/02
# version  : v0.0.1
#
# changelog:
# - v0.0.1          initial version                                             (harald)

'''
    mkpasswd.py - python script for creating hashed password (sha512).
    these passwords can be used in /etc/shadow and in the user module of
    Ansible.
'''

# default imports
from __future__ import print_function
import sys
import string
import random
import getpass

# extra imports (use pip to install)
from passlib.hash import sha512_crypt

# define function
def gen_random_salt(charset):
    ''' function for creating a random salt '''
    return ''.join(random.sample(charset*8, 8))

def gen_sha512_hash(password, salt):
    ''' function for creating sha512 password hash '''
    return sha512_crypt.encrypt(password, salt=salt, rounds=5000)

def main():
    ''' main function of this script '''
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
    salt = gen_random_salt(charset)
    password = getpass.getpass('[*] please enter a password: ')
    passwordhash = gen_sha512_hash(password, salt)

    print('hash: {}' .format(passwordhash))

# run the main function
if __name__ == "__main__":
    main()
    sys.exit(0)
