#!/usr/bin/python
import pyaudio
import array
import time
import sys

CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 48000,
                input = True,
                frames_per_buffer = CHUNK,
                input_device_index = 0)

last = time.time()

print 'pause'
sys.stdout.flush()

while True:
    try:
        data = stream.read(CHUNK)
    except:
        stream.stop_stream()
        stream.start_stream()
        continue
    data = array.array("h", data)
    if last < time.time() - 1:
        if max(data) < -32000:
            last = time.time()
            print 'pause'
            sys.stdout.flush()
        if min(data) > 32000:
            last = time.time()
            print 'pause'
            sys.stdout.flush()

stream.stop_stream()
stream.close()
p.terminate()
