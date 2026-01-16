# Full Page Screenshot Tool
⚠️Generative AI was used in this project⚠️ 

This is a small Python script that opens a web page, scrolls it from top to bottom, takes screenshots along the way, and stitches them into one long image.

It works on Windows and is useful when you need a full-page capture of a site that does not support native full-page screenshots.

---

## What it does

* Opens a URL in Chrome
* Scrolls the page viewport by viewport
* Takes screenshots at each step
* Combines all screenshots into one image file

---

## Requirements

* Windows
* Python 3.9 or newer
* Google Chrome installed

Python packages:

```
pip install selenium pillow webdriver-manager
```

---

## Usage

Basic usage:

```
python fullpage_screenshot.py https://example.com
```

With options:

```
python fullpage_screenshot.py https://example.com \
  --output page.png \
  --delay 1.0 \
  --headless
```

---

## Arguments

* `url` – URL to capture (required)
* `--output` – Output image filename (default: `full_page.png`)
* `--delay` – Delay between scrolls in seconds (default: `0.6`)
* `--width` – Browser window width (default: `1920`)
* `--height` – Browser window height (default: `1080`)
* `--headless` – Run Chrome without showing the window

---

## Notes

* Some sites use sticky headers; these may repeat in the final image
* Lazy-loaded content may require a longer delay
* Screenshots are temporarily stored in a `screenshots/` folder

---
