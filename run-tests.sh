#!/bin/bash

set -xe

Xvfb :1 -screen 0 1024x768x16 &> /var/log/xvfb.log &
export DISPLAY=:1.0

# Enable Assistive Technology support
gsettings set org.gnome.desktop.interface toolkit-accessibility true

behave

