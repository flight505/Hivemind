"""
Predictor 68
Generated on: 2025-09-09 03:25:43
Accuracy: 40.02%
"""


# PREDICTOR 68 - Accuracy: 40.02%
# Correct predictions: 4002/10000 (40.02%)

def predict_output(A, B, C, D, E):
    sum_ABC = A + B + C
    high_C = C > 60
    low_C = C < 25
    high_B = B > 70
    low_B = B < 25
    A_ge60 = A >= 60
    D_gt60 = D > 60
    
    if high_C:
        if A_ge60 and B > 20 and D_gt60 or sum_ABC > 210:
            return 1
        else:
            return 2
    elif low_C:
        if low_B:
            return 3
        elif high_B:
            return 1
        else:
            return 4
    else:
        if high_B:
            return 2
        else:
            return 1