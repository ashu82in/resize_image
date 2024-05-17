#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:22:54 2024

@author: ashutoshgoenka
"""

import streamlit as st
from PIL import Image
import PIL
import os
import zipfile
from zipfile import ZipFile, ZIP_DEFLATED
import pathlib
import shutil



try:
    shutil.rmtree("images_comp")
except:
    pass
    

st.title("Resize Images")
# st.write('My first app Hello *world!*')
up_files = st.file_uploader("Upload Image Files", type = ["png", "jpeg", "jpg"] ,accept_multiple_files=True)
# st.write(up_files)

def resize(img, new_width):
    width, height  = img.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = img.resize((new_width, new_height), resample=PIL.Image.LANCZOS)
    return resized_image




try:
    os.mkdir("images_comp")
except:
    pass

 option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method..",
)

st.write("You selected:", option)

for file in up_files:
    
    
    # files = os.listdir("images")
    extensions = ["jpg", "jpeg", "png", "gif", "webp"]
    im = Image.open(file)
    # st.write(file)
    st.image(file)
   
    # st.write(im.size)
    im_resized = resize(im, 400)
    # st.write(im_resized.size)
    im_resized.save("images_comp/"+file.name)
    
    

zip_path = "images_compressed.zip"
directory_to_zip = "images_comp"
folder = pathlib.Path(directory_to_zip)
# st.write(folder)


with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
    for file in folder.iterdir():
        zip.write(file, arcname=file.name)
        
with open("images_compressed.zip", "rb") as fp:
    btn = st.download_button(
        label="Download ZIP",
        data=fp,
        file_name="images_compressed.zip",
        mime="application/zip"
    )
    
os.remove(zip_path)
shutil.rmtree("images_comp")

# st.download_button("Download Images", file_name="bali.jpeg")
    
    # for file in files:
    # ext = im.name.split(".")[-1]
    # if ext in extensions:
    #     # im = Image.open("images/"+file)
        
        
    #     im_resized = resize(im, 400)
    #     filepath = "images/"+file+".jpg"
    #     im_resized.save(filepath)
        
