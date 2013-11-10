#!/bin/bash

DIR=""

cd $DIR
source env/bin/activate
python $DIR/getData.py
deactivate
