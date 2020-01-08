#!/bin/bash
for i in {1000..1015}
do
   echo "Downloading photos corresponding to the page $i..."
   python rover_photo_downloader.py --sol $i --debug --key s7EvFHQ2UnvilHhF5TtpBcTY4ewXlUa6s6QhNfED
done