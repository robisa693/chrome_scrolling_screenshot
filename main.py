import os
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

# =====================
# Argument parsing
# =====================
parser = argparse.ArgumentParser(
    description="Scroll a web page, capture viewport screenshots, and stitch them into one image."
)
parser.add_argument("url", help="Target URL")
parser.add_argument("--output", default="full_page.png", help="Output image filename")
parser.add_argument("--delay", type=float, default=0.6, help="Delay between scrolls (seconds)")
parser.add_argument("--width", type=int, default=1920, help="Browser window width")
parser.add_argument("--height", type=int, default=1080, help="Browser window height")
parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")

args = parser.parse_args()

# =====================
# Configuration
# =====================
OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================
# Selenium setup
# =====================
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")

if args.headless:
    chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.set_window_size(args.width, args.height)
driver.get(args.url)
time.sleep(2)

# =====================
# Page dimensions
# =====================
total_height = driver.execute_script("return document.body.scrollHeight")
viewport_height = driver.execute_script("return window.innerHeight")

screenshots = []
scroll_position = 0
index = 0

# =====================
# Scroll and capture
# =====================
while scroll_position < total_height:
    filename = f"{OUTPUT_DIR}/part_{index}.png"
    driver.save_screenshot(filename)
    screenshots.append(filename)

    scroll_position += viewport_height
    driver.execute_script(f"window.scrollTo(0, {scroll_position});")
    time.sleep(args.delay)

    index += 1

driver.quit()

# =====================
# Stitch images
# =====================
images = [Image.open(img) for img in screenshots]

width = images[0].width
total_height = sum(img.height for img in images)

final_image = Image.new("RGB", (width, total_height))

y_offset = 0
for img in images:
    final_image.paste(img, (0, y_offset))
    y_offset += img.height

final_image.save(args.output)

print(f"Saved stitched screenshot to: {args.output}")
