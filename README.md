# 🖼️ Batch Image Watermarker (Day 9)

A Python automation tool that applies a custom text watermark to all images in a folder. It uses the **Pillow (PIL)** library to draw semi-transparent text on photos to protect copyright or branding.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Batch Processing:** Processes hundreds of images in seconds.
* **Smart Positioning:** Automatically calculates the bottom-right corner, regardless of image size.
* **Custom Styling:**
    * Adjustable text transparency (Opacity).
    * Custom font support (TTF).
    * Auto-scaling text size based on image resolution.
* **Non-Destructive:** Saves watermarked copies to a new folder, keeping originals safe.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Library:** `Pillow` (Python Imaging Library Fork).

## ⚙️ Installation

### 1. Install Dependencies
```bash
pip install Pillow