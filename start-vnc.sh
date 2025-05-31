#!/bin/bash

# Set up logging
LOGFILE="/var/www/start-vnc.log"
exec > >(tee -a "$LOGFILE") 2>&1
echo "=== Script started at $(date) ==="

# Your commands
export DISPLAY=:1
Xvfb :1 -screen 0 1280x720x24 &
sleep 2
fluxbox &
x11vnc -display :1 -nopw -forever -shared -rfbport 5901 &

echo "=== Script ended at $(date) ==="
