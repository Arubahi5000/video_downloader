
# 🎵 Video Downloader Script (Multithreaded with `yt-dlp`)

A Python script to download videos from URLs listed in a CSV file using `yt-dlp` and multithreading. Each video is saved with a custom filename derived from the song name provided.

## 📁 About

This script reads a CSV file (`songs.csv`) containing song names and YouTube (or other supported platform) URLs. It downloads each video using `yt-dlp`, saving it with the song name as the filename. The downloading process is multithreaded to speed up execution.

---

## ⚙️ Features

- 🔁 Multithreaded for faster downloads
- 🎯 Custom output filenames based on song names
- 🛑 Automatically skips files that already exist
- 📦 Cleanly structured and easy to customize

---

## 📄 CSV Format

The `songs.csv` file should be in the following format:

```csv
Song Name,URL
Song One,https://youtube.com/example1
Song Two,https://youtube.com/example2
```

Make sure the first row is a header (it will be skipped).

---

## 🚀 Requirements

- Python 3.6 or higher
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

Install `yt-dlp` via pip if you haven't already:

```bash
pip install yt-dlp
```

---

## 🧠 How It Works

1. Reads song names and video URLs from `songs.csv`
2. Creates a thread-safe queue of download tasks
3. Launches multiple threads to process the queue concurrently
4. Uses `yt-dlp` to download each video with the song name as filename
5. Skips downloads if the file already exists

---

## ▶️ Usage

```bash
python3 downloader.py
```

Ensure your `songs.csv` is in the same directory as the script.

---

## 📝 Notes

- Default number of threads is `4`. You can change it by modifying the `NUM_THREADS` constant in the script.
- Output videos are saved in `.mp4` format (default from `yt-dlp` based on the site's stream).

---

## 🧑‍💻 Author

**Aryan Bahinipati**  
[GitHub](https://github.com/yourusername)  
April 22, 2025

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
