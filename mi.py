import random

def generate_balance_frequency():
    frequency_options = [1.0, 1.5, 2.0, 2.5]  # Example predefined options
    return random.choice(frequency_options)

# Example usage:
balance_frequency = generate_balance_frequency()
print(balance_frequency)  # Output: one of the predefined frequencies
