import cv2
import numpy as np

# Load the image
image_path = 'sama.png'  # Make sure to replace this with your image's path
image = cv2.imread(image_path)

# Load a pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert the image to grayscale (necessary for face detection)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Crop the first detected face (if multiple faces are present, it takes the first one)
for (x, y, w, h) in faces:
    face = image[y:y+h, x:x+w]
    break  # Only take the first detected face for simplicity

# Save the cropped face
cv2.imwrite('sama_face.png', face)

print("Cropped face saved as 'sama_face.png'")
