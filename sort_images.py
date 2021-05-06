# USAGE
# python sort_images.py --source source --destination destination --format .jpg

from imutils import paths
import os
import argparse
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True, help="path to the source images folder")
ap.add_argument("-d", "--destination", required=True, help="path to the destination folder")
ap.add_argument("-f", "--format", required=True, help="format of images")
args = vars(ap.parse_args())

def sort_images(SOURCE, DESTINATION, FORMAT):
    Paths = paths.list_images(SOURCE)
    # Create a list of new Paths (only file with size > 0)
    new_Paths = []

    for path in Paths:
        if os.path.getsize(path) > 0:   # keep ony file with size > 0
            new_Paths.append(path)
    
    i = 1
    for path in new_Paths:
        filename = "image" + "_" + format(i, "0>5d") + FORMAT  # 0: fill left empty location, >: right align ,5: length of string, d integer
        destination = os.path.sep.join([DESTINATION , filename])
        shutil.copyfile(path, destination)
        i += 1

if __name__ == "__main__":
    SOURCE = args["source"]
    DESTINATION = args["destination"]
    FORMAT = args["format"]
    sort_images(SOURCE, DESTINATION, FORMAT)