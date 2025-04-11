# Telegram Bot Deployment on Render

This is a simple Telegram Bot built with Python Telegram Bot v22. It can be deployed to Render.

## Files
- `bot.py`: Main script for the bot.
- `requirements.txt`: Dependency list.
- `Dockerfile`: Configuration for containerization.

## Deployment Steps
1. **Prepare Code**
   - Clone this repository.
   - Replace `<YOUR_BOT_TOKEN>` with your Telegram Bot Token in the environment variable configuration.

2. **Deploy to Render**
   - Create a new web service on [Render](https://render.com).
   - Connect your GitHub repository.
   - Configure the environment variable `TELEGRAM_BOT_TOKEN` in Render's settings.
   - Deploy the service.

3. **Run and Test**
   - Once deployed, test the bot by sending `/start` and `/help` commands in Telegram.

## Local Testing
- Run the bot locally:
  ```bash
  export TELEGRAM_BOT_TOKEN=<YOUR_BOT_TOKEN>
  python bot.py
  ```