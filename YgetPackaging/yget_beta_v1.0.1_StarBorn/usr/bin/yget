#!/usr/bin/env python3
##################################################
# Yget - Open Source YouTube Video Installer
# Version: 1.0.1 - Development Build (Code Name StarBorn)
# Credits: Install Location
# Purpose: Sick of not being able to right-click YouTube videos Download them with Yget
##################################################
import argparse
import random
import sys
import pytube

Varg = 1
arguments = argparse.ArgumentParser(prog="yget", description="Converts Your Favorite Songs To Downloaded Format")
arguments.add_argument("video_url", type=str, help="The Video Url")
arguments.add_argument("-f", "--File-format_s", dest="Data", default="mp4",
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


Argx = arguments.parse_args()


def completed(stream, file_path):
    progress = Bcolors.OKGREEN + "━━" + Bcolors.ENDC
    print("[" + str(progress * 25) + "] COMPLETED!               ")
    print(Bcolors.OKBLUE + stream.title + " Downloaded" + Bcolors.ENDC)
    print(Bcolors.OKBLUE + "Saved To: " + Bcolors.OKGREEN + file_path + Bcolors.ENDC)
    return 0


def show_progress_bar(stream, chunk,bytes_remaining):
    sys.stdout.flush()
    progress = "━━"
    bad_space = Bcolors.OKGREEN + "━━" + Bcolors.ENDC
    x = stream.filesize
    percentage = (bytes_remaining / x) * 100
    t_fraction = (percentage / 4)
    spaces = int(round((25 - t_fraction) + 0.000000000000000001))
    spaces = bad_space * spaces
    pr = round(t_fraction + 0.0000000000000000001) * progress
    print(
        "[" + str(spaces) + str(pr) + "] " + str(x - bytes_remaining) + "/" + str(x) + "                              ",
        end="\r", flush=True)


def yt_convert(video_url, file_format2):
    try:
        video = pytube.YouTube(video_url,
                               on_progress_callback=show_progress_bar,
                               on_complete_callback=completed
                               )
        print("Downloading ", video.title)
        print("[" + str("━━" * 25) + "] 0/...", end="\r")
        video.streams.filter(progressive=True, file_extension=str(file_format2)).order_by(
            'resolution').desc().first().download()
    except Exception as UwU:
        if random.randint(1, 100) != 100:
            print(Bcolors.FAIL + "ERROR: Download failed" + Bcolors.ENDC)
            print(Bcolors.FAIL + str(UwU) + Bcolors.ENDC)
            return 1
        else:
            print(
                Bcolors.FAIL + """OOPSIE WOOPSIE!! Uwu We make a fucky wucky!! A wittle fucko boingo! \nThe code 
                monkeys at our headquarters are working VEWY HAWD to fix this!""" + Bcolors.ENDC)
            return 69 - 68


def process(video_url, format_s):
    # This Function Checks if you are a playlist
    if "playlist" in video_url:
        play_list = pytube.Playlist(video_url)
        for video in play_list.video_urls:
            yt_convert(video, format_s)
    else:
        yt_convert(video_url, format_s)


# Main Program Starts
process(Argx.video_url, Argx.Data)
