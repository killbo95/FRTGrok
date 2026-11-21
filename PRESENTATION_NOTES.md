# Presentation Notes – FRT APK Prototype

## 1. Purpose
Educational demonstration of facial detection technology for the school community. Shows how a simple biometric system works on a mobile device.

## 2. How it works (30-second explanation)
- The phone camera feeds video frames to the app.
- OpenCV’s Haar Cascade looks for facial features.
- When a face is found, a green box is drawn around it.
- The count of faces is shown on screen.
- All processing happens locally on the phone.

## 3. Strengths
- Offline and private
- Real-time
- Easy to understand and explain
- No cloud or account required

## 4. Limitations & Possible Errors
- Needs decent lighting and a mostly frontal face
- Can miss faces that are turned sideways or partially covered
- May draw a box on something that is not a face (false positive)
- Does not identify *who* the person is (detection only)

## 5. Privacy
- Only use with volunteers who agree
- No photos are stored
- Data never leaves the device
- Not intended for real surveillance or school deployment without further review

## 6. Demo tips
- Ask a friend for permission first
- Hold the phone steady
- Show both “face found” and “no face” cases
- Mention that full recognition (naming people) is possible with more training data and LBPH, but this version focuses on clear, reliable detection
