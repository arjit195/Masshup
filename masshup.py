# 1. YouTube Video Downloader
# This function retrieves the top 10 videos based on a search term and saves them to a specified directory.
import yt_dlp
import os

def fetch_youtube_videos(search_term, save_directory="downloaded_content"):
    os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist
    download_options = {
        'format': 'bestvideo[ext=mp4]/bestvideo[ext=webm]/best',
        'noplaylist': True,
        'max_downloads': 10,
        'quiet': True,
        'outtmpl': os.path.join(save_directory, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(download_options) as downloader:
        downloader.download(f"ytsearch10:{search_term}")
    print(f"Downloaded the first 10 videos into: {save_directory}")

# 2. Audio Extraction from Videos
# This function converts video files into audio files and saves them in a separate directory.
import moviepy.editor as mp

def convert_videos_to_audio(video_dir, audio_dir="extracted_audio"):
    os.makedirs(audio_dir, exist_ok=True)
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    for video in video_files:
        video_path = os.path.join(video_dir, video)
        audio_path = os.path.join(audio_dir, f"{os.path.splitext(video)[0]}.wav")
        video_clip = mp.VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path)
        print(f"Extracted audio from {video} to {audio_path}")
    print("All video files have been processed.")

# 3. Extracting Audio While Skipping Initial Portion
# This function skips the first few seconds of the video before extracting audio.
def extract_audio_with_skip(video_dir, audio_dir="audio_with_skip", start_time=30):
    os.makedirs(audio_dir, exist_ok=True)
    video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    for video in video_files:
        video_path = os.path.join(video_dir, video)
        audio_path = os.path.join(audio_dir, f"{os.path.splitext(video)[0]}.wav")
        video_clip = mp.VideoFileClip(video_path).subclip(start_time)
        video_clip.audio.write_audiofile(audio_path)
        print(f"Extracted audio from {video} starting at {start_time} seconds")
    print("Processed all videos with audio extraction after skipping the initial seconds.")

# 4. Concatenating Multiple Audio Files
# This function merges multiple audio files into a single audio file.
def merge_audio_files(audio_dir, merged_file="combined_audio.wav"):
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.wav')]
    audio_clips = [mp.AudioFileClip(os.path.join(audio_dir, audio)) for audio in audio_files]
    final_audio = mp.concatenate_audioclips(audio_clips)
    final_audio.write_audiofile(os.path.join(audio_dir, merged_file))
    print(f"All audio files merged into: {os.path.join(audio_dir, merged_file)}")

# 5. Zipping a File
# This function compresses a specified file into a zip archive.
import zipfile

def compress_file(file_to_compress, zip_destination):
    with zipfile.ZipFile(zip_destination, 'w') as zipf:
        zipf.write(file_to_compress, os.path.basename(file_to_compress))
    print(f"File {file_to_compress} has been compressed into {zip_destination}")

# Example usage:
# fetch_youtube_videos('arijit singh videos', 'video_downloads')
# convert_videos_to_audio('/path/to/videos')
# extract_audio_with_skip('/path/to/videos', start_time=60)
# merge_audio_files('/path/to/audio')
# compress_file('/path/to/audio/combined_audio.wav', '/path/to/audio/combined_audio.zip')
