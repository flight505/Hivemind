"""
Predictor 274
Generated on: 2025-09-09 06:59:37
Accuracy: 48.43%
"""


# PREDICTOR 274 - Accuracy: 48.43%
# Correct predictions: 4843/10000 (48.43%)

def predict_output(A, B, C, D, E):
    low_B = B < 25
    low_C = C < 25
    high_D = D > 70
    high_C = C > 60
    if low_B and low_C:
        return 3
    elif E > 90:
        return 4
    elif high_C:
        if A > 50:
            return 1
        else:
            return 2
    elif high_D:
        return 1
    else:
        return 1