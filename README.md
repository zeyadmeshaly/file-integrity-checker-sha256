# File Integrity Checker (SHA-256)
ECE4113 - Secure Software Development - Data Integrity service

## Requirements
Python 3.6+ (no extra packages; uses built-in `hashlib`).

## Run
    python integrity_checker.py

## Usage
1. Option 1: enter a file path -> prints SHA-256 and saves it to `<file>.sha256` (trusted hash).
2. Option 2: enter the same path -> recomputes the hash and prints PASS or FAIL.
3. Option 3: exit.

## Demo
    echo "Hello, this is my original message." > sample.txt
    python integrity_checker.py     # option 1, then option 2 -> PASS
    echo "Hello, this is my TAMPERED message." > sample.txt
    python integrity_checker.py     # option 2 -> FAIL

## Limitation
The trusted hash must be stored somewhere an attacker cannot change. See report.
