## Intruder Detection System

This project implements a basic intruder detection system using Python, incorporating computer camera image capture, PushBullet API for push notifications, and user interaction for prompt response.

**Features:**

* **Image Capture:** Captures an image of the potential intruder using the computer's webcam.
* **PushBullet Notifications:** Sends an alert message to the user's mobile device along with the captured image via PushBullet.
* **Voice Alerts:** Plays a voice message to notify the user of a suspected intruder.
* **System Logoff:** If the intruder is confirmed, the system logs off to prevent unauthorized access.
* **IP Address Logging:** Records the IP address of the intruder for potential investigation.

**How it Works:**

1. **User Authentication:** The system prompts the user for a password to verify their identity.
2. **Intruder Detection:** If the incorrect password is entered, the system takes the following actions:
    * Captures an image of the person using the webcam.
    * Sends a push notification with the captured image to the user's mobile device via PushBullet.
    * Plays a voice message alert.
3. **User Confirmation:** The user receives the push notification on their mobile device. They can respond with "Yes" if it is an intruder or "No" if it's a false alarm.
4. **System Action:**  Based on the user's confirmation:
    * **Intruder confirmed:** The system logs off the computer to prevent unauthorized access.
    * **False alarm:**  The system plays a voice message indicating that it's safe.
5. **IP Address Logging:** The system records the IP address of the intruder for potential investigation.

**Dependencies:**

* `cv2` (OpenCV): For image processing and camera interaction.
* `numpy`:  For numerical array manipulation.
* `pushbullet`: To send push notifications via PushBullet API.
* `win32com.client`: For voice alerts using the Windows SAPI.
* `time`:  For pausing execution.
* `os`:  For system commands.
* `socket`: To get the IP address of the current system.
* `json`:  For handling JSON data for IP address logging.
* `datetime`: To record the timestamp of the intrusion.
* `geocoder`: To get the user's location based on the IP address.

**Usage:**

1. **Install Dependencies:**
   ```bash
   pip install opencv-python numpy pushbullet pywin32 geocoder
2. **Replace API Key:** Update the api_key variable in the code with your PushBullet API key.

3. **Run the Script:** Execute the main.py file.
