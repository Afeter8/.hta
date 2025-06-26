#!/bin/bash

echo "🛰️ Iniciando instalación OTA..."
unzip firmware.zip -d /sdcard/update_package/
echo "📲 Reiniciando en modo recovery..."
reboot recovery
