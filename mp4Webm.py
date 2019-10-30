import os, subprocess, re
import messages as msg

# settings = helpers.get_settings()

def execute(PATH):
	def removeOriginalExt(FILENAME):
		return re.sub('\.mp4$', '', FILENAME)

	videoFiles = os.listdir(PATH)
	msg.show(videoFiles)
	for item in videoFiles:
		itemName = os.path.splitext(item)[0]
		subprocess.call([
			'ffmpeg',
			'-i',
			'{}/{}'.format(PATH, item),
			'-c:v',
			'libvpx',
			'-crf',
			'10',
			'-b:v',
			'1M',
			'-c:a',
			'libvorbis',
			'{}/{}.webm'.format(removeOriginalExt(PATH), itemName)
		])

	# ffmpeg -i input-file.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output-file.webm
