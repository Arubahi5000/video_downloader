#!/usr/bin/env python3
"""
Video Downloader Script using yt-dlp and Multithreading

Author: Aryan Bahinipati
Date: April 22, 2025
Description:
    This script reads a list of song names and video URLs from a CSV file (songs.csv),
    and uses multiple threads to download the videos using yt-dlp.
    Each video is saved with its corresponding song name as the filename.

Requirements:
    - yt-dlp
    - Python 3.6+
"""

import csv
import os
import threading
import subprocess
from queue import Queue

# Constants
CSV_FILENAME = "songs.csv"
NUM_THREADS = 4

# Thread-safe queue to hold (url, output_filename) tuples
url_queue = Queue()

def load_urls_from_csv(filename):
    """
    Load URLs and corresponding song names from the given CSV file.
    Adds (url, output_filename) tuples to the queue.
    """
    with open(filename, "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            song_name, url = row
            output_filename = f"/output/{song_name}.mp4"
            url_queue.put((url, output_filename))

def download_video():
    """
    Worker function that downloads videos from URLs in the queue.
    Skips files that already exist.
    """
    while not url_queue.empty():
        url, output_filename = url_queue.get()
        try:
            if os.path.exists(output_filename):
                print(f"[SKIP] {output_filename} already exists.")
                continue
            print(f"[DOWNLOAD] {output_filename} from {url}")
            subprocess.run(["yt-dlp", "-f", "bestvideo[ext=mp4][vcodec=avc1]+bestaudio[ext=m4a]/best", "--merge-output-format", "mp4", "--recode-video", "mp4", "-o", output_filename, url])
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to download {url}: {e}")
        finally:
            url_queue.task_done()

def main():
    """Main function to orchestrate loading URLs and starting threads."""
    load_urls_from_csv(CSV_FILENAME)

    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=download_video)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("✅ All downloads completed!")

if __name__ == "__main__":
    main()
