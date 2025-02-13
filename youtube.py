from pytube import YouTube

def download_youtube_video(url, output_path=None):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Print video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Length: {yt.length} seconds")
        print(f"Downloading the highest quality video...")

        # Download the video
        video_stream.download(output_path=output_path)
        print(f"Download completed! Video saved to: {output_path if output_path else 'current directory'}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Optional: Specify the output directory (leave blank for current directory)
    output_directory = input("Enter the output directory (leave blank for current directory): ").strip() or None

    # Call the download function
    download_youtube_video(video_url, output_directory)
