#!/usr/bin/env python3
# (c) J~Net 2026
# pdf-password-recovery.py — Brute-force PDF password recovery using pikepdf
#
# Usage: python3 pdf-password-recovery.py <encrypted.pdf> <password-list.txt> [output.pdf]
# Example: python3 pdf-password-recovery.py secret.pdf passwords.txt decrypted.pdf
#
# Requires: pip install pikepdf

import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 pdf-password-recovery.py <encrypted.pdf> <password-list.txt> [output.pdf]")
        sys.exit(1)

    enc_file=sys.argv[1]
    pass_file=sys.argv[2]
    out_file=sys.argv[3] if len(sys.argv) > 3 else "recovered-decrypted.pdf"

    # --- Checks ---
    if not os.path.isfile(enc_file):
        print(f"Error: Encrypted PDF '{enc_file}' not found.")
        sys.exit(1)

    if not os.path.isfile(pass_file):
        print(f"Error: Password list '{pass_file}' not found.")
        sys.exit(1)

    # Lazy import so error is clear if pikepdf missing
    try:
        import pikepdf
    except ImportError:
        print("Error: pikepdf not installed. Run: pip install pikepdf")
        sys.exit(1)

    # Read passwords
    with open(pass_file, "r", encoding="utf-8", errors="ignore") as f:
        passwords=[line.rstrip("\n\r") for line in f if line.strip()]

    total=len(passwords)
    found=False

    print("=" * 50)
    print(" PDF Password Recovery (pikepdf)")
    print(f" Encrypted file : {enc_file}")
    print(f" Password list  : {pass_file}")
    print(f" Total passwords: {total}")
    print(f" Output file    : {out_file}")
    print("=" * 50)
    print()

    for idx, password in enumerate(passwords, 1):
        print(f"\r[{idx}/{total}] Trying: {password}...", end="", flush=True)

        try:
            pdf=pikepdf.open(enc_file, password=password)
            pdf.save(out_file)
            pdf.close()
            found=True
            print()
            print()
            print("=" * 50)
            print(" SUCCESS! Password found.")
            print("=" * 50)
            print(f" Password : {password}")
            print(f" Attempt  : {idx} / {total}")
            print(f" Output   : {out_file}")
            print("=" * 50)
            break
        except pikepdf.PasswordError:
            continue
        except Exception as e:
            # Some other error — still wrong password likely
            continue

    if not found:
        print()
        print()
        print("=" * 50)
        print(" FAILED — No password in the list worked.")
        print(f" Tried {total} passwords.")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    main()
