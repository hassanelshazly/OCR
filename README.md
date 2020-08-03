
# OCR

### Dependencies

Tesseract v4.0 or more

```
pip install pillow 
pip install pytesseract
pip install imutils
```

### Manual Script
The script is located in ocr.py file, use the following command to run it

    python3 scripts/ocr.py <image_path> <text_mode> <Mode>

Options

    <Mode> 
"m"    <br> It will open a window to you, so you can select text from image.
      If you selected wrong area in image and want to undo it, press "c". 

"a"    <br> It will try to find the border of the page and extract it
      not effection in low qualtiy photos

    <text_mode>
0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Orientation and script detection (OSD) only.<br>
1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Automatic page segmentation with OSD.<br>
2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Automatic page segmentation, but no OSD, or OCR. (not implemented)<br>
3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fully automatic page segmentation, but no OSD. (Default)<br>
4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Assume a single column of text of variable sizes.<br>
5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Assume a single uniform block of vertically aligned text.<br>
6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Assume a single uniform block of text.<br>
7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Treat the image as a single text line.<br>
8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Treat the image as a single word.<br>
9 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Treat the image as a single word in a circle.<br>
10 &nbsp;&nbsp;&nbsp;&nbsp; Treat the image as a single character.<br>
11 &nbsp;&nbsp;&nbsp;&nbsp; Sparse text. Find as much text as possible in no particular order.<br>
12 &nbsp;&nbsp;&nbsp;&nbsp; Sparse text with OSD.<br>
13 &nbsp;&nbsp;&nbsp;&nbsp; Raw line. Treat the image as a single text line,
    bypassing hacks that are Tesseract-specific.

### Autonomous Script
The script is located in auto.py file, use the following command to run it

    python3 scripts/auto.py <image_path>

This script automatically detect locations of text in image, select them and type the detected text over them.<br>
This script is weak in detecting rotated text As it would't transform the image to any persp, but it can detect line words in specific banner.

### Google Script
It needs an API_KEY in order to work

    python3 scripts/google.py <image_path>
