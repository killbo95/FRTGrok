[app]
title = FRT Face Detection
package.name = frtface
package.domain = org.school.frt
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 1.0

requirements = python3==3.10.12,kivy,opencv,numpy==1.24.4
orientation = portrait
fullscreen = 0

android.permissions = CAMERA
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
