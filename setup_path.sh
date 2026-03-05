#!/bin/bash

# 1. Deteksi folder root project (lokasi script ini berada)
PROJECT_ROOT=$(pwd)

# 2. Cari di mana python venv berada
# Kita asumsikan folder venv bernama 'venv' atau '.venv'
if [ -d "venv" ]; then
    VENV_PATH="venv"
elif [ -d ".venv" ]; then
    VENV_PATH=".venv"
else
    echo "❌ Error: Folder venv tidak ditemukan! Pastikan kamu sudah membuat venv."
    exit 1
fi

# 3. Cari folder site-packages di dalam venv
# Ini akan mendeteksi versi python secara otomatis (misal python3.10, 3.11, dll)
SITE_PACKAGES=$(find $VENV_PATH -name "site-packages" -type d | head -n 1)

if [ -z "$SITE_PACKAGES" ]; then
    echo "❌ Error: Folder site-packages tidak ditemukan di dalam $VENV_PATH."
    exit 1
fi

# 4. Buat file .pth dan masukkan path project root
echo "$PROJECT_ROOT" > "$SITE_PACKAGES/project_root.pth"

echo "✅ Berhasil!"
echo "📍 Project Root: $PROJECT_ROOT"
echo "📂 Ditulis ke: $SITE_PACKAGES/project_root.pth"
echo "🚀 Sekarang kamu bisa 'import src' dari mana saja di dalam venv ini."
