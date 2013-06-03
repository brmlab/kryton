#!/bin/bash
./detector.py | mplayer -fs -vo directfb -slave $1 -loop 0
