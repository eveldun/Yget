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
import tkinter


Varg = 1
arguments = argparse.ArgumentParser(prog="yget", description="Converts Your Favorite Songs To Downloaded Format")
arguments.add_argument("VideoUrl", type=str, help="The Video Url")
arguments.add_argument("-f", "--File-format",dest="Data", default="mp4", help="Video File Format: Mp3,Mp4 Default:Mp4")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


Argx = arguments.parse_args()


def completed(stream, file_path):
    Progress = bcolors.OKGREEN + "━━" + bcolors.ENDC
    print("[" + str(Progress * 25) + "] COMPLETED!               ")
    print(bcolors.OKBLUE + stream.title + " Downloaded" + bcolors.ENDC)
    print(bcolors.OKBLUE + "Saved To: " + bcolors.OKGREEN + file_path + bcolors.ENDC)
    return 0


def show_progress_bar(stream, chunk, bytes_remaining):
    sys.stdout.flush()
    Progress = "━━"
    BadSpace = bcolors.OKGREEN + "━━" + bcolors.ENDC
    x = stream.filesize
    BytesDownloaded = x - bytes_remaining
    Percentage = (bytes_remaining / x) * 100
    TFraction = (Percentage / 4)
    Spaces = int(round((25 - TFraction)+0.000000000000000001))
    Spaces = BadSpace * Spaces
    Pr = round(TFraction+0.0000000000000000001) * Progress
    print("[" + str(Spaces) + str(Pr) + "] " + str(x - bytes_remaining) + "/" + str(x) +"                              ", end="\r",flush=True)


def YtConvert(VideoURL, FileFormat2):
    try:
        video = pytube.YouTube(VideoURL,
                               on_progress_callback=show_progress_bar,
                               on_complete_callback=completed
                               )
        print("Downloading ", video.title)
        print("[" + str("━━" * 25) + "] 0/...", end="\r")
        video.streams.filter(progressive=True, file_extension=str(FileFormat2)).order_by(
            'resolution').desc().first().download()
    except Exception as UwU:
        if random.randint(1, 100) != 100:
            print(bcolors.FAIL + "ERROR: Download failed" + bcolors.ENDC)
            print(bcolors.FAIL + str(UwU) + bcolors.ENDC)
            return 1
        else:
            print(
                bcolors.FAIL + """OOPSIE WOOPSIE!! Uwu We make a fucky wucky!! A wittle fucko boingo! \nThe code monkeys at our headquarters are working VEWY HAWD to fix this!""" + bcolors.ENDC)
            return 69 - 68
        print(bcolors.FAIL + "WARNING! a impossible action just occured in this program. Possible Corruption detected!")
        CriticalERR = input("Do you still want to continue? (y,n)")
        while True:
            if CriticalERR.lower().strip() == "yes" or CriticalERR.lower().strip() == "y":
                print("Continuing Program")
                return 1
            elif CriticalERR.lower().strip() == "n" or CriticalERR.lower().strip() == "no":
                print("Exiting Program Immediatly!")
                quit()
            else:
                print("Error")
            print("Critical Error Happened a second time killing program!")
            quit()
def Process(VideoUrl,Format):
    #This Function Checks if you are a playlist
    if "playlist" in VideoUrl:
        play_list = pytube.Playlist(VideoUrl)
        for video in play_list.video_urls:
            YtConvert(video,Format)
    else:
        YtConvert(VideoUrl,Format)


###Main Program Starts###
Process(Argx.VideoUrl, Argx.Data)