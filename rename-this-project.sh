#!/bin/bash

##
# Renames all strings and filenames 'foo-bar' to a user-provided string.
##


set -e
oldname_="conan-hello-world"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <new-project-name>"
    exit 1
fi
newname_="$1"

mv "$oldname_.cpp" "$newname_.cpp"
find -type f ! -path "./.*" | xargs sed -i -r -e s,"$oldname_","$newname_",g
