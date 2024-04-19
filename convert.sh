#!/bin/bash

echo "Directory: $(pwd)"

for dir in */; do
    cd "$dir" || exit
    for dirr in */; do
        cd "$dirr" || exit
        echo "Directory: $(pwd)"
        lowriter --convert-to docx *.doc
        rm -rf *zip *.doc
        cd ..
    done
    cd ..
done
