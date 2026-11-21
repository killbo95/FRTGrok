# FRT Student Innovation Competition - Face Recognition Prototype

## Overview
This is a complete facial recognition system prototype designed for the Grades 9-10 Facial Recognition Technology (FRT) Student Innovation Competition.

The system demonstrates:
- **Face Detection**: Using Haar Cascade classifiers
- **Face Recognition**: Using LBPH (Local Binary Patterns Histograms) algorithm
- **Enrollment**: Capturing and storing face samples from consenting individuals
- **Real-time Recognition**: Identifying enrolled people from a live camera feed

## Technology Explained

### How Face Detection Works
Haar Cascade is a machine learning-based approach that uses a cascade of simple features (edge, line, rectangle features) to detect faces. The OpenCV implementation includes a pre-trained model for frontal faces.

### How Face Recognition Works
LBPH (Local Binary Patterns Histograms) extracts texture features from face images. It divides the face into regions, computes local binary patterns, and creates histograms. These histograms are compared to identify matches. Lower confidence scores indicate better matches.

### Tools Used
- **OpenCV**: Computer vision library for detection and recognition
- **Python**: Programming language
- **NumPy**: Numerical operations
- Webcam: For live demonstration

## How to Run

### Prerequisites
```bash
pip install opencv-python opencv-contrib-python numpy
```

### Running the Demo
```bash
python face_recognition_demo.py
```

Follow the menu:
1. Enroll people (get consent first!)
2. Train the model
3. Run live recognition

## Project Requirements Alignment

### Working Prototype
✅ Complete face detection and recognition system

### Clear Explanation of Approach
- Haar Cascade for detection (classical computer vision)
- LBPH for recognition (texture-based matching)
- All code is commented and understandable

### Demonstration
- Live webcam demo with consenting volunteers
- Or use test images

### Presentation Points
**Purpose**: Educational demonstration of biometric face recognition technology for school community awareness.

**Strengths**:
- Works offline (privacy-friendly)
- Simple and understandable algorithm
- Real-time performance on standard hardware
- No cloud dependency

**Limitations**:
- Requires good lighting and frontal faces
- Accuracy decreases with different angles, expressions, or aging
- Needs multiple training samples per person
- Can have false positives/negatives

**Possible Errors**:
- False rejection (known person marked as unknown)
- False acceptance (unknown person matched to someone)
- Detection failure in poor lighting or side profiles

### Privacy and Security
- Only uses faces from people who knowingly agreed to participate
- Data stored locally only
- No transmission of biometric data
- Clear consent process before enrollment
- Model and images can be deleted after demo
- School deployment would require additional review and approval

## Competition Notes
- AI tools were used to assist with code structure and documentation
- The student understands the algorithms and can explain every component
- This is an original educational implementation of standard techniques

## Design Responsibly. Create Independently. Explain Confidently.
