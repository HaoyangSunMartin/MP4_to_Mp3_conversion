"""
Trevor Amestoy
Cornell University
January, 2023

This script is the main executable, calling the main_module_function which does
the rest of the work.
"""

# Import the main package
import sample_package
from moviepy.editor import *
import os
import argparse


def parse_file_names(absolute_path:str)->list[str]:
    return [f for f in os.listdir(absolute_path) if (f.endswith(".mp4") and not f.startswith("._")) ]
def convert(root:str,files:list[str],destination:str):
    for index, f in enumerate(files):
        video = VideoFileClip(os.path.join(root,f))
        name = f[:-4]+".mp3"
        video.audio.write_audiofile(os.path.join(destination,name))
        print("finished file:", " index: ", index, " name:", name)

def run():
    video = VideoFileClip(os.path.join("path","to","movie.mp4"))
    solved = sample_package.main_module_function()
    return solved



# Run the function if this is the main file executed
if __name__ == "__main__":
    #setup the argparser
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--base_path", type=str,
                        help="the base file path of the videos to convert")
    parser.add_argument( "-f","--files", type=str,nargs='*', help="the names of the .mp4 files to convert")
    parser.add_argument("-d","--destination",type=str, help="the destination folder to store the .mp3 files")
    parser.add_argument("-A","--ALL",action='store_true',help="if to convert all the .mp4 files under the path")
    args = parser.parse_args()
    
    if args.ALL:
        file_names = parse_file_names(absolute_path=args.base_path)
    else:
        file_names = args.files
    convert(root=args.base_path,files=file_names,destination=args.destination)
        
    #run()
