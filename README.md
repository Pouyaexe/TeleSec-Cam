
`TeleSec-Cam`

![Pic](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*6w87eM4Yx2jDfwHC4a7wFw.png)


# TeleSec-Cam

TeleSec-Cam is a security camera system powered by a Python script that utilizes a webcam to monitor a space for motion. When motion is detected, alerts are sent to specified users via a Telegram bot. Users can also interact with the bot to receive live captures on demand.

## Check out the [Medium article on this Project!](https://medium.com/@pouyahallaj/diy-telegram-security-cam-with-python-a807766153e8)

## Features
- Motion detection using a webcam.
- Real-time alerts sent to Telegram.
- Live capture on demand via Telegram bot commands.
- User management to control who can receive alerts and request captures.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/TeleSec-Cam.git
   cd TeleSec-Cam
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Configuration:**
   Create a `config.py` file with your Telegram bot token and admin user ID:

   ```python
   BOT_TOKEN = "your-telegram-bot-token"
   TELEGRAM_USER_ID = your-telegram-user-id  # Replace with your numeric Telegram user ID
   ```

   You can use the `config_template.py` file and rename it to `config.py`
4. **Run the Application:**

   ```bash
   python main.py
   ```

## Usage

- Run the `main.py` script to start both the Telegram bot and the security cam.
- Interact with the Telegram bot to receive motion alerts, request live captures, and manage users.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

MIT

