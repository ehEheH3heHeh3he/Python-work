import cv2

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video from the default webcam (index 0)
cap = cv2.VideoCapture(0)

detected_face_positions = []  # To store the positions of detected faces

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale (Haar Cascade works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Clear the list before adding new detections
    detected_face_positions.clear()

    # Check if at least two faces are detected
    if len(faces) >= 2:
        for i, (x, y, w, h) in enumerate(faces):
            if i < 2:
                detected_face_positions.append((x, y, w, h))  # Store the position of each detected face
                # Draw rectangles around the detected faces
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    else:
        print("Less than two faces detected.")

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()

# Print the positions of the detected faces
print("Detected face positions:", detected_face_positions)
# In this code, the detected_face_positions list is cleared on each iteration of the loop to store fresh detections in the current frame. The list will hold the (x, y, w, h) values for both detected faces, allowing you to print or further process their positions after the program finishes.





