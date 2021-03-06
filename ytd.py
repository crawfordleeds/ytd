from pytube import YouTube, Playlist
import argparse, os, time, pathlib


def video_dl(url, resolution, is_progressive, is_adaptive, is_only_audio, path, numbered, prefix):
	print('Fetching ...', end='\r')
	for i in range(6):
		try:
			video = YouTube(url, on_progress_callback=progress)
		except:
			if i < 5:
				print('Fetching failed, retrying ... {}' .format(i+1))
				continue
			else:
				print('Five retries failed, skipping current video ...')
				return -1
		break

	print('Downloading: %s' %video.title)
	stream = video.streams.filter(res=resolution, progressive=is_progressive, adaptive=is_adaptive, only_audio=is_only_audio).first()
	if stream == None:
		print('No video with the selected parameters found.')
	else:
		global file_size
		file_size = stream.filesize
		if numbered ==True:
			stream.download(output_path=path, filename=None, filename_prefix=prefix)
		else:
			stream.download(path)
		print('\nDownload completed')
	
	if args.c != None:
		lang_code = args.c
		cc = video.captions.get_by_language_code(lang_code)
		if cc == None:
			print('No captions in the selected language found.')
		else:
			srt = cc.generate_srt_captions()
			captions_file = open('%s.srt' %video.title, 'w+')
			captions_file.write(srt)
			captions_file.close()
	
	return 0


def playlist_dl(url, resolution, is_progressive, is_adaptive, is_only_audio, path):
	numbered = args.x
	links = Playlist(url).parse_links()
	number_of_videos = len(links)
	print('%s videos in playlist' %number_of_videos)
	t = args.t
	if t == -1:
		t = number_of_videos
	
	f = args.f - 1
	for i in range(f, t):
		prefix = '%d - ' %(i+1)
		video_dl(links[i], resolution, is_progressive, is_adaptive, is_only_audio, path, numbered, prefix)
	
	return 0


def progress(stream, chunk, file_handle, bytes_remaining):
	percent = round((1-bytes_remaining/file_size) ,4)
	blocks = round(percent*40)
	print('    %2.2f%%\t>%-40s< %2.2fMB' %(100*percent, '█'*blocks, file_size/(1024*1024)), end='\r')


arguments = argparse.ArgumentParser(description = 'YouTube Downloader v1.2')
required = arguments.add_argument_group('required arguments (use only one)')
required.add_argument('-v', type = str, metavar = "'url'", default = None , help = 'Video URL')
required.add_argument('-p', type = str, metavar = "'url'", default = None, help = 'Playlists URL')
arguments.add_argument('-o', type = str, metavar = 'path', default = '', help = 'Output path, relative to root directory. (e.g. -o C:\\Users\\Smith\\')
arguments.add_argument('-r', type = str, metavar = 'resolution', default = None, help = 'Video download resolution. (e.g. -r 480p)')
arguments.add_argument('-c', type = str, metavar = 'language code', default = None, help = 'Download srt captions. (e.g. -c en)')
arguments.add_argument('-f', type = int, metavar = 'n', default = 1, help = 'Start downloading playlist from the nth video. (e.g. -f 7)')
arguments.add_argument('-t', type = int, metavar = 'n', default = -1, help = 'Downloading playlist to the nth video. (e.g. -t 3)')
arguments.add_argument('-x', action='store_true', default = False, help = 'Number playlis videos.')
arguments.add_argument('-d', action='store_true', default = False, help = 'Download audio only streams')
arguments.add_argument('-a', action='store_true', default = False, help = 'Use adaptive streams only')
arguments.add_argument('-g', action='store_true', default = False, help = 'Use progressive streams only')
args = arguments.parse_args()


path = r"%s" %args.o
if path != '':
	if not os.path.exists(path):
		pathlib.Path(path).mkdir(parents=True)

resolution = args.r
if args.a == True and args.g == True:
	print('You cannot filter both progressive and adaptive streams ath the same time.')
	quit()
elif args.a == True:
	is_adaptive = True
	is_progressive = False
elif args.g == True:
	is_adaptive = False
	is_progressive = True
else:
	is_progressive = False
	is_adaptive = False

is_only_audio = args.d
if args.p != None and args.v != None:
	print('Please put either a video or a playlist url, not both.')
elif args.p == None and args.v != None:
	url = args.v
	video_dl(url, resolution, is_progressive, is_adaptive, is_only_audio, path, False, '')
elif args.v == None and args.p != None:
	url = args.p
	playlist_dl(url, resolution, is_progressive, is_adaptive, is_only_audio, path)
else:
	print('You must put either a video or a playlist url.')