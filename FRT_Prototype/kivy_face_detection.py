"""
Kivy + OpenCV Face Detection App (for APK packaging with Buildozer)
This is a simplified version focused on face detection for mobile demonstration.
Full recognition can be added similarly.

To build APK:
1. Install Buildozer: pip install buildozer
2. On Linux: buildozer init (or use the provided spec)
3. buildozer android debug

Note: Building requires Android SDK/NDK (downloaded automatically) and may take 30+ minutes and several GB of space.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import numpy as np

class FaceDetectionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.status = Label(text='FRT Prototype - Face Detection\nPress Start to begin', size_hint=(1, 0.2))
        self.layout.add_widget(self.status)
        
        self.img = Image(size_hint=(1, 0.6))
        self.layout.add_widget(self.img)
        
        self.btn = Button(text='Start Camera', size_hint=(1, 0.2))
        self.btn.bind(on_press=self.toggle_camera)
        self.layout.add_widget(self.btn)
        
        self.capture = None
        self.running = False
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        return self.layout
    
    def toggle_camera(self, instance):
        if not self.running:
            self.capture = cv2.VideoCapture(0)
            if self.capture.isOpened():
                self.running = True
                self.btn.text = 'Stop Camera'
                self.status.text = 'Detecting faces... (get consent first!)'
                Clock.schedule_interval(self.update, 1.0/30.0)
            else:
                self.status.text = 'Could not open camera'
        else:
            self.running = False
            self.btn.text = 'Start Camera'
            if self.capture:
                self.capture.release()
            Clock.unschedule(self.update)
            self.status.text = 'Camera stopped'
    
    def update(self, dt):
        if self.capture and self.running:
            ret, frame = self.capture.read()
            if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, 'Face Detected', (x, y-10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Convert to texture for Kivy
                buf = cv2.flip(frame, 0).tobytes()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
                self.img.texture = texture
                
                self.status.text = f'Faces detected: {len(faces)}'

if __name__ == '__main__':
    FaceDetectionApp().run()
