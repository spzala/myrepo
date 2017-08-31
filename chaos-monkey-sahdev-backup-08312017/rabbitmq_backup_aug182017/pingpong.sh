#!/bin/sh
endtime=$((SECONDS+10))

while [ $SECONDS -lt $endtime ]; do
    python player1.py
    #sleep for one seconds
    sleep 1
    :
done

