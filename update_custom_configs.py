import subprocess
import sys

CLOSE_PAGE_PATH1 = "/usr/share/jitsi-meet/static/close3.html"
WATERMARK_IMG_PATH = "/usr/share/jitsi-meet/images/watermark.png"

CLOSE_PAGE_CONTENT = """
<html>
   <head>
   </head>
   <body>
      <div style="height: 100%;">
         <h4>Meeting has ended</h4>
      </div>
   </body>
</html>
"""
WATERMARK_IMG_DATAURL = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGP6zwAAAgcBApocMXEAAAAASUVORK5CYII="

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pybase64")

import base64 

png_recovered = base64.decodestring(WATERMARK_IMG_DATAURL.encode())
f = open(WATERMARK_IMG_PATH, "wb")
f.write(png_recovered)
f.close()




f = open(CLOSE_PAGE_PATH1, "w")
f.write(CLOSE_PAGE_CONTENT)
f.close()


print("Custom config update complete")

