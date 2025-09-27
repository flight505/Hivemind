"""
Predictor 23
Generated on: 2025-09-09 12:53:31
Accuracy: 54.83%
"""


# PREDICTOR 23 - Accuracy: 54.83%
# Correct predictions: 5483/10000 (54.83%)

def predict_output(A, B, C, D, E):
    ed = E - D

    # Very low C strongly indicates class 3
    if C <= 12:
        return 3

    # Class 2: high C with either very low D or very strong B
    if C >= 75 and (D <= 10 or B >= 80):
        return 2

    # Class 4: E dominates D in low C region
    if C <= 30 and ed >= 50:
        return 4

    # Default to class 1
    return 1