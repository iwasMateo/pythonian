import cv2
import numpy as np
import subprocess

subprocess.run(["grim", "/tmp/screenshot.png"], check=True)
img=cv2.imread("/tmp/screenshot.png")
cv2.imshow("Screenshot",img)