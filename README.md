# Facebook Image Date Formatter

---

This script is intended to modify the EXIF data from a copy of your photos downloaded from [Facebook](https://www.facebook.com/)
and change it to the date of upload. This is comes handy when you download a copy of your information form Facebook 
and wants to back up you photos in other services like google photos, and wants go them order as accurate as possible.
If you want to know how to download a copy of all your photos from Facebook please look for the last section of this file.

By default, the photos will have the date of when the copy was created as the date in the EXIF data, this script modifies
the EXIF info of each photo and replace it with the upload date of the photo.

## How to use it?

---

Extract the zip file downloaded directly from Facebook, execute the script followed by the **FULL PATH** to the 
*extracted folder* as shown below  

`$ python facebookImageDateFormatter C:/full_path/extracted_folder/photos_and_videos/album`

### How it works?

---

The script will scan throw the html files inside the *album* folder, each file have the images with the date info attached
the script extract this info and updates the date in EXIF data of the image file.

#### Dependencies list
|Package    |Version    |
|-----------|---------------|
|beautifulsoup4| [4.9.3](https://pypi.org/project/beautifulsoup4/)|
|piexif| [1.1.3](https://pypi.org/project/piexif/)|


### How to get a copy from all my photos and videos uploaded to Facebook?

---

1. Open [Facebook](https://www.facebook.com/)
2. Go to *Settings & privacy* -> *Settings* -> *Your Facebook information*
3. Move down to *Download your information* and click on *view*
4. In the *Request Copy* section select the *Data Range*, and the *Media Quality* you prefer 
5. Set the *Format* to HTML
6. From 'Your information' section mark only 'Photos and Videos' 
7. Click on *Create File*

A copy of all your data will be created and you will receive a notifications when it's ready to download.
