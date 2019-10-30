import json, subprocess
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	return json.loads(read_file(profilePath))

def get_settings():
	profile = load_profile()
	return profile['settings']

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def generate_posters(PATH, setFrame, item):
	filename = item[:-4]
	subprocess.call([
		'ffmpeg',
		'-ss',
		setFrame,
		'-i',
		PATH + item,
		'-vframes',
		'1',
		'-q:v',
		'2',
		'{}posters/{}{}'.format(PATH, filename, '.jpg')
	])
