"""
Predictor 97
Generated on: 2025-09-09 03:49:02
Accuracy: 38.84%
"""


# PREDICTOR 97 - Accuracy: 38.84%
# Correct predictions: 3884/10000 (38.84%)

def predict_output(A, B, C, D, E):
    high_C = C > 60
    low_B = B < 25
    low_C = C < 25
    
    if high_C:
        if B > 70:
            return 1
        else:
            return 2
    else:
        if E > 70:
            return 4
        elif low_B and low_C:
            return 3
        else:
            return 1