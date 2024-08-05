from flask import Flask
from PIL import ImageGrab
import time
import threading
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Screenshot service is running."

def take_screenshot():
    serial_number = 1
    while True:
        screenshot = ImageGrab.grab()
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        today_date = datetime.today().strftime('%Y-%m-%d')
        directory = f"images/{today_date}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{directory}/screenshot_{serial_number}_{timestamp}.png"
        screenshot.save(filename)
        serial_number += 1
        time.sleep(1)  # Take a screenshot every second

if __name__ == '__main__':
    threading.Thread(target=take_screenshot).start()
    app.run(debug=True, port=9000)
