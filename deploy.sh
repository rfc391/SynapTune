#!/bin/bash

echo "[*] Installing SynapTune..."
pip install .

echo "[*] Building .deb package..."
dpkg-deb --build debian synaptune_1.0.0.deb

echo "[*] Building AppImage..."
appimage-builder --recipe AppImageBuilder.yml

echo "[*] Building .exe with PyInstaller..."
pyinstaller synaptune.spec

echo "[*] Building documentation..."
mkdocs build

echo "[*] Deploying documentation to GitHub Pages..."
mkdocs gh-deploy --force

echo "[*] SynapTune is fully built and deployed."
