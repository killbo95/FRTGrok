# Presentation Outline for FRT Competition

## Slide 1: Title
Facial Recognition Technology (FRT) Prototype
Student Innovation Competition | Grades 9-10
[Your Name / Team Name]

## Slide 2: The Challenge
- Create a biometric face-recognition system
- Detect and recognize faces in a controlled demonstration
- Show how it works, explain the technology, demonstrate responsible design

## Slide 3: Our Approach
- **Detection**: Haar Cascade classifier (classical computer vision)
- **Recognition**: LBPH algorithm (Local Binary Patterns Histograms)
- **Tools**: Python + OpenCV
- **Why this approach**: Understandable, offline, educational, privacy-friendly

## Slide 4: How It Works
1. **Enrollment**: Capture multiple face samples from consenting person
2. **Training**: Extract features and build recognition model
3. **Recognition**: Compare live face against trained model
4. **Output**: Name + confidence score, or "Unknown"

## Slide 5: Live Demonstration
[Show the working prototype]
- Enroll a volunteer (with consent)
- Train the model
- Recognize in real-time

## Slide 6: Strengths
- Works completely offline
- No cloud dependency (better privacy)
- Real-time on standard hardware
- Simple algorithms students can explain
- Educational value

## Slide 7: Limitations & Possible Errors
- Requires good lighting and frontal faces
- Performance drops with side angles or expressions
- False positives/negatives possible
- Needs multiple training samples
- Not as accurate as modern deep learning systems

## Slide 8: Privacy & Security
- Only uses faces from people who knowingly agreed
- Data stored locally only
- No transmission of biometric information
- Clear consent process
- Can delete all data after demonstration
- School deployment requires additional review and approval

## Slide 9: Positive Contribution
- Helps school community understand biometric technology
- Demonstrates responsible AI/ML design principles
- Educational tool for learning computer vision
- Shows both capabilities and limitations of FRT

## Slide 10: Conclusion
Design responsibly. Create independently. Explain confidently.
Questions?
