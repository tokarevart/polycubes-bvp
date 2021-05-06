#!/bin/bash
if [ $# -eq 5 ]; then
    ndir=$1
    rbeg=$2
    rend=$3
    nthr=$4
    gpui=$5
    screen -dmS $ndir'-'$rbeg'-'$rend'-gpu'$gpui python realizes.py $ndir $rbeg $rend $nthr $gpui
else
    nbeg=$1
    nend=$2
    rbeg=$3
    rend=$4
    nthr=$5
    gpui=$6
    screen -dmS 'n'$nbeg'to'$nend'-'$rbeg'-'$rend'-gpu'$gpui python realizes.py $nbeg $nend $rbeg $rend $nthr $gpui
fi