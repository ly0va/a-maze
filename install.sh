#!/bin/sh

curl -qL http://py.processing.org/processing.py-linux64.tgz | tar xzf - --wildcards '*/processing-py.jar'
mv processing.py*/processing-py.jar .
rmdir processing.py*
