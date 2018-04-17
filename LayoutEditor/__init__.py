
def main():
    """Entry point for the application script"""
    #print("Call your main application code here")


# print("Search LayoutEditor installation")

import sys
import os,site

dir=""


from sys import platform
if platform == "linux" or platform == "linux2":
    #linux
    if sys.version_info > (3, 0):
        dir="/opt/layout/python3"
        #dir="/home/thies/layout/python3"
    else:
        dir="/opt/layout/python"
elif platform == "darwin":
    # OS X
    dir="/Applications/layout.app/Contents/python"
elif platform == "win32":
    # Windows...
    dir="Program Files (x86)/LayoutEditor/python"

import os
if (os.path.isdir(dir)):
    site.addsitedir(dir)
    try:
        import LayoutScript

    except:
        print ("ops, there was a problem load LayoutScript for python")
else:
    print ("it seems that the LayoutEditor is not installed on your system")
    print ("please download and install it from https://layouteditor.com/download.html")
