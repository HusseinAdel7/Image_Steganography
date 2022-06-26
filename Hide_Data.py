import os.path
from sys import platform
from tkinter import Y
import time
from ctypes import resize
import numpy as np
import cv2
import matplotlib.pyplot as plt
import types 
import os 
from termcolor import colored
import PIL.Image
import io 

# Checking if you're using Linux or Windows and getting the desktop path 
if platform == "linux" or platform == "linux2":
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    os.chdir(desktop)
elif platform == "win32":
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desktop)
#--------------------------------------------------------------------------------

# Clear the screan after run the script 
os.system('clear') #

# this section for printing the title and our names
print ("\n\n\t\t\t    -------------------------")
print(colored('\t\t\t       Steganography Image ', 'red'))
print ("\t\t\t    -------------------------")
print(colored('\n\t\t* Written by :  ', 'red'),end="")
print("  Hussein Adel")
print (colored('\t\t\t\t  ------------','white'))
print (colored('\t===================================================================','blue'))
print (colored('\t\t\t\t  ------------','white'))
print(colored('\t\t\t\t    Hello \U0001f600 ', 'blue'))
print (colored('\t\t\t\t  ------------\n','white'))
#-----------------------------------------------------------------------------------

# A Secrect Key exists at the end of the secret message.
key_sec=input(" * Enter a shared secret key to hide and extract any data : ")

