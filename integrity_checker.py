"""
File Integrity Checker - ECE4113 Secure Software Development
Service: Data Integrity (SHA-256 hash verification)
Uses only Python's built-in hashlib module.
"""
import hashlib


def compute_sha256(path):
    """Read the file in small pieces and return its SHA-256 hash as hex text."""
    sha = hashlib.sha256()
    with open(path, "rb") as f:          # "rb" = read raw bytes
        while True:
            chunk = f.read(4096)         # read 4096 bytes at a time
            if not chunk:                # empty chunk = end of file
                break
            sha.update(chunk)            # feed the piece into the hash
    return sha.hexdigest()               # 64 hex characters


def save_hash(path):
    """Compute the file's hash and save it as the trusted hash."""
    hash_value = compute_sha256(path)
    hash_file = path + ".sha256"
    with open(hash_file, "w") as f:
        f.write(hash_value)
    print(f"SHA-256 : {hash_value}")
    print(f"Trusted hash saved to: {hash_file}")


def verify_file(path):
    """Recompute the file's hash and compare it with the saved trusted hash."""
    with open(path + ".sha256", "r") as f:
        trusted_hash = f.read().strip()
    current_hash = compute_sha256(path)
    print(f"Trusted hash : {trusted_hash}")
    print(f"Current hash : {current_hash}")
    if current_hash == trusted_hash:
        print("RESULT: PASS - file is unchanged.")
    else:
        print("RESULT: FAIL - file has been modified!")


def main():
    while True:
        print("\n1) Calculate and save hash")
        print("2) Verify file")
        print("3) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "3":
            break
        if choice not in ("1", "2"):
            print("Invalid choice. Enter 1, 2 or 3.")
            continue
        path = input("Enter file path: ").strip()
        try:
            if choice == "1":
                save_hash(path)
            else:
                verify_file(path)
        except FileNotFoundError:
            print("Error: file (or its .sha256 hash file) not found. "
                  "Did you run option 1 first?")
        except OSError as e:
            print(f"Error: cannot read file ({e.strerror}).")


if __name__ == "__main__":
    main()
