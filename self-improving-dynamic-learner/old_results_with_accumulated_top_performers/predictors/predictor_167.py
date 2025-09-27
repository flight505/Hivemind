"""
Predictor 167
Generated on: 2025-09-09 04:49:46
Accuracy: 47.35%
"""


# PREDICTOR 167 - Accuracy: 47.35%
# Correct predictions: 4735/10000 (47.35%)

def predict_output(A, B, C, D, E):
    high_C = C > 60
    low_C = C < 25
    high_E = E > 80
    low_B = B < 25
    high_D = D > 70
    high_A = A > 70
    low_D = D < 20
    if high_E:
        if low_C:
            if low_B:
                return 1
            else:
                return 4
        elif high_C:
            if low_D:
                return 2
            else:
                return 1
        else:
            return 4
    elif high_C and not high_E:
        if high_A:
            return 1
        else:
            return 2
    elif low_C:
        if low_B:
            if high_A and low_D:
                return 4
            else:
                return 3
        elif high_D and C < 10:
            return 3
        else:
            return 1
    else:
        return 1