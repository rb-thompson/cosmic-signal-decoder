import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

signal = "3K7P9Q2R8T4M1N6J5H2G8F4D9C1B7A2Z4Y6X8W3V5U9T2S1R7Q4P3N6M8L2K9J4H5G1F7D3C8B2A6Z9Y4X5W3V8U2T1R7Q6P4N3M9L2K8J5H4G1F7D"

# Step 1: Extract letters
letters = re.findall(r'[A-Z]', signal)
message = ''.join(letters[2::3])
print(f"Hidden message: {message}")

# Step 2: Extract numbers and analyze
numbers = [int(n) for n in re.findall(r'\d', signal)]
print(f"Numbers: {numbers}")

stats = {
    'mean': np.mean(numbers),
    'median': np.median(numbers),
    'std_dev': np.std(numbers),
    'min': np.min(numbers),
    'max': np.max(numbers)
}
print(f"Statistics: {stats}")

# Letter frequency
letter_counts = pd.Series(list(''.join(letters))).value_counts()

# Step 3: Plot 
letter_counts.plot(kind='bar', title='Cosmic Signal: Letter Frequencies')
plt.xlabel('Letter')
plt.ylabel('Count')
plt.savefig('cosmic_signal.png')
plt.show()