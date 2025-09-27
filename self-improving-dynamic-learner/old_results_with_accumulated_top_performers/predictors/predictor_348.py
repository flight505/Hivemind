"""
Predictor 348
Generated on: 2025-09-09 09:09:58
Accuracy: 51.59%
"""


# PREDICTOR 348 - Accuracy: 51.59%
# Correct predictions: 5159/10000 (51.59%)

def predict_output(A, B, C, D, E):
    # Find the position of the smallest value
    min_val = min(A, B, C, D, E)
    if min_val == C:
        max_val = max(A, B, C, D, E)
        if max_val == E:
            return 4
        else:
            return 3
    elif min_val == D:
        max_val = max(A, B, C, D, E)
        if max_val == C:
            return 2
        else:
            return 1
    elif min_val == A:
        if C > 70:
            return 2
        else:
            return 1
    else:
        return 1