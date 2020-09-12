*************************************************************************
           This tool is not made for any malicious use.                
*************************************************************************

### Donations.

* paypal: https://paypal.me/AndreasKarageorgos/

Add the executable file to a usb and insert it to the computer that you want to 
copy the files.

I recomend pyinstaller to create an executable file.

* windows

      pip install pyinstaller

* Linux

      pip3 install pyinstaller


# Run in background.

if you want it to run in the background, rename the File-Grabber.py to File-Grabber.pyw

# Create an executable file.
   
   * without console window
   
      pyinstaller -F File-Grabber.pyw
  
   * with console window
   
      pyinstaller -F File-Grabber.py
