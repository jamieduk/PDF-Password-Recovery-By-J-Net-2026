#!/bin/bash
# (c) J~Net 2026
#
# ./start.sh "secret.pdf"
#

pass_list="password-list.txt"

text="PDF File Password Recovery BruteForce By (c) J~Net 2026"
color="\e[92m"

echo -e "$color$text"

if [ ! -f "venv/bin/activate" ]; then
    bash ./setup.sh
fi

source "venv/bin/activate"

if [ -z "$1" ]; then
    echo "Enter PDF file (example: secret.pdf)"
    read in_file
else
    in_file="$1"
fi


if [ ! -f "$pass_list" ]; then
    echo "Password list not found."
    echo "Enter password list filename:"
    read pass_list
fi

if [ ! -f "$in_file" ]; then
    echo "PDF file not found: $in_file"
    exit 1
fi

if [ ! -f "$pass_list" ]; then
    echo "Password list not found: $pass_list"
    exit 1
fi


echo "Virtual Environment ready!"
echo

python3 pdf-password-recovery.py "$in_file" "$pass_list"
