# Saat – Minimal Floating Clock

**Pure Python. Zero Dependencies. Clean and Minimal.**

Saat is an ultra-lightweight digital clock that floats on your desktop with no window frame and a fully transparent background. It is written using only Python’s standard library, with no third-party dependencies.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square\&logo=python)
![Size](https://img.shields.io/badge/Size-Tiny-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

## ✨ Features

* **No Dependencies:** No `pip install` required. Uses only Python and `tkinter` (included by default).
* **Borderless & Transparent:** No window frame, title bar, or background — only the time is visible.
* **Always on Top:** Stays visible above other windows.
* **Draggable:** Move the clock anywhere on the screen despite having no window frame.
* **Lightweight:** Minimal CPU and memory usage.

## 🚀 Installation & Run

You only need Python installed on your system.

1. Clone the repository or download it as a ZIP:

   ```bash
   git clone https://github.com/ibodeth/Saat.git
   cd Saat
   ```

2. Run the script:

   ```bash
   python main.py
   ```


## 🖱️ Controls

Since there is no traditional UI, interactions are handled via mouse actions:

| Action                | Result                                |
| --------------------- | ------------------------------------- |
| **Left Click + Drag** | Move the clock anywhere on the screen |
| **Right Click**       | Exit the application                  |

## 🔧 Technical Details

* **Platform:** Windows (transparency is optimized for the Windows window manager)
* **Libraries:** `tkinter`, `time`
* **Font:** Consolas (falls back to a default monospace font if unavailable)

## 📄 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it.
