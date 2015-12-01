#!/bin/python
import email, imaplib

#initialize IMAP thing
im =imaplib.IMAP4_SSL('imap.gmail.com', '993')
#log in
im.login('artificialdoorman@gmail.com', 'so when is spring break?')
#select gmail inbox
im.select()
#select every message
im.store("1:*",'+X-GM-LABELS', '\\Trash')
#delete 'em
im.expunge()
