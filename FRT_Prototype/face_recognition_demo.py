"""
Facial Recognition Technology (FRT) Student Prototype
For Grades 9-10 Innovation Competition

This system demonstrates:
1. Face Detection using Haar Cascade classifier
2. Face Recognition using LBPH (Local Binary Patterns Histograms) algorithm
3. Enrollment of new faces (with consent)
4. Real-time recognition from webcam or images

Requirements: opencv-python, opencv-contrib-python, numpy
Install: pip install opencv-python opencv-contrib-python numpy

Privacy Note: Only use faces of people who have given informed consent.
Do not store or share biometric data without permission.
"""

import cv2
import os
import numpy as np
from datetime import datetime

# Configuration
DATASET_DIR = "dataset"
TRAINER_FILE = "trainer.yml"
CASCADE_FILE = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
NAMES_FILE = "names.txt"

os.makedirs(DATASET_DIR, exist_ok=True)

def load_names():
    """Load enrolled person names"""
    if os.path.exists(NAMES_FILE):
        with open(NAMES_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

def save_names(names):
    """Save enrolled person names"""
    with open(NAMES_FILE, "w") as f:
        for name in names:
            f.write(name + "\n")

def detect_faces(img):
    """Detect faces in an image using Haar Cascade"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(CASCADE_FILE)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces, gray

def enroll_face(name, num_samples=20):
    """Enroll a new person by capturing face samples from webcam"""
    print(f"\n=== Enrolling: {name} ===")
    print("Look at the camera. Press 'c' to capture a sample, 'q' to finish early.")
    print(f"Need about {num_samples} samples for good recognition.")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open webcam. Use image files instead or check camera permissions.")
        return False
    
    count = 0
    person_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(person_dir, exist_ok=True)
    
    while count < num_samples:
        ret, frame = cap.read()
        if not ret:
            break
        
        faces, gray = detect_faces(frame)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Samples: {count}/{num_samples}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow("Enrollment - Press C to capture, Q to quit", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c') and len(faces) > 0:
            # Save the first detected face
            x, y, w, h = faces[0]
            face_img = gray[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (200, 200))
            filepath = os.path.join(person_dir, f"{name}_{count}.jpg")
            cv2.imwrite(filepath, face_img)
            count += 1
            print(f"Captured sample {count}")
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if count > 0:
        print(f"Successfully enrolled {name} with {count} samples.")
        names = load_names()
        if name not in names:
            names.append(name)
            save_names(names)
        return True
    return False

def train_recognizer():
    """Train the LBPH face recognizer on enrolled faces"""
    print("\n=== Training Recognizer ===")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    
    faces = []
    labels = []
    label_map = {}  # name -> id
    current_id = 0
    
    names = load_names()
    if not names:
        print("No enrolled people. Please enroll faces first.")
        return None
    
    for name in names:
        person_dir = os.path.join(DATASET_DIR, name)
        if not os.path.exists(person_dir):
            continue
        label_map[name] = current_id
        for filename in os.listdir(person_dir):
            if filename.endswith(('.jpg', '.png')):
                img_path = os.path.join(person_dir, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    faces.append(img)
                    labels.append(current_id)
        current_id += 1
    
    if len(faces) == 0:
        print("No face images found for training.")
        return None
    
    recognizer.train(faces, np.array(labels))
    recognizer.save(TRAINER_FILE)
    print(f"Training complete! Trained on {len(faces)} images of {len(names)} people.")
    return recognizer, label_map

def recognize_live():
    """Real-time face recognition from webcam"""
    if not os.path.exists(TRAINER_FILE):
        print("No trained model found. Train first!")
        return
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(TRAINER_FILE)
    
    names = load_names()
    id_to_name = {i: name for i, name in enumerate(names)}
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open webcam.")
        return
    
    print("\n=== Live Recognition ===")
    print("Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        faces, gray = detect_faces(frame)
        
        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            face_roi = cv2.resize(face_roi, (200, 200))
            
            label, confidence = recognizer.predict(face_roi)
            
            # Lower confidence is better for LBPH (distance)
            if confidence < 80:  # Threshold - adjust as needed
                name = id_to_name.get(label, "Unknown")
                color = (0, 255, 0)  # Green for recognized
                text = f"{name} ({confidence:.1f})"
            else:
                name = "Unknown"
                color = (0, 0, 255)  # Red for unknown
                text = f"Unknown ({confidence:.1f})"
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        cv2.imshow("Face Recognition - Press Q to quit", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("=" * 50)
    print("FRT Student Innovation Competition Prototype")
    print("Facial Recognition Technology Demo")
    print("=" * 50)
    print("\nIMPORTANT PRIVACY RULES:")
    print("- Only use faces from people who have given informed consent")
    print("- Do not store biometric data without permission")
    print("- This is for educational demonstration only")
    print("- A school-use version must be reviewed and approved")
    
    while True:
        print("\nOptions:")
        print("1. Enroll a new person (capture from webcam)")
        print("2. Train the recognition model")
        print("3. Live face recognition")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            name = input("Enter person's name (first name only): ").strip()
            if name:
                enroll_face(name)
        elif choice == "2":
            train_recognizer()
        elif choice == "3":
            recognize_live()
        elif choice == "4":
            print("Goodbye! Remember: Design responsibly.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
