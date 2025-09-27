"""
Predictor 222
Generated on: 2025-09-09 09:00:09
Accuracy: 48.04%
"""


# PREDICTOR 222 - Accuracy: 48.04%
# Correct predictions: 4804/10000 (48.04%)

def predict_output(A, B, C, D, E):
    if C < 15:
        if B > 70:
            if A < 10:
                return 2
            else:
                return 4
        elif D > 80:
            if A > 50:
                return 3
            else:
                return 1
        elif E > 55:
            return 4
        else:
            return 3
    elif C < 30:
        if E > 90:
            return 4
        elif D > 80:
            return 1
        else:
            return 3
    elif C < 60:
        if D > 90:
            return 3
        elif B > 70 and E < 30:
            return 4
        else:
            return 1
    else:
        if B < 20:
            return 4
        elif D > 90:
            return 1
        elif A > 50:
            return 1
        else:
            return 2