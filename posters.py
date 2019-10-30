import os, subprocess, helpers
import messages as msg

settings = helpers.get_settings()

def execute(PATH):
	PATH = PATH + '/'
	videoFiles = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]
	if '.DS_Store' in videoFiles:
		videoFiles.remove('.DS_Store')
	msg.show(videoFiles)
	setWidth = raw_input("Set the value of the overall width: [420] ")
	setCustomFrames = input('''[1] Default position to 00:00:01
[2] Custom positions
[3] Custom positions from profile settings

selection: ''')
	setCustomFrames
	if setWidth == "":
		setWidth = 420
	subprocess.call(['mkdir', PATH + 'posters'])
	for item in videoFiles:
		filename = item[:-4]
		if setCustomFrames == 1:
			setFrame = "00:00:01"
		elif setCustomFrames == 2:
			setFrame = raw_input('''
Input snapshot position for {}
: [00:00:01] '''.format(item))
			if setFrame == "":
				setFrame = "00:00:01"
		elif setCustomFrames == 3:
			setFrame = settings['posters'][item]
		msg.command([
			'ffmpeg',
			'-ss',
			setFrame,
			'-i',
			PATH + item,
			'-vframes',
			'1',
			'-q:v',
			'2',
			# 'scale="{}:-1"'.format(setWidth),
			'{}posters/{}{}'.format(PATH, filename, '.jpg')
		])
		helpers.generate_posters(PATH, setFrame, item)
