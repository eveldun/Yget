#!/usr/bin/env python3
##################################################
# Yget - Open Source YouTube Video Installer
# Version: 1.2 - Development Build (Code Name Interstellar)
# Credits: Install Location
# Purpose: Sick of not being able to right-click YouTube videos Download them with Yget
##################################################
import argparse
import os
import sys
import pytube
import time
import moviepy
arguments = argparse.ArgumentParser(prog="yget", description="Converts Your Favorite Songs To Downloaded Format")
arguments.add_argument("video_url", type=str, help="The Video Url")
arguments.add_argument("--file-format", "-f", type=str.lower, action="store", nargs=1, dest="filetype", default="mp4",
                       choices=["mp3", "mp4", "ffmpeg", "wav", "ogg", "webm"],
                       help="Video File Format: Mp3,Mp4 Default:Mp4")


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


args = arguments.parse_args()


class FileInfo:
    Ftype = args.filetype
    URL = None
    path = os.getcwd()
    def completed(stream, file_path):
            progress = Bcolors.OKGREEN + "━━" + Bcolors.ENDC
            print("[" + str(progress * 25) + "] COMPLETED!               ")
            print(Bcolors.OKBLUE + stream.title + " Downloaded" + Bcolors.ENDC)
            print(Bcolors.OKBLUE + "Saved To: " + Bcolors.OKGREEN + file_path + Bcolors.ENDC)
            return 0




def show_progress_bar(stream, chunk, bytes_remaining):
    sys.stdout.flush()
    ProgressBarLength = 100
    print((ProgressBarLength + 20) * " ", end="\r")
    Empty = (bytes_remaining / stream.filesize) * ProgressBarLength
    Progbar = ProgressBarLength - round(Empty)
    progress_bar = ("━" * Progbar) + (" " * round(Empty))
    print(f"[{progress_bar}] {stream.filesize - bytes_remaining} / {stream.filesize}", end="\r")




def yt_download(video_url):
    try:
        video = pytube.YouTube(video_url,
                               on_progress_callback=show_progress_bar,
                               on_complete_callback=FileInfo.completed
                               )
        print("Starting Download For: ", video.title)
        print("Preparing To Download")
        video.streams.filter(progressive=True, file_extension=str("mp4")).order_by(
            'resolution').desc().first().download()
    except Exception as UwU:
        return 1


def process(video_url):
    # This Function Checks if you are a playlist
    if "playlist" in video_url:
        play_list = pytube.Playlist(video_url)
        for video in play_list.video_urls:
            yt_download(video)

    else:
        yt_download(video_url)



# Main Program Starts

process(args.video_url)
