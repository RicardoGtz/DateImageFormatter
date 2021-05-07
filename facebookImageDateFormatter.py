import os  # Handle the files
import piexif  # Handle Image loading and editing
import sys
from bs4 import BeautifulSoup  # Work with HTML files
from datetime import datetime

# This is the folder path passed through arguments at execution
folderPath = sys.argv[1]

# Get all HTMl files in the folder
htmlFiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(folderPath)
             for name in files]

for file in htmlFiles:
    with open(file, 'rb') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    photoList = soup.find_all("div", class_="pam _3-95 _2pi0 _2lej uiBoxWhite noborder")
    print("Working in album: ", soup.head.title.string)
    for photo in photoList:
        photoURI = photo.find("div", class_="_3-96 _2let").img['src']
        photoDate = photo.find("div", class_="_3-94 _2lem").a.string
        print("\tImage file name: ", photoURI,"\n\tExtracted date: ", photoDate)
        date_time_obj = datetime.strptime(photoDate, '%b %d, %Y, %I:%M %p')
        new_date = date_time_obj.strftime("%Y:%m:%d %H:%M:%S")
        photoURI = folderPath.replace("photos_and_videos/album","")+photoURI
        exif_dict = piexif.load(photoURI)
        exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, photoURI)
        print("\t","--- Date updated successfully to - ",new_date)
