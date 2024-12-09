import numpy as np
import cv2

# Open video
cap = cv2.VideoCapture('https://wv-cdn-00-00.wowza.com/06ae7cb0-07d1-414b-b902-e297d69d5284/v-96522659-7c64-4dca-a0d8-3770b04be367.mp4')  # Frame size: 852x480

# Define the line position
line_x = 410  # X-coordinate of the vertical line
object_count = 0  # Initialize counter for objects passing the line

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Get the frame's dimensions
        height, width = frame.shape[:2]

        # Define the crop dimensions for the bottom-right corner
        crop_width = width
        crop_height = height // 2 -20
        x_start = width - crop_width
        y_start = height - crop_height

        # Crop the frame (bottom-right)
        frame_cropped = frame[y_start:, x_start:]

        # Convert to grayscale
        gray_frame = cv2.cvtColor(frame_cropped, cv2.COLOR_BGR2GRAY)

        # Apply threshold
        _, result = cv2.threshold(gray_frame, 120, 255, cv2.THRESH_BINARY_INV)

        # Apply operations
        kernel = np.ones((9, 9), np.uint8)
        closing = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel, iterations=2)
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=2)

        # Draw the line
        cv2.line(frame_cropped, (line_x, 0), (line_x, crop_height), (0, 0, 255), 5)

        # Find contours in the processed image
        contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # Loop through contours to check for crossing objects
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000 and area < 50000:  # Ignore small areas
                x, y, w, h = cv2.boundingRect(contour)

                # Calculate the center of the bounding box
                center_x = x + w // 2

                # Check if the center crosses the line with a larger tolerance
                if line_x - 20 <= center_x <= line_x + 20:  # Increased tolerance to ±20 pixels
                    object_count += 1  # Increment object count

                # Draw bounding box and center
                cv2.rectangle(frame_cropped, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame_cropped, (center_x, y + h // 2), 5, (255, 0, 0), -1)

        # Display the object count on the frame
        cv2.putText(
            frame_cropped, f"Objects Passed: {object_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2
        )

        # Show the processed cropped frame
        cv2.imshow('Bottom-Right Frame', frame_cropped)

        # Break the loop on 'q' key press
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Print final count
print(f"Total objects passed the line: {object_count}")
