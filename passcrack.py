import subprocess
import time
import string
import statistics
from collections import Counter

def test_password(password, trials=100):
    times = []
    for _ in range(trials):
        start_time = time.perf_counter()
        process = subprocess.run(["./vault.elf", password], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    median_time = statistics.median(times)
    return median_time, times

def find_best_letter(current_password, trials=100):
    results = {}
    characters = string.ascii_lowercase  # Only lowercase letters
    trial_results = {char: [] for char in characters}

    for char in characters:
        password = current_password + char
        median_time, times = test_password(password, trials)
        results[char] = median_time
        trial_results[char] = times

    best_char = max(results, key=results.get)

    # Calculate confidence level
    confidence_counts = {char: 0 for char in characters}
    for i in range(trials):
        max_time = max(trial_results[char][i] for char in characters)
        for char in characters:
            if trial_results[char][i] == max_time:
                confidence_counts[char] += 1

    confidence_level = (confidence_counts[best_char] / trials) * 100
    return best_char, results[best_char], confidence_level, results

if __name__ == "__main__":
    current_password = ""
    trials = 100  # Number of trials for more accuracy
    max_retries = 10  # Maximum number of retries for each position

    for i in range(15):  # Extended to 15 characters
        retry_count = 0
        candidate_counter = Counter()

        while retry_count < max_retries:
            best_char, best_time, confidence_level, all_results = find_best_letter(current_password, trials)
            candidate_counter[best_char] += 1

            if confidence_level >= 80:
                break

            retry_count += 1
            print(f"Low confidence level for position {i+1}: {confidence_level:.2f}%, Retesting...")
            print(f"Current best candidate for position {i+1}: {best_char}, Score: {all_results[best_char]:.6f}")

        # Determine the best character based on the most frequent candidate
        final_best_char = candidate_counter.most_common(1)[0][0]
        current_password += final_best_char
        print(f"Best letter for position {i+1}: {final_best_char}, Confidence level: {confidence_level:.2f}%")
        print(f"Current best password: {current_password}")

    # Print the final best password combination
    print(f"\nBest password combination: {current_password}")
