import numpy as np 
import cv2 
import pyautogui 
import keyboard
from datetime import date
  
image_call = 0
print("""
████████╗░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
░░░██║░░░███████║█████═╝░██║██╔██╗██║██║░░██╗░
░░░██║░░░██╔══██║██╔═██╗░██║██║╚████║██║░░╚██╗
░░░██║░░░██║░░██║██║░╚██╗██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░

░██████╗░█████╗░██████╗░███████╗███████╗███╗░░██╗░██████╗██╗░░██╗░█████╗░████████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░██║██╔════╝██║░░██║██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░██║░░╚═╝██████╔╝█████╗░░█████╗░░██╔██╗██║╚█████╗░███████║██║░░██║░░░██║░░░╚█████╗░
░╚═══██╗██║░░██╗██╔══██╗██╔══╝░░██╔══╝░░██║╚████║░╚═══██╗██╔══██║██║░░██║░░░██║░░░░╚═══██╗
██████╔╝╚█████╔╝██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║╚█████╔╝░░░██║░░░██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═════╝░

██╗░░░░░██╗██╗░░██╗███████╗  ██████╗░██████╗░░█████╗░██╗
██║░░░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║
██║░░░░░██║█████═╝░█████╗░░  ██████╔╝██████╔╝██║░░██║██║
██║░░░░░██║██╔═██╗░██╔══╝░░  ██╔═══╝░██╔══██╗██║░░██║╚═╝
███████╗██║██║░╚██╗███████╗  ██║░░░░░██║░░██║╚█████╔╝██╗
╚══════╝╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝""")


print("press S to take a SS and q to exit!")

print("enter the image name you wanna give in this session")
im = input("==>")

# take screenshot using pyautogui 
while True:
	if keyboard.is_pressed('s'):
		image_call += 1
		image = pyautogui.screenshot() 
		now = date.today()
		print("time is "+str(now))
		# since the pyautogui takes as a  
		# PIL(pillow) and in RGB we need to  
		# convert it to numpy array and BGR  
		# so we can write it to the disk 
		image = cv2.cvtColor(np.array(image), 
		cv2.COLOR_RGB2BGR) 
		print("taking screenshot...")
		# writing it to the disk using opencv 
		cv2.imwrite("{}_{}_{}.png".format(im,image_call,now), image) 
		print("screenshot taken!, saving image as {}_{}_{}.png".format(im,image_call,now))
	elif keyboard.is_pressed('q'):
		print("closing the program...")
		break
print("thankyou Kiddo! AHah")
		