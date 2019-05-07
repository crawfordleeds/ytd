# ytd YouTube Downloader

ytd is a command line program that downloads YouTube videos and playlists. It is written in python with the pytube library.

## How to use

`python ytd.py -arguments` or `ytd -arguments` if built to an executable

There are two obvious required arguments:

* `-v 'ur'` to download a single video.
* `-p 'url'` to download an entire playlist.

There are a couple of optional arguments:

* `-o 'path'` to set the download directory.
* `-r 'res'` to select the video's resolution to download.
* `-c 'lang'` to download srt captions in the selected language if available.
* `-d` to download audio streams only (but still in a video format for now).
* `-g` to download progressive streams only (video and audio in one file).
* `-a` to download adaptive streams only (video and audio in separate files).

## Building

I built it with pyinstaller on Windows.

To install pyinstaller run 
```python
pip install pyinstaller
```
to build to a single-file executable run
```python
pyinstaller ytd.py -F
```
the executable can be copied to a PATH directory to run directly from the terminal.
