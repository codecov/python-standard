#!/bin/sh

export CI="True"
export APPVEYOR="True"
bash <(curl -s https://codecov.io/bash) 
