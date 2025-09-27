"""
Predictor 7
Generated on: 2025-09-09 17:09:34
Accuracy: 39.45%
"""


# PREDICTOR 7 - Accuracy: 39.45%
# Correct predictions: 3945/10000 (39.45%)

def predict_output(A, B, C, D, E):
    if B < 20:
        if C < 20:
            if E < 40:
                return 3
            else:
                return 1
        else:
            if E > 90 and D < 50 and C < 30:
                return 4
            elif C > 70:
                return 4
            elif D < 15:
                return 3
            elif A < 10:
                return 2
            else:
                return 1
    if C >= 75:
        return 2
    if E > 90:
        if D < 50 and C < 30:
            return 4
        else:
            return 1
    if C < 40:
        if A > 80 and B > 80 and D < 25:
            return 4
        elif B > 60 and D < 20:
            return 3
        elif D > 50 or B > 40:
            return 1
        else:
            return 4
    else:
        if B > 70 and D > 80 and C > 60:
            return 3
        elif B > 70 and D > 30:
            return 2
        else:
            return 1