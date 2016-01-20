#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special(v_dir):
	files = os.listdir(v_dir)
	sp_list = []
	for fil in files:
		if re.search(r"__\w+__", fil):
			sp_list.append(fil)
	for ele in sp_list:
		print os.path.abspath(os.path.join(v_dir,ele))

def copy_to(v_dir,todir):
	files = os.listdir(v_dir)
	sp_list = []
	for fil in files:
		if re.search(r"__\w+__", fil):
			sp_list.append(fil)
	if not os.path.exists(todir):
		os.mkdir(todir)
		
	for ele in sp_list:
		shutil.copy(os.path.abspath(os.path.join(v_dir,ele)), os.path.join(todir,ele))
		
def zip_to(v_dir, tozip):
	files = os.listdir(v_dir)
	sp_list = []
	for fil in files:
		if re.search(r"__\w+__", fil):
			sp_list.append(fil)
	cmd = 'zip -j ' + tozip + ' ' + ' '.join(sp_list)
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if not (todir or tozip):
  	  get_special(args[0])
  
  if todir:
  	  copy_to(args[0], todir)
  elif tozip:
    	  zip_to(args[0], tozip)
  
if __name__ == "__main__":
  main()
