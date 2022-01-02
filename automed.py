import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import os, sys, time
import subprocess

SNAPSHOT_DIMENSIONS = (750,450,1160,650)
TESSERACT_PATH = r"C:\Users\jakem\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
N = 25000 # number of iterations (5,000 = about 1.5 hours)

def main():
  ahk_path = "C:\Program Files\AutoHotkey\AutoHotkey.exe"
  alpha = "bcfghjklmnprtuvxz"
  c = 0

  while True:
    if c == N:
      break
    c += 1
    # snapshot part of the screen & return an image
    img = ImageGrab.grab(bbox=SNAPSHOT_DIMENSIONS)
##    img.show()
    # to file
    img.save('snap.png')

    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    # convert image to character string
    letter = pytesseract.image_to_string(Image.open("snap.png"), config="--psm 10")
    if letter == '':       
      continue
    got_letter = letter.lower()[0]

    if got_letter in alpha:
      # press the key of the letter
      subprocess.Popen(f"{ahk_path} so_pressed.ahk {got_letter}")
##      print("Clicked:", got_letter)
    else:
      subprocess.Popen(f"{ahk_path} so_pressed.ahk m")
    # time delay gap between pressing key & taking next snapshot 
    time.sleep(.2)
  print("Done!")

if __name__ == "__main__":
  for i in range(5,0,-1):
    sys.stdout.write(f"\rStarting in {i} seconds")
    time.sleep(1)
  sys.stdout.write("\rRunning...           ")
  main()
  if os.path.exists("snap.png"):
      os.remove("snap.png")
