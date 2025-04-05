
.PHONY: all deb appimage exe clean

all: deb appimage exe

deb:
	dpkg-deb --build debian synaptune_1.0.0.deb

appimage:
	appimage-builder --recipe AppImageBuilder.yml

exe:
	pyinstaller synaptune.spec

clean:
	rm -rf build dist __pycache__ synaptune_1.0.0.deb *.spec *.AppImage *.exe
