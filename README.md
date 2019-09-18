
# OCR

**Dependencies**

Tesseract v4.0 or more

pip install pillow
pip install pytesseract
pip install imutils

**Manual Script**
The script is located in ocr.py file, use the following command to run it

    python3 ocr.py <image_path> <text_mode> <Mode>

Options

    <Mode> 
m     It will open a window to you, so you can select text from image.
      If you selected wrong area in image and want to undo it, press "c". 

a     It will try to find the border of the page and extract it
      not effection in low qualtiy photos

    <text_mode>
0     Orientation and script detection (OSD) only.
1     Automatic page segmentation with OSD.
2     Automatic page segmentation, but no OSD, or OCR. (not implemented)
3     Fully automatic page segmentation, but no OSD. (Default)
4     Assume a single column of text of variable sizes.
5     Assume a single uniform block of vertically aligned text.
6     Assume a single uniform block of text.
7     Treat the image as a single text line.
8     Treat the image as a single word.
9     Treat the image as a single word in a circle.
10    Treat the image as a single character.
11    Sparse text. Find as much text as possible in no particular order.
12    Sparse text with OSD.
13    Raw line. Treat the image as a single text line,
    bypassing hacks that are Tesseract-specific.

**Autonomous Script**
The script is located in auto.py file, use the following command to run it

    python3 auto.py <image_path>

This script automatically detect locations of text in image, select them and type the detected text over them.
This script is weak in detecting rotated text As it would't transform the image to any persp, but it can detect line words in specific banner.

**google Script**
It needs an API_KEY in order to work

    python3 google.py <image_path>