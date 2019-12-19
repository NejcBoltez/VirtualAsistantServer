pip install wikipedia
pip install pyttsx3
pip install speechrecognition
pip install tkinter

INSTALL ESPEAK ON LINUX
sudo apt-get install espeak --fix-broken lib32gcc1 libc6-i386 lib32z1 libespeak1 espeak-data 

INSTALL PYAUDIO
sudo apt-get install libasound-dev
Download the portaudio archive from: http://portaudio.com/download.html
Unzip the archive: tar -zxvf [portaudio.tgz]
Enter the directory, then run: ./configure && make
Install: sudo make install
And finally: sudo pip install pyaudio
Check the version of pyaudio, it should be 0.2.9

