#!/bin/sh
endtime=$((SECONDS+5))
python throwball.py
sleep 2
python player1.py
sleep 1
pkill -f player1.py
exit 0
while [ $SECONDS -lt $endtime ]; do
    python player1.py
    #sleep for one seconds
    sleep 2
    exit 0
    :
done
python endgame.py

