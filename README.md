# Password Cracker

This project contains a script to perform a timing attack trying to bruteforce password.

## Prerequisites

- Python 3.7

## Usage

1. Ensure you have Python 3.7 installed.
2. Navigate to the directory containing the script and `vault.elf`.
3. Make sure `vault.elf` is executable:
    ```bash
    chmod +x vault.elf
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the script:
    ```bash
    python passcracker.py
    ```

The script will attempt to determine the correct password using timing attacks and print the best password combination it finds.
