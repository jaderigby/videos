def statusMessage():
	print
	print "Example usage: vid resize ~/staticcontent/videos/"
	print
	print "Available Commands:"
	print '''
[ vid resize <path to directory> ]			resize the original file
[ vid mp4-webm <path to directory> ]		create a webm file from the mp4 file
[ vid poster <path to directory> ]			create the poster image
[ vid do-all <path to directory> ]			resize, mp4-webm, and poster -- all in one!
[ vid code ]								generate html snippet
'''

def command(LIST):
	s = ""
	for item in LIST:
		s += item + " "
	print("Running Command: {}".format(s))

def show(INPUT):
	print
	if isinstance(INPUT, list):
		for item in INPUT:
			print item
	print
