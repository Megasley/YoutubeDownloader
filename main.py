from pytube import YouTube
import sys

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    sys.stdout.write(f"\rDownloading: {int(percentage_of_completion)}%")
    sys.stdout.flush()

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")

    # Create YouTube object with progress callback
    yt = YouTube(url, on_progress_callback=progress_function)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video to the specified directory
    stream.download("/Users/User/Desktop/Youtube Downloads")

    print("\nDownload complete.")
except Exception as e:
    print("An error occurred:", str(e))
