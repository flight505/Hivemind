"""
Predictor 131
Generated on: 2025-09-09 05:49:23
Accuracy: 45.01%
"""


# PREDICTOR 131 - Accuracy: 45.01%
# Correct predictions: 4501/10000 (45.01%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 15:
        if B < 20 and E < 50:
            return 3
        elif E > 60 and B < 40 and A < 10:
            return 2
        else:
            return 3
    if C > 70:
        if E < 30:
            return 4
        if B < 30 and D < 30:
            return 4
        if A >= 50:
            return 1
        else:
            return 2
    if C < 40:
        if A < 20 and E > 50 and D < 30:
            return 2
        if B > 60 and E > 70:
            return 2
        if D > 70:
            if A > 80:
                return 3
            else:
                return 1
        else:
            return 3
    else:
        if B > 60:
            if D > 80 and E > 70:
                return 3
            else:
                return 1
        elif C > 50 and E < 30 and A < 30:
            return 4
        else:
            return 1