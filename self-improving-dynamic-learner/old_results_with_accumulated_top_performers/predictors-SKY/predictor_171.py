"""
Predictor 171
Generated on: 2025-09-09 07:10:46
Accuracy: 51.36%
"""


# PREDICTOR 171 - Accuracy: 51.36%
# Correct predictions: 5136/10000 (51.36%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 50:
        return 4
    if A < 40 and B > 60 and C > 70:
        return 2
    if C < 15:
        if B < 20:
            if E > 60:
                return 2
            else:
                return 3
        elif B > 50:
            if E < 50:
                return 3
            else:
                return 1
        else:
            return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            if A >= 50:
                return 4
            else:
                return 1
    if C < 40:
        if A < 50 and B > 60 and E > 70:
            return 2
        if B > 50 and C < 35 and E > 70:
            return 4
        if C > 30 and E < 20 and D > 70 and B < 60:
            return 3
        return 1
    else:
        if A < 30 and E < 30:
            return 4
        if B > 60 and D >= 90:
            return 3
        return 1