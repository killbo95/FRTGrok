"""
FRT Student Innovation Competition - Android Prototype
Facial Recognition Technology (Face Detection)

This is a Kivy + OpenCV app designed to be packaged as an Android APK
using Buildozer.

It demonstrates real-time face detection using the device camera.
(Full LBPH recognition can be added later; this version focuses on a
working, explainable detection prototype suitable for the competition.)

Privacy: Only use with consenting volunteers. Face data stays on-device.
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window

import cv2
import numpy as np

class FRTApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.15, 1)
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.title_label = Label(
            text='FRT Prototype\nFace Detection',
            font_size='22sp',
            size_hint=(1, 0.12),
            halign='center'
        )
        self.layout.add_widget(self.title_label)
        
        self.status = Label(
            text='Ready. Tap Start Camera\n(Only use with consenting people)',
            font_size='16sp',
            size_hint=(1, 0.1)
        )
        self.layout.add_widget(self.status)
        
        self.img = Image(size_hint=(1, 0.65))
        self.layout.add_widget(self.img)
        
        btn_layout = BoxLayout(size_hint=(1, 0.13), spacing=10)
        
        self.start_btn = Button(text='Start Camera', background_color=(0.2, 0.6, 0.9, 1))
        self.start_btn.bind(on_press=self.start_camera)
        btn_layout.add_widget(self.start_btn)
        
        self.stop_btn = Button(text='Stop', background_color=(0.8, 0.3, 0.3, 1))
        self.stop_btn.bind(on_press=self.stop_camera)
        btn_layout.add_widget(self.stop_btn)
        
        self.layout.add_widget(btn_layout)
        
        self.capture = None
        self.running = False
        self.face_cascade = None
        
        # Load Haar Cascade (ships with OpenCV)
        try:
            cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
            if self.face_cascade.empty():
                self.status.text = 'Warning: Face detector failed to load'
        except Exception as e:
            self.status.text = f'Detector error: {str(e)[:40]}'
        
        return self.layout
    
    def start_camera(self, instance):
        if self.running:
            return
        
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            self.status.text = 'Could not open camera.\nCheck permissions.'
            return
        
        self.running = True
        self.status.text = 'Detecting faces...'
        Clock.schedule_interval(self.update_frame, 1.0 / 20.0)  # ~20 FPS
    
    def stop_camera(self, instance):
        self.running = False
        Clock.unschedule(self.update_frame)
        if self.capture:
            self.capture.release()
            self.capture = None
        self.status.text = 'Camera stopped'
        self.img.texture = None
    
    def update_frame(self, dt):
        if not self.running or self.capture is None:
            return
        
        ret, frame = self.capture.read()
        if not ret:
            return
        
        # Convert to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = []
        if self.face_cascade is not None and not self.face_cascade.empty():
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(60, 60)
            )
        
        # Draw rectangles and labels
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(
                frame, 'Face',
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 255, 0), 2
            )
        
        self.status.text = f'Faces detected: {len(faces)}'
        
        # Convert frame to Kivy texture
        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = texture
    
    def on_stop(self):
        self.stop_camera(None)

if __name__ == '__main__':
    FRTApp().run()
