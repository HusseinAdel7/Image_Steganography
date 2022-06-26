> # Steganography

Steganography is the technique of hiding secret information.

The steganography hides different types of data within a cover file. 

The resulting stego file also contains hidden information, although it is virtually identical to the cover file.

> ## Image Steganography
 Image steganography refers to hiding information i.e. text, images, audios, videos, scripts, exe files in another image.
 
I rely on two directions in this tool to hide information in an image:

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1- LSB Method

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2- Hexa Decimal for the Image

> ### 1- LSB Method 

The Least Significant Bit (LSB) steganography is one technique in which the least significant bit of the image is replaced with a data bit. In this method, the least significant bits of some or all of the bytes inside an image are replaced with a bit of the secret message.
#### An image for describing LSB 
<img src="https://3.bp.blogspot.com/-Y2mozhtViLQ/WnIwaQdEKfI/AAAAAAAAKGs/Z78gfWuI1bMfDeyNcCf0uBsS7Ttr6LQdgCLcBGAs/s640/encode.png">

#### A screenshot from the code

<img src="https://user-images.githubusercontent.com/84356407/175820465-4e9946a1-fb32-4d0d-ab07-30e653c19b90.jpeg">

To learn more about LSB Steganography follow this link [More_about_LSB](https://www.geeksforgeeks.org/image-based-steganography-using-python/)

> ### 2- Hexa Decimal for the Image

Every JPEG/JPG file just like any other object has a beginning or header, called “Start of Image” and a trailer called “End of Image”, every JPEG file starts from the binary value ‘0xFFD8‘ and ends by the binary value ‘0xFFD9‘.

After this value '0xFFD9' we insert our information.
#### An image for describing jpeg image with its start and end
<img src="https://user-images.githubusercontent.com/84356407/175820837-9944cdc2-08b5-46c4-9ced-74e59ca748cc.png" width="820">

We know that exe file starts with '0x4D5A'.

#### An image shows that we hid an exe in an image 
<img src="https://user-images.githubusercontent.com/84356407/175821229-d253537a-2194-4be5-b1a4-fbaadbda2a80.png" width="820">

> # How to run this script

## Install python 
Download the latest version of python [python](https://www.python.org/downloads/)
## install labriries that we need
```
pip install ctypes
```
```
pip install numpy
```
```
pip install opencv-python
```
```
pip install tk
```
```
pip install os-sys
```
```
pip install syspath
```
```
pip install python-time
```
```
pip install matplotlib
```
```
pip install types-all
```
```
pip install termcolor
```
```
pip install requires.io
```
```
pip install Pillow
```

## Run on cmd or terminal 
```
python Hide_data.py
```
# Final Run
<div>
   <img src="https://user-images.githubusercontent.com/84356407/175823315-3a87f34e-b9b8-4526-a0df-8254bc2a20e9.png" width="820">
   <img src="https://user-images.githubusercontent.com/84356407/175823312-98e2b4f7-b58d-462f-9c62-b423039bcfc7.png" width="820">
 </div>
 
> # A note

## There is a demo 

Each file has an original image and injected image.
If you want to extract information use this key '###'
