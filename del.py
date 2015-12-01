#!/bin/python
import email, imaplib
im =imaplib.IMAP4_SSL('imap.gmail.com', '993')
im.login('artificialdoorman@gmail.com', 'password')
print im.list()
im.select()
 
im.store("1:*",'+X-GM-LABELS', '\\Trash')

im.expunge() # should be useless
#typ, data = im.search(None, 'All')
#for num in data[0].split():
#	im.store(num, '+FLAGS', '\\Deleted')
#im.store("1:*", '+FLAGS', '\\Deleted')
#im.expunge()
