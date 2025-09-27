"""
Predictor 3
Generated on: 2025-09-09 17:03:56
Accuracy: 43.41%
"""


# PREDICTOR 3 - Accuracy: 43.41%
# Correct predictions: 4341/10000 (43.41%)

def predict_output(A, B, C, D, E):
    if C >= 75:
        if D < 10:
            if B > 50:
                return 2
            else:
                return 3
        else:
            if B > 70:
                return 2
            else:
                return 1
    if B < 20:
        if A > 90 and D > 90:
            return 4
        elif D > 80 and E > 60:
            return 1
        elif A > 50 and C > 40:
            return 1
        elif C > 30 and E > 45:
            return 2
        else:
            return 3
    else:
        if C < 40 and (A > 80 or E > 90):
            return 4
        if C < 40:
            if D > 70:
                return 1
            else:
                return 2
        else:
            if B > 50 and D > 70:
                return 3
            if A > 80 and B < 60 and D < 60:
                return 2
            else:
                return 1