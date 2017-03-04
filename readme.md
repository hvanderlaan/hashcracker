# hashcracker [![Build Status](https://travis-ci.org/hvanderlaan/hashcracker.svg?branch=master)](https://travis-ci.org/hvanderlaan/hashcracker)

Hashcracker is python script for brute-forcing sha512 hashed linux passwords. In addition to hashcracker there is also a python script for creating sha512 hashed linux passwords, this script is called mkpasswd.py

This script needs a dictionary file with the most common passwords, in the directory `dict/` you can find 4 dictionary files:

    - small.dict.txt      (1.000 most common passwords)
    - medium.dict.txt     (10.000 most common passwords)
    - lagre.dict.txt      (100.000 most common passwords)
    - very_large.dict.txt (1.000.000 most common passwords)

## Usage

    ./mkpasswd.py
    [*] please enter a password: 
    hash: $6$SzxuWrh5$DCSVtTt.9HH7IWrdiHApDhtfPG.1B17LzIlpJMA58RZwRIarPMkcuSogiOq0skAdfOnfjnM9Zgd3KhRS5zDkm1
    
    ./hashcracker.py
    #####################################################################
    # hashcracker.py - brute-force the shit out sha512 hashed passwords #
    #                                                                   #
    #        FOR EDUCATIONAL PURPOSES ONLY, THIS COULD BE ILLEGAL       #
    #####################################################################
    
    enter sha512 hash: $6$SzxuWrh5$DCSVtTt.9HH7IWrdiHApDhtfPG.1B17LzIlpJMA58RZwRIarPMkcuSogiOq0skAdfOnfjnM9Zgd3KhRS5zDkm1
    enter dict file  : dict/medium.dict.txt
    
    [+] password found: brook
    
    [*] stats: processed 9999 password in 50 seconds
    [*] stats: processed 199 passwords/seconds

## Legal
This script is for educational purposes and penetration testing purposes only. The creator of this script is in no way responsible for the action of the user. And can not held accountable for any damage to his or an other's system.
