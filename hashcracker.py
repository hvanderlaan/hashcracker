#!/usr/bin/env python

# file     : hashcracker.py
# purpose  : brute-force sha512 hashed passwords
#
# author   : harald van der laan
# date     : 2017/03/03
# version  : v1.0.0
#
# changelog:
# - v1.0.0          multiprocessing for speedup brute-force         (harald)
# - <= v0.9.9       Initial version                                 (harald)
#
# Legal    :
# this script is for educational pruposes only, use of this script is in some
# parts of the world illegal. the author of this script is in no way responsible
# for the action of the user of this script.

''' hashcracker.py - brute-force sha512 hashed passwords '''

# import modules
from __future__ import print_function           # required for print()
import sys                                      # required for sys action
import os                                       # required for os actions
import time                                     # required for time calculation
from multiprocessing import Pool                # required for multithreating

from passlib.hash import sha512_crypt           # required for sha512 hashes

# displat banner
print('#####################################################################')
print('# hashcracker.py - brute-force the shit out sha512 hashed passwords #')
print('#                                                                   #')
print('#        FOR EDUCATIONAL PURPOSES ONLY, THIS COULD BE ILLEGAL       #')
print('#####################################################################\n')

# global variables that are used in functions and in the main script
ORIGINHASH = raw_input('enter sha512 hash: ')
DICTIONARY = raw_input('enter dict file  : ')
STARTTIME = int(time.time())

# functions
def brute_force_hash(password):
    ''' function for brute-forcing the sha512 hash '''
    # dictionary file has newlines at the end of the line, we need to strip them
    password = password.strip('\n')
    # sha512 password hashes have a salt $6$<salt>$<sha512 hash>, lets get this salt
    salt = ORIGINHASH.split('$')[2]
    # create a new hash with salt and password provided by password and salt
    newhash = sha512_crypt.encrypt(password, salt=salt, rounds=5000)

    # brute-force check if ORIGINHASH is newhash
    if ORIGINHASH == newhash:
        # success we found the password by brute-forcing
        # calculate the time this took.
        processtime = int(time.time()) - STARTTIME

        # fix for division by zero error when password is found within 1 sec
        if processtime == 0:
            processtime = 1

        count = 1
        print('\n[+] password found: {}' .format(password))

        # calculate amount of password that where scanned
        with open(DICTIONARY) as fhd:
            for line in fhd:
                if line.strip('\n') == password:
                    pps = count / processtime
                    print('\n[*] stats: processed {} password in {} seconds'
                          .format(count, processtime))
                    print('[*] stats: processed {} passwords/seconds' .format(pps))
                else:
                    count += 1

        # this is really uggly but some reason the multiprocessing will not stop
        # only after raising an exception. therefor we raise the most likely
        # exception: StopIteration, because we stop the iteration of multiprocessing
        raise StopIteration('[+]: password found.')

# main brute-force script
def main():
    ''' main function '''
    # start a try to catch the StopIteration exception wen the password is found
    try:
        # we need to check if dictionary file exists, if not exists exit with code 1
        if not os.path.exists(DICTIONARY):
            print('[-]: could not find dictionary file: {}' .format(DICTIONARY))
            sys.exit(1)

        # starting multiprocessing of the dictionary file
        pool = Pool()
        with open(DICTIONARY) as passwordline:
            # use pool.map to iterate through dictionary file and pass line to the
            # brute-force function (pool.map(function, itterable, chunksize)
            pool.map(brute_force_hash, passwordline, 100)

        # if script comes to this point no password was found, stop multiprocessing
        # and exit with code 1
        pool.close()
        pool.terminate()

        # create some statistics
        filelen = len(open(DICTIONARY).read().split('\n')) - 1
        processtime = int(time.time()) - STARTTIME
        pps = filelen / processtime
        print('\n[-]: no passwords where found')
        print('\n[*] stats: processed {} password in {} seconds' .format(filelen, processtime))
        print('[*] stats: processed {} passwords/seconds' .format(pps))
        sys.exit(1)
    except  StopIteration:
        # function raised StopIteration, password found, stop multiprocessing
        # and exit with code 0
        pool.close()
        pool.terminate()
        sys.exit(0)

if __name__ == "__main__":
    # run main function
    main()
