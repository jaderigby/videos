import os, subprocess
import messages as msg

# settings = helpers.get_settings()

def execute(PATH):
	videoFiles = os.listdir(PATH)
	msg.show(videoFiles)
	setWidth = raw_input("Set the value of the overall width: [480] ")
	if setWidth == "":
		setWidth = 480
	subprocess.call(['mkdir', PATH + 'resized'])
	for item in videoFiles:
		subprocess.call([
			'ffmpeg',
			'-i',
			PATH + item,
			'-vf',
			'scale='+str(setWidth)+':-1',
			'{}/resized/{}'.format(PATH, item)
		])
