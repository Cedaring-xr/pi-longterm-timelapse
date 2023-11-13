# import libraries
from picamera2 import Picamera2, Preview
import time
#import os

# setup variables
interval = 5  # time in seconds between images
frame = 0

#setup and start camera
picam = Picamera2()

config = picam.create_preview_configuration(main={"size": (1600, 1200)})
# config["transform"] = picam.Transform(hflip=1, vflip=1)
picam.configure(config)

# (old) picam.resolution = (4056, 3040) # default is 1920 x 1080
picam.start_preview(Preview.QTGL)


# let camera settle and focus
picam.start()
time.sleep(2)

# loop over a range for taking consecutive pictures
for i in range(1, 10):
	picam.capture_file(f"ts{i}.jpg")
	print(f"Captured image {i}")
	time.sleep(interval)


picam.stop()




# shut down when done
# os.system('sudo shutdown now')
