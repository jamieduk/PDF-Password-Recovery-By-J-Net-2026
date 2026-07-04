# PDF Password Recovery By J~Net 2026

https://github.com/jamieduk/PDF-Password-Recovery-By-J-Net-2026  
jnetai.com  

---

## Overview

High-speed PDF password recovery tool using `pikepdf` and a wordlist-based brute force approach.

Designed for quick recovery of lost or forgotten PDF passwords using a local password list.

---

## Features

- Fast wordlist brute-force
- Uses `pikepdf` for PDF decryption attempts
- Virtual environment setup included
- Simple CLI interface
- Clear success output with decrypted file export

---

## Requirements

- Python 3
- pip
- pikepdf

---

## Setup

```bash
./setup.sh

This will:

Create virtual environment
Install dependencies
Prepare runtime environment
Usage
./start.sh "secret.pdf"
Example Output
PDF File Password Recovery BruteForce By (c) J~Net 2026
Virtual Environment ready!

==================================================
 PDF Password Recovery (pikepdf)
 Encrypted file : secret.pdf
 Password list  : password-list.txt
 Total passwords: 8
 Output file    : recovered-decrypted.pdf
==================================================

[7/8] Trying: test...ainASSh0le!...

==================================================
 SUCCESS! Password found.
==================================================
 Password : test
 Attempt  : 7 / 8
 Output   : recovered-decrypted.pdf
==================================================
Files
start.sh → main launcher
setup.sh → environment setup
password-list.txt → wordlist file
recovered-decrypted.pdf → output file (generated)
Notes
Keep wordlists updated for better success rate
Large wordlists will increase recovery time
Output file will only be created on successful match
License

(c) J~Net 2026 - All rights reserved
