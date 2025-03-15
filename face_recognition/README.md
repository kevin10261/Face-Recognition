# Face Recognition Project

This project demonstrates a simple face recognition system using Python. The system can detect and recognize faces from images and live video streams. It utilizes the `face_recognition` library for face detection and recognition, and `opencv` for handling image and video processing.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [Acknowledgements](#acknowledgements)

## Usage

1. **Download Celebrity Images:**
    Run the `webscrape.py` script to download images of celebrities listed in `celebrities.txt` (auto-generated using ChatGPT):
    ```sh
    python webscrape.py
    ```

2. **Run Face Recognition:**
    Run the `main.py` script to start the face recognition system:
    ```sh
    python main.py
    ```

## Project Structure

```
face_recognition/
├── README.md
├── celebrities.txt
├── main.py
├── requirements.txt
├── simple_facerec.py
├── webscrape.py
└── celebs/  # Directory where downloaded images will be stored
```

## Code Explanation

### `webscrape.py`
This script downloads images of celebrities from Google Images using Google Cloud and Google Search Engine. It reads celebrity names from `celebrities.txt` and saves the images in the `celebs` directory.

### `simple_facerec.py`
This script contains the `SimpleFacerec` class, which handles loading face encodings from images and detecting known faces in a given frame.

- `load_encoding_images(images_path)`: Loads and encodes images from the specified path.
- `detect_known_faces(frame)`: Detects and recognizes known faces in the given frame.

### `main.py`
This script initializes the camera and uses the `SimpleFacerec` class to detect and recognize faces in real-time.

## Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition) - The world's simplest facial recognition API for Python and the command line.
- [opencv](https://opencv.org/) - Open Source Computer Vision Library.
- [google_images_search](https://github.com/arrrlo/google-images-search) - Python library to search and download images from Google.
- ChatGPT - Used to auto-generate celebrity names for `celebrities.txt`.

