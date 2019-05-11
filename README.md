# ytd

ytd is a command line YouTube downloader for videos and playlists. It is written in python with the pytube library.

That's the first thing I wrote in python, I hope it's good enough to be usefull.

## How to use

`ytd -arguments`

There are two obvious required arguments:

* `-v 'ur'` to download a single video.
* `-p 'url'` to download a playlist.

There are a couple of optional arguments:

* `-o 'path'` set the download directory.
* `-r 'res'` select the video's resolution to download.
* `-c 'lang'` download srt captions in the selected language if available.
* `-d` download audio streams only (but still in a video format for now).
* `-f n` download playlist from the nth video.
* `-t n` download playlist until the nth video.
* `-x` number downloaded playlist videos.
* `-g` download progressive streams only (video and audio in one file).
* `-a` download adaptive streams only (video and audio in separate files).

## Dependencies

* pytube library, to install it run:
	```
	pip install pytube
	```

## Building

I built it with pyinstaller on Windows and Ubuntu.

To install pyinstaller run:
```
pip install pyinstaller
```
to build to a single-file executable run:
```
pyinstaller ytd.py -F
```
the executable can be copied to PATH to run directly from the terminal.