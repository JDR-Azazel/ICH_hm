#!/bin/bash

finder=$(find /opt/210225-ptm -name "*.sh")

        for FILE in $finder; do
        chmod +x $FILE
        echo "changed permision $FILE"
        done

echo "done"
