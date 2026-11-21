[app]
android.accept_sdk_license = True
title = FRT Face Detection
package.name = frtface
package.domain = org.school.frt
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,opencv,numpy
orientation = portrait
fullscreen = 0
android.permissions = CAMERA
android.api = 31
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a,armeabi-v7a
