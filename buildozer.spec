[app]
title = Nasih
package.name = nasih
package.domain = org.nasih
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.11.1
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
# Java sürümünü 11 olarak sabitliyoruz (Buildozer API 31+ için Java 11 gerektirir)
android.gradle_dependencies = 
android.add_jars = 
android.presplash_color = #FFFFFF
