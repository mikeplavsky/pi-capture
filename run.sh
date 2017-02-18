#!/bin/bash

BUCKET=$1
BASEDIR=$(dirname "$0")

$BASEDIR/make.sh $BUCKET >> $BASEDIR/make.log  2>&1 
