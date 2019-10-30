import sys, resize, status, helpers
import posters
import mp4Webm
import code
import doAll
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

try:
	PATH = str(sys.argv[2])
except:
	PATH = None

if action == 'status' or action == None:
	status.execute()

elif action == 'resize':
	# You will want to change the name to something specific, when developing
	resize.execute(PATH)

elif action == "poster":
    posters.execute(PATH)

elif action == "mp4-webm":
    mp4Webm.execute(PATH)

elif action == "code":
    code.execute()

elif action == "do-all":
    doAll.execute(PATH)
# new actions start here
