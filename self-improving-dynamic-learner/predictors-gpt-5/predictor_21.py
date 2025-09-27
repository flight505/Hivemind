"""
Predictor 21
Generated on: 2025-09-09 12:51:24
Accuracy: 55.97%
"""


# PREDICTOR 21 - Accuracy: 55.97%
# Correct predictions: 5597/10000 (55.97%)

def predict_output(A, B, C, D, E):
    # Class 3: very low C
    if C <= 12:
        return 3

    # Class 2: high C with either very low D or very strong B
    if C >= 78 and (D <= 10 or B >= 90):
        return 2

    # Class 4: low C with high E and low D
    if C <= 25:
        if E >= 85 and D <= 35:
            return 4
        # otherwise low C in this sample defaults to 1
        return 1

    # Additional class 4: very high E with low D and not-too-high C
    if E >= 95 and D <= 30 and C <= 85:
        return 4

    # Default class 1
    return 1