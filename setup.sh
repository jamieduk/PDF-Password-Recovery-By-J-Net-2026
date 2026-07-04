#!/bin/bash
# (c) J~Net 2026
#
# ./setup.sh
#
#
#
text="PDF File Password Recovery BruteForce By (c) J~Net 2026"
color="\e[92m"

echo -e "$color$text"

if [ ! -f "venv/bin/activate" ]; then
    echo "Creating virtual environment..."
    #/usr/bin/rm -rf venv
    python -m venv venv
fi

source venv/bin/activate

echo "Virtual Environment Setup and ready!"

pip install pikepdf

chmod +x pdf-password-recovery.py

echo "You will need a password-list.txt and the target pdf-file.pdf to crack"
echo "./start.sh file.pdf"
