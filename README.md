# FRT Student Innovation Competition
## Android Face Detection Prototype (APK)

**Grades 9–10 | Facial Recognition Technology**

### What this project is
A working Android app that detects faces in real time using the phone’s camera.  
It is designed to be built into an **APK** with Buildozer (Python-for-Android).

### How the system works
1. **Camera** captures live video from the device.
2. **Haar Cascade classifier** (classic computer-vision method) scans each frame for faces.
3. **Bounding boxes** are drawn around detected faces.
4. Everything runs **on the device** — no internet or cloud required.

### Tools used
- **Kivy** – mobile user interface
- **OpenCV** – face detection (Haar Cascade)
- **Buildozer** – packages the app into an Android APK

### Strengths
- Works offline (good for privacy)
- Real-time on a normal phone
- Simple and explainable algorithm
- Clear visual feedback (green boxes + face count)

### Limitations
- Works best with frontal faces and good lighting
- Detection only (not full recognition of specific people in this version)
- Accuracy drops with side angles, masks, or very low light
- Requires camera permission

### Privacy & Responsible Design
- Only demonstrate with people who have given clear consent
- No face images are saved or uploaded
- All processing stays on the phone
- Suitable for a controlled school demonstration
- A school-deployed version would need extra review and approval

### How to build the APK
On a Linux computer (or Ubuntu WSL / VM):

```bash
# Install dependencies (one time)
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip \
  autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
  cmake libffi-dev libssl-dev
pip install buildozer cython

# Build
cd FRT_APK_Project
buildozer android debug
```

The finished APK will be in the `bin/` folder.  
Transfer it to your phone and install (you may need to allow “Install from unknown sources”).

### Competition alignment
- Working prototype ✔
- Clear explanation of approach ✔
- Live demonstration possible ✔
- Strengths, limitations, and errors discussed ✔
- Privacy and security considered ✔

**Design responsibly. Create independently. Explain confidently.**
