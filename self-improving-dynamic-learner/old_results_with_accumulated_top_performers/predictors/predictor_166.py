"""
Predictor 166
Generated on: 2025-09-09 04:46:47
Accuracy: 41.93%
"""


# PREDICTOR 166 - Accuracy: 41.93%
# Correct predictions: 4193/10000 (41.93%)

def predict_output(A, B, C, D, E):
    high_C = C > 60
    low_C = C < 25
    low_B = B < 25
    high_D = D > 70
    high_E = E > 80
    if high_E:
        return 4
    elif high_C and not high_E:
        if low_B:
            if A > 70:
                return 4
            else:
                return 3
        elif A < 50:
            return 2
        else:
            return 1
    elif low_C:
        if E > 80:
            return 4
        elif B > 70 and D < 70:
            return 4
        elif B > 60 and D < 50:
            return 3
        elif B < 20:
            return 3
        else:
            return 1
    else:
        if B > 80:
            return 2
        else:
            return 1