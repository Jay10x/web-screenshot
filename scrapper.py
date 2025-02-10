from playwright.sync_api import sync_playwright
from PIL import Image


# URL of the website
url = 'https://coinmarketcap.com/charts/fear-and-greed-index/'


output_file = 'screenshot.png'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_viewport_size({"width": 1280, "height": 600})  
    page.goto(url)
    page.wait_for_timeout(5000) 
    page.screenshot(path=output_file, full_page=True)
    browser.close()
    
screenshot_file = 'screenshot.png'
cropped_file = 'cropped_screenshot.png'

with Image.open(screenshot_file) as img:

    width, height = img.size
    print(width, height)
    crop_area = (0, 0, width, height - 1600)  
    cropped_img = img.crop(crop_area)
    cropped_img.save(cropped_file)
print(f"Cropped image saved as {cropped_file}")