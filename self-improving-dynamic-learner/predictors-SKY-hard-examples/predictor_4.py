"""
Predictor 4
Generated on: 2025-09-09 17:05:27
Accuracy: 44.29%
"""


# PREDICTOR 4 - Accuracy: 44.29%
# Correct predictions: 4429/10000 (44.29%)

def predict_output(A, B, C, D, E):
    if C >= 75:
        if A > 50:
            return 1
        else:
            return 2
    if B < 20:
        if C > 50:
            return 4
        elif D > 80 and E > 60:
            return 1
        elif A > 50 and C > 40:
            return 1
        elif C > 30 and E > 45:
            return 2
        else:
            return 3
    if C < 40:
        if E > 90:
            if A > 30:
                return 4
            else:
                return 1
        elif B > 70 and E > 50:
            return 4
        elif A > 70 and B < 50:
            return 4
        elif A + E < 70:
            return 4
        elif D > 70:
            return 1
        elif A > 50:
            return 1
        else:
            return 2
    else:
        if E > 90:
            return 4
        if B < 30 and D < 30 and C < 50:
            return 4
        if B > 50 and D > 70:
            return 3
        if D < 20:
            return 1
        if B >= 50 and D < 60 and C < 50:
            return 2
        if A > 80 and B < 60 and D < 60:
            return 2
        return 1