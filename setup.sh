#!/bin/bash

python3.11 -m venv . || pip install virtualenv

source venv/bin/activate
pip install -q -r requirements.txt

setopt aliases || shopt -s expand_aliases

alias activate="venv/bin/activate"
alias play_hangman="python3 game/play.py"

play_hangman
