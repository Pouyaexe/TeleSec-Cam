import cv2
import winsound
import time
import os
from telegram_bot import send_message_to_telegram,  send_photo_to_telegram  # Import the functions from the other file

# Function to calculate the absolute difference of two frames
def get_frame_difference(frame1, frame2):
    return cv2.absdiff(frame1, frame2)

def main():
    cap = cv2.VideoCapture(0)  # Open webcam (0 is the default webcam device index)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    ret, frame1 = cap.read()  # Read the first frame
    ret, frame2 = cap.read()  # Read the second frame

    cooldown = 0  # Initialize cooldown counter
    cooldown_duration = 10  # Set cooldown duration (e.g., 30 frames)

    # Create a directory to store the images
    os.makedirs('motion_pictures', exist_ok=True)

    while cap.isOpened():
        diff = get_frame_difference(frame1, frame2)  # Get the absolute difference of the two frames
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the difference to grayscale
        blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur to the grayscale image
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # Apply thresholding
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours

        if cooldown > 0:
            cooldown -= 1  # Decrement cooldown counter
        
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  # Get the current timestamp
        file_path = f'motion_pictures/Motion_{timestamp}.jpg'  # Create a unique file path for each image   
           
        # Check for the /capture command
        if os.path.exists('capture_command.txt'):
            print('Capture command detected. File capture_command.txt found.')  # Print a message to the terminal
            os.remove('capture_command.txt')  # Remove the file to acknowledge the command
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f'motion_pictures/Capture_{timestamp}.jpg'
            cv2.putText(frame2, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Add timestamp to frame
            cv2.imwrite(file_path, frame2)  # Save the current frame as a .jpg file with a unique name
            send_photo_to_telegram(file_path)  # Send the photo to Telegram

          

        for contour in contours:
            if cv2.contourArea(contour) > 500 and cooldown == 0:  # If contour area is greater than 500 pixels and cooldown is 0
                winsound.Beep(1000, 500)  # Play a beep sound (frequency=1000 Hz, duration=500 ms)
                cv2.putText(frame2, "Movement Detected", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(frame2, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # Add timestamp to frame
                cv2.imwrite(file_path, frame2)  # Save the current frame as a .jpg file with a unique name
                send_message_to_telegram('Motion detected')  # Send a message to Telegram
                send_photo_to_telegram(file_path)  # Send the photo to Telegram

                cooldown = cooldown_duration  # Reset cooldown counter
                break  # Break after the first detected motion to avoid continuous beeping

        cv2.imshow('Security Cam', frame2)  # Show the frame in a window titled 'Security Cam'

        frame1 = frame2
        ret, frame2 = cap.read()  # Update frames for the next iteration

        if cv2.waitKey(10) == 27:  # Exit if the 'Esc' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
