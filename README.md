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
4. Run the script:
    ```bash
    python passcrack.py
    ```


## Explanation

The code is based on statistical analysis and multiple trials to determine the correct password. It uses a timing attack method where it measures the time taken to verify each character of the password. By running multiple trials, the script identifies the character with the longest average response time, which is likely part of the correct password.

### Adjusting Trials for Accuracy

To ensure more accurate results, you can increase the number of trials and retries. The variables `trials` and `max_retries` in the script control these parameters:

- `trials`: Number of times each password attempt is tested to calculate the average response time. Increasing this value will make the results more reliable but will also take more time.
- `max_retries`: Maximum number of retries for each position if the confidence level is below the threshold. This helps to ensure that the selected character is correct.

#### Example:

To increase the number of trials to 200 and the maximum retries to 20, modify the following lines in `script.py`:

```python
trials = 200  # Number of trials for more accuracy
max_retries = 20  # Maximum number of retries for each position
