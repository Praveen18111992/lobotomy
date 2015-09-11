#!/bin/sh

# Upgrade PIP
pip2.7 install --upgrade pip

# Install requirements
echo "[*] Installing requirements"
pip2.7 install -r requirements

# Download Androguard
echo "[*] Cloning androguard"
git clone https://github.com/androguard/androguard.git

# Setup Androguard
cd androguard
git checkout 1.9
python setup.py install
cd ..

# Download and build apktool
echo "[*] Downloading and building the apktool "
git clone git://github.com/iBotPeaches/Apktool.git
cd Apktool
./gradlew build fatJar
mv brut.apktool/apktool-cli/build/libs/apktool-cli.jar ../apktool.jar
cd ..
rm -rf Apktool/

# Download and unzip dex2jar
echo "[*] Downloading dex2jar"
wget https://bitbucket.org/pxb1988/dex2jar/downloads/dex2jar-2.0.zip
unzip dex2jar-2.0.zip
rm dex2jar-2.0.zip
chmod +x dex2jar-2.0/*

# Download frida-server
echo "[*] Downloading Frida"
curl -O http://build.frida.re/frida/android/arm/bin/frida-server
chmod +x frida-server