# Checking if he entered a key or not.
if len(key_sec) > 0:
    
        # This function for converting our message to binary to handle it.
    def Converting_To_Bin(data):
        if type(data)==str:
            return ''.join([format(ord(i),"08b")for i in data])
        elif type(data)==bytes or type(data)==np.ndarray:
            return [format(i,"08b")for i in data ]
        elif type(data)==int or type(data)==np.uint8:
            return format(data,"08b")
        else:
            print(" * Please, Enter Your data as a Text")

    # This function for hiding our data (binary)*.
    def hideData(pic,data):
        number_Of_Bytes=pic.shape[0]*pic.shape[1]*3
        if len(data)>number_Of_Bytes:
            print(" * Your Data must be less than this")
        data+=key_sec
        data_index=0
        binary_Message=Converting_To_Bin(data)
        binary_Message_len=len(binary_Message)
        for values in pic:
            for pixel in values:
                r,g,b = Converting_To_Bin(pixel)
                if data_index<binary_Message_len:
                    pixel[0]=int(r[:-1]+binary_Message[data_index],2)
                    data_index+=1
                if data_index<binary_Message_len:
                    pixel[1]=int(g[:-1]+binary_Message[data_index],2)
                    data_index+=1
                if data_index<binary_Message_len:
                    pixel[2]=int(b[:-1]+binary_Message[data_index],2)
                    data_index+=1
                if data_index>=binary_Message_len:
                    break
        print (colored('\n\t\t\t\t  ------------','white'))
        print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
        print (colored('\t\t\t\t  ------------\n','white'))
        return pic

    # This function encodes the data
    def encode_data():
        original_Image=input(" * Enter the image name with its path and extention : ")
        image = cv2.imread(original_Image)
        resized_image=cv2.resize(image,(500,500))
        plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB))
        print(colored('\n\t\t       Choose one of the following:- ', 'red'))
        print(colored('\t\t     ---------------------------------', 'white'))
        print("\t\t       1- Hiding a text\n\t\t       2- Hiding a text file\n\t\t       3- Hiding an Image\n\t\t       4- Hiding a Video\n\t\t       5- Hiding an exe file\n\t\t       6- Hiding a script",end="")
        d=int(input(""))
        if d==1:
            data=input(" * Enter Your Message That You Want To Hide : ")
            if len(data)==0:
                print(" * There is nothing")
            injected_Image_name= input(" * Enter the new image name with its path and extention : ")
            injected_Image=hideData(image,data)
            cv2.imwrite(injected_Image_name,injected_Image)
        if d==2:
            file=input(" * Enter the file name with its path : ")
            with open(file) as f:
                contents = f.read()
            if len(contents)==0:
                print(" * There is nothing")
            injected_Image_name= input(" * * Enter the new image name with its path and extention : ")
            injected_Image=hideData(image,contents)
            cv2.imwrite(injected_Image_name,injected_Image)
        if d==3:
            img1_path = input("\n * Enter the Image that you want to hide with its path and extension : ")
            img = PIL.Image.open(img1_path)
            byte_arr = io.BytesIO()
            img.save(byte_arr,format="PNG")
            with open (original_Image,'ab') as f:
                    f.write(byte_arr.getvalue())
            print (colored('\n\t\t\t\t  ------------','white'))
            print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
            print (colored('\t\t\t\t  ------------\n','white'))
        if d==4:
            video_path = input("\n * Enter the video that you want to hide with its path and extension : ")
            with open(original_Image,"ab") as f, open(video_path,"rb") as s:
                f.write(s.read())
            print (colored('\n\t\t\t\t  ------------','white'))
            print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
            print (colored('\t\t\t\t  ------------\n','white'))
        if d==5:
            exe_path = input("\n * Enter the exe file that you want to hide with its path and extension : ")
            with open(original_Image,"ab") as f, open(exe_path,"rb") as s:
                f.write(s.read())
            print (colored('\n\t\t\t\t  ------------','white'))
            print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
            print (colored('\t\t\t\t  ------------\n','white'))
        if d==6:
            script_path = input("\n * Enter the script that you want to hide with its path and extension : ")
            with open(original_Image,"ab") as f, open(script_path,"rb") as s:
                f.write(s.read())
            print (colored('\n\t\t\t\t  ------------','white'))
            print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
            print (colored('\t\t\t\t  ------------\n','white'))
     # This function for Extracting our data 
    def decode():
        image_name=input("\n * Enter the injected image with its path and extention : ")
        print(colored('\n\t\t       Choose one of the following:- ', 'red'))
        print(colored('\t\t     ---------------------------------', 'white'))
        print("\t\t       1- Extracting a text\n\t\t       2- Extracting an Image\n\t\t       3- Extracting a video\n\t\t       4- Extracting an exe file\n\t\t       5- Extracting a script",end="")
        d=int(input(""))
        if d==1:
            # read the image
            image = cv2.imread(image_name)
            binary_data = ""
            for row in image:
                for pixel in row:
                    r, g, b = Converting_To_Bin(pixel)
                    binary_data += r[-1]
                    binary_data += g[-1]
                    binary_data += b[-1]
            # split by 8-bits
            all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
            # convert from bits to characters
            decoded_data = ""
            for byte in all_bytes:
                decoded_data += chr(int(byte, 2))
                stop=int(len(key_sec))
                if decoded_data[-(stop):] == key_sec:
                    break
            print(colored('\n * Your Hidden Data is : ', 'red'),end="")
            print(decoded_data[:-(stop)])
        elif d==2:
            with open(image_name,'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FFD9'))
                f.seek(offset+2)
                new_image = PIL.Image.open(io.BytesIO(f.read()))
                new_image_path = input("\n * Enter the new Image name with its path and extension : ")
                new_image.save(new_image_path)
        elif d==3:
                with open(image_name,'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset+2)
                    new_video_path = input("\n * Enter the new video name with its path and extension : ")
                    with open (new_video_path,"wb") as e:
                        e.write(f.read())
        elif d==4:
                with open(image_name,'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset+2)
                    new_exe_path = input("\n * Enter the new exe name with its path and extension : ")
                    with open (new_exe_path,"wb") as e:
                        e.write(f.read())
                                
        elif d==5:
                with open(image_name,'rb') as f:
                    content = f.read()
                    offset = content.index(bytes.fromhex('FFD9'))
                    f.seek(offset+2)
                    new_exe_path = input("\n * Enter the new script name with its path and extension : ")
                    with open (new_exe_path,"wb") as e:
                        e.write(f.read())
        print (colored('\n\t\t\t\t  ------------','white'))
        print(colored('\t\t\t\t     Done \U0001f600 ', 'blue'))
        print (colored('\t\t\t\t  ------------\n','white'))

       # This function looks like main function, inside it we invoke the encoded and decoded function
    def steganography():
        print(colored('\n\t\t       Choose one of the following:- ', 'red'))
        print(colored('\t\t     ---------------------------------', 'white'))
        print("\t\t       1-  Hiding Data into an image\n\t\t       2-  Extracting Data from an image",end="")
        pro=int(input(""))
        if pro==1:
            print(colored('\n\t\tNow, You are going to hide data into an image..', 'red'))
            print(colored('\t     ------------------------------------------------', 'white'))
            encode_data()
        elif pro==2:
            print(colored('\n\t\tNow, You are goning to extract data from an image..', 'red'))
            print(colored('\t     ---------------------------------------------------------', 'white'))
            decode()
    steganography()
