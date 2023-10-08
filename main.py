import multiprocessing
import telegram_bot  # Assume telegram_bot.py is in the same directory
import security_cam  # Assume security_cam.py is in the same directory

def run_telegram_bot():
    telegram_bot.bot.polling(none_stop=True)

def run_security_cam():
    security_cam.main()

if __name__ == "__main__":
    # Create separate processes for the Telegram bot and the security camera
    telegram_process = multiprocessing.Process(target=run_telegram_bot)
    security_cam_process = multiprocessing.Process(target=run_security_cam)
    
    # Start both processes
    telegram_process.start()
    security_cam_process.start()
    
    # Wait for both processes to finish (they won't, since they loop forever)
    telegram_process.join()
    security_cam_process.join()
