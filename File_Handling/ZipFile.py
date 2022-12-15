from zipfile import *

f = ZipFile('new_zip.zip', 'w', ZIP_DEFLATED)
f.write('new-photo.jpg')

# f = ZipFile("new_zip.zip", 'r', ZIP_STORED)
# names = f.namelist()
