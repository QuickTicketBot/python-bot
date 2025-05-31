#!/bin/bash

# Log file path
LOGFILE="/var/www/stop-vnc.log"
exec > >(tee -a "$LOGFILE") 2>&1
echo "=== Stop script started at $(date) ==="

# Stop processes related to display :1
echo "[*] Killing processes using DISPLAY=:1"

# Kill x11vnc
pkill -f "x11vnc -display :1"

# Kill fluxbox
pkill -f "fluxbox"

# Kill Xvfb
pkill -f "Xvfb :1"

echo "[✓] All processes on DISPLAY=:1 stopped."
echo "=== Stop script ended at $(date) ==="
