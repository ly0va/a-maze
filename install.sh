#!/bin/sh

case "$(uname -s)" in
    Linux*)     platform="linux64" ;;
    Darwin*)    platform="macosx"  ;;
    *)          echo "Unsupported platform"; exit 1 ;;
esac

curl -qL "http://py.processing.org/processing.py-$platform.tgz" | tar xzf - --wildcards '*/processing-py.jar'
mv processing.py*/processing-py.jar .
rmdir processing.py*
