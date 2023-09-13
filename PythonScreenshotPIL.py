from PIL import ImageGrab
from datetime import datetime
now = datetime.now()
date_string = now.strftime('%Y-%m-%d %H-%M-%S')
#print the date object, not the container ;-)
img = ImageGrab.grab()
file = f"{date_string}_screenshot.jpg" 
print(file)
img.save(file)