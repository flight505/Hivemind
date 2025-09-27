"""
Predictor 9
Generated on: 2025-09-09 17:10:02
Accuracy: 46.66%
"""


# PREDICTOR 9 - Accuracy: 46.66%
# Correct predictions: 4666/10000 (46.66%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C >= 75:
        if E < 30:
            return 4
        if B > 60:
            if A > 70 and D > 80:
                return 1
            return 2
        else:
            return 1
    if B < 20:
        if C < 25:
            if E > 70:
                return 1
            return 3
        elif D < 20:
            return 3
        elif A > 70:
            if C > 60:
                return 1
            return 4
        elif C > 70:
            return 4
        else:
            return 1
    if C < 40:
        if C < 5 and E > 40:
            return 3
        if B > 70 and D > 70 and E > 70:
            return 2
        elif B > 70 and E > 50:
            return 4
        elif A > 70 and B > 70:
            return 4
        elif E > 70:
            return 1
        elif D > 50 or B > 40:
            return 1
        else:
            return 3
    else:
        if B > 50 and D > 65:
            if E < 10:
                return 4
            return 3
        elif B > 70:
            if D < 30:
                return 1
            return 2
        elif D < 30 and E < 50:
            return 4
        else:
            return 1