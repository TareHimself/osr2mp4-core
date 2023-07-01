import os
from osr2mp4.VideoProcess.DiskUtils import convert_tomp4
import time
import sys
import shutil
from osr2mp4.osr2mp4 import Osr2mp4

def main():
	# data = read("osr2mp4/config.json")

	# gameplaydata = read("osr2mp4/settings.json")

	osu_path, skin_path,beatmap_path = sys.argv[1:4]
	osr2mp4 = Osr2mp4(data={
		"osu! path": osu_path,
    "Skin path": skin_path,
    "Beatmap path": beatmap_path,
    ".osr path": "auto",
    "Default skin path": "",
    "Output path": os.path.join(os.getcwd(),"replay.mkv"),
    "Width": 1920,
    "Height": 1080,
    "FPS": 60,
    "Start time": 0,
    "End time": -1,
    "Video codec": "XVID",
    "Process": 2,
    "ffmpeg path": "ffmpeg"
	},
	filesettings="./settings.json", 
# filepp="osr2mp4/ppsettings.json",
	logtofile=True)

	print("Rendering Video")
	osr2mp4.startvideo()
	osr2mp4.joinall()
	# osr2mp4.joinvideo()
	# shutil.copyfile(os.path.join(osr2mp4.settings.temp,'outputf.mkv'),osr2mp4.settings.output)
	# osr2mp4.cleanup()
	print("Finished Rendering Video")

	if os.name != 'nt':
		convert_tomp4(osr2mp4.settings)


if __name__ == "__main__":
	asdf = time.time()
	main()
	print("\nTotal time:", time.time() - asdf)
