# # import OS module
# import os
 
# # Get the list of all files and directories
# path = "/home/shubhampanchal/Videos"
# dir_list = os.listdir(path)
 
# print("Files and directories in '", path, "' :")
 
# # prints all files
# print(dir_list)


from pprint import pprint
from pymediainfo import MediaInfo
import os

media_info = MediaInfo.parse("/home/shubhampanchal/Videos/Alcoholia Vikram Vedha Hrithik Roshan, Saif Ali Khan Vishal-Sheykhar, Manoj M Snigdhajit,Ananya.webm")
for track in media_info.tracks:
    if track.track_type == "Video":
        print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
              "Format: {t.format}".format(t=track)
        )
        print("Duration (raw value):", track.duration)
        print("Duration (other values:")
        pprint(track.other_duration)
    elif track.track_type == "Audio":
        print("Track data:")
        pprint(track.to_data())
    elif track.track_type == "Video":
        print("Track data:")
        pprint(track.to_data())