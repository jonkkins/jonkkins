#!/bin/bash

# Install flask
# Dev note: -U is an issue. We have to revise it to install a specific
#            version of flask. We want to install a specific flask version
#            than to choose a latest build, to ensure that our docker image
#            will be created in an always same state.
pip install -U Flask

# Remove itself from the image
rm $0