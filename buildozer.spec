[app]
title = FRT Face Detection
package.name = frtface
package.domain = org.school.frt
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.0
requirements = python3,kivy,opencv,numpy
orientation = portrait
fullscreen = 0

# Android settings
android.permissions = CAMERA
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# Optional: reduce size
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 0
