#! /usr/bin/env python3
# coding: utf-8
"""
Barcode scanning with the picamera
Sandbox #1
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import time
from io import BytesIO

import picamera

from pyzbar.pyzbar import decode as pyzbar_decode
from PIL import Image as pil_image

#-----------------------------------------------------------------------------
# Test
#-----------------------------------------------------------------------------
# Camera setup
camera = picamera.PiCamera()
camera.sharpness = 100
camera.brightness = 55
camera.resolution = (500, 500)
camera.start_preview()

while True:
    # Get an image from the camera
    stream = BytesIO()
    camera.capture(stream, format='jpeg')
    stream.seek(0)

    # Scan image
    tmp = pyzbar_decode(pil_image.open(stream))
    print(tmp)