import SimpleCV
import time

camera = SimpleCV.Camera()
display = SimpleCV.Display()       #for display
#image  = camera.getImage()         #to get image
#image.drawText("Hello World",200,200)  #for text
#image.save(display)                    #saving to show
#time.sleep(5)                         #timer
camera.live()                           #live camera
#img = camera.getImage()

#img.save(filepath)
#print "Saved Successfully to"+filepath
#img.save(display)
time.sleep(5)
