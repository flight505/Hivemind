"""
Predictor 371
Generated on: 2025-09-09 10:12:30
Accuracy: 55.72%
"""


# PREDICTOR 371 - Accuracy: 55.72%
# Correct predictions: 5572/10000 (55.72%)

def predict_output(A, B, C, D, E):
    low_B = B < 25
    low_C = C < 25
    high_B = B > 60
    high_C = C > 60
    high_A = A > 70
    high_E = E > 80
    
    if low_B and low_C:
        return 3
    elif high_E and low_C:
        return 4
    elif high_B and high_C:
        if high_A:
            return 1
        else:
            return 2
    else:
        return 1