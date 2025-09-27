"""
Predictor 252
Generated on: 2025-09-09 06:26:21
Accuracy: 34.83%
"""


# PREDICTOR 252 - Accuracy: 34.83%
# Correct predictions: 3483/10000 (34.83%)

def predict_output(A, B, C, D, E):
    low_B = B < 25
    low_C = C < 25
    high_C = C > 60
    high_E = E > 80
    high_B = B > 70
    low_D = D < 20
    
    if low_B and low_C:
        return 3
    elif high_C:
        if high_B and low_D:
            return 1
        else:
            return 2
    elif high_E:
        return 4
    else:
        return 1