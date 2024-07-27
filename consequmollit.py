def count_crossings(segments, lambda_value):
    crossings = 0
    for segment in segments:
        if (segment[0] - lambda_value) * (segment[1] - lambda_value) < 0:
            crossings += 1
    return crossings

# Example usage
segments = [(1, 3), (-2, 4), (0, 2)]
lambda_value = 0
print(count_crossings(segments, lambda_value))  # Output: 2
