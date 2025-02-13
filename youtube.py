import os
from pytube import YouTube
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_youtube_video(url, output_path=None):
    """
    Downloads a YouTube video from the given URL to the specified output path.

    Args:
        url (str): The URL of the YouTube video.
        output_path (str, optional): The directory where the video will be saved. Defaults to None (current directory).

    Returns:
        None
    """
    try:
        # Validate URL
        if not url.startswith("https://www.youtube.com/"):
            raise ValueError("Invalid YouTube URL. Please provide a valid YouTube video link.")

        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Log video details
        logging.info(f"Title: {yt.title}")
        logging.info(f"Views: {yt.views}")
        logging.info(f"Length: {yt.length} seconds")
        logging.info("Downloading the highest quality video...")

        # Set output path
        if output_path and not os.path.exists(output_path):
            os.makedirs(output_path)
            logging.info(f"Created directory: {output_path}")

        # Download the video with progress bar
        def on_progress(stream, chunk, bytes_remaining):
            current = ((stream.filesize - bytes_remaining) / stream.filesize)
            progress_bar.update(current - progress_bar.n)

        yt.register_on_progress_callback(on_progress)
        progress_bar = tqdm(total=1, unit='B', unit_scale=True, desc=yt.title)

        video_stream.download(output_path=output_path)

        progress_bar.close()
        logging.info(f"Download completed! Video saved to: {output_path if output_path else 'current directory'}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input YouTube video URL
    video_url = input("Enter the YouTube video URL: ").strip()

    # Optional: Specify the output directory (leave blank for current directory)
    output_directory = input("Enter the output directory (leave blank for current directory): ").strip() or None

    # Call the download function
    download_youtube_video(video_url, output_directory)
