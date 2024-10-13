# Multimedia Processing Python Project

This Python project provides a set of tools for multimedia processing, specifically focusing on downloading videos, extracting audio, and merging files. The project leverages popular libraries like `yt-dlp` and `moviepy` to perform these tasks efficiently.

## Features

1. **YouTube Video Downloader**  
   Downloads the top 10 videos based on a search query using the `yt-dlp` library and saves them to a specified directory.
   
2. **Audio Extraction from Videos**  
   Converts video files (e.g., `.mp4`, `.mkv`, `.avi`, `.mov`) into audio files (`.wav`) using the `moviepy` library. Useful for extracting soundtracks, lectures, or audio from media content.

3. **Partial Audio Extraction**  
   Extracts audio after skipping the initial segment of the video, allowing for flexible audio processing (e.g., skipping intros or ads in videos).

4. **Audio Concatenation**  
   Merges multiple audio files into one single audio file. Ideal for combining podcast episodes, lectures, or music tracks into a seamless file.

5. **File Compression**  
   Compresses specified files into a `.zip` format for easier sharing and storage.

## Dependencies

- `yt-dlp` - For downloading YouTube videos.
- `moviepy` - For video and audio processing.
- `os`, `zipfile` - For file and directory handling, compression.

## Installation

To install the necessary libraries, use the following command:

```bash
pip install yt-dlp moviepy
