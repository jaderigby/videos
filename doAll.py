import messages as msg
import resize, mp4Webm, subprocess, os, re, helpers

settings = helpers.get_settings()

def execute(PATH):
    resize.execute(PATH)
    posters.execute(PATH)
    mp4Webm.execute(PATH)
