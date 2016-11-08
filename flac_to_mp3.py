import sys
import glob, os

source = False
s_path = ''
arguments = iter(sys.argv)

for arg in arguments:
	if arg == '-s':
		source = True
		arg = next(arguments)
		s_path = arg
	elif arg == 'help':
		print('>> USAGE: flac_to_mp3 -s [SOURCE_DIR]')


if source:
	os.chdir(s_path)
	for file in glob.glob('*.flac'):
		command = 'ffmpeg -i \'{0}\' -ab 320k -map_metadata 0 -id3v2_version 3 \'{1}\''.format(file, file.replace('.flac','.mp3'))
		os.system(command)
else:
	print('>> Invalid Arguments.')
	print('>> USAGE: flac_to_mp3 -s [SOURCE_DIR]')
