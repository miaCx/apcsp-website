#!/bin/bash


echo -e "Content-type: text/html\n\n"

echo "<h1>Raspberry Pi Status</h1>"

echo "<h2>Host Info</h2>"
echo "<pre>$(./rpistatus)</pre>"

