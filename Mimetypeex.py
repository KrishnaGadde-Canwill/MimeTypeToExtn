import mimetypes, os
from mimetypes import guess_extension
import requests

# This below function gives wrong MimeType if the file extension is changed. So I used magic library
# def MimeTypeForFile(filename):
#     """
#     :param filename: input file name
#     :return: returns the mimetype
#     """
#     type = mimetypes.MimeTypes().guess_type(filename)[0]
#     print(type)
#     return  typeimeTypes().guess_type(filename)[0]
#     return  type

def MimeTypeforFile(fname):

    xx = magic.from_file(fname)
    tx = magic.Magic(mime = True)
    mime = tx.from_file(fname)
    print(mime)
    print(xx)




MimeTypeforFile('14.py')




def ExtnForMimeType(mtype):
    """
    :param mtype: Mimetype
    :return: returns .extension for that particular MimeType
    """
    extn = guess_extension(mtype)
    print(extn)
    return extn


for root, dirs, files in os.walk('.', topdown=True):
    dirs.clear()
    for file in files:
      # print(file)
      print("file name: ",file, "----------" "type: ", mimetypes.MimeTypes().guess_type(file)[0])
      MimeTypeForFile(file)


MimetypeList = [ 'image/png', 'application/pdf', 'text/x-python', 'message/rfc822']

for m in MimetypeList:
    ExtnForMimeType(m)












