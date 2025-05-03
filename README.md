# Challenge: "Cosmic Signal Decoder"

**Concept**: You’re an interstellar hacker decoding a mysterious signal from a distant galaxy. The signal is a string of numbers and letters, and your job is to write a Python script to extract a hidden message, analyze its patterns, and visualize the results—all in under an hour.

**Why it's optimized for devs**: 

- Coding & Creativity
- Data Analysis
- Portfolio Boost
- Time-Boxed

**The Signal**:
Here's the raw signal you've intercepted:

```
signal = "3K7P9Q2R8T4M1N6J5H2G8F4D9C1B7A2Z4Y6X8W3V5U9T2S1R7Q4P3N6M8L2K9J4H5G1F7D3C8B2A6Z9Y4X5W3V8U2T1R7Q6P4N3M9L2K8J5H4G1F7D"
```

It's a mix of numbers (0-9) and letters (A-Z). The hidden message is encoded in the letters but you need to filter and decode it based on a rule.

**The Mission**:

1. **Extract the Message** (15 min):
    - Write a function to filter out numbers and keep only letters (A-Z).
    - The letters form a sequence, but every *third* letter is part of the actual message. Concatenate those to reveal the hidden text.
    - Hint: Use string methods or regex to clean the signal, then slice or loop to grab every third letter.

2. **Analyze the Signal** (15 min):
    - Convert the numbers in the signal to a list of integers.
    - Calculate basic stats: mean, median, and standard deviation (use NumPy or Pandas).
    - Count how many times each letter appears in the full signal (use a dictionary or Pandas).

3. **Visualize It** (10 min):
    - Create a quick plot with Matplotlib: a bar chart of letter frequencies.
    - Save the plot as `cosmic_signal.png` for your portfolio.

4. **Stretch Goal** (if time allows):
    - Check if the numeric sequence has any patterns (e.g., is it random, or does it follow a simple rule like alternating odd/even?). Print a one-sentence hypothesis.