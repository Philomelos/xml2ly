#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Running $DIR/xml2ly.py in $DIR..."

source "$DIR/env/bin/activate"
python "$DIR/xml2ly.py" "$@"
