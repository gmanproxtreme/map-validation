import glob
from PIL import Image





# read in prefabs.xml files - recurse through world directories in a root path
# glob_path = Path(r"J:\Games\7D2D\candidates")
# file_list = [str(pp) for pp in glob_path.glob("**/genHM.png")]md 

###########
# TESTING #
###########
file_list = ["c:\code\MAPCHKR\map-validation\genHM.png"]


for file in file_list:
    im = Image.open(file)

    #Check for mudflats
    print(im.format, im.size, im.mode)