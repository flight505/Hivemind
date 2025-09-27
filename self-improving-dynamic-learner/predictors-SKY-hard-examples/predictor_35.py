"""
Predictor 35
Generated on: 2025-09-09 17:32:28
Accuracy: 43.49%
"""


# PREDICTOR 35 - Accuracy: 43.49%
# Correct predictions: 4349/10000 (43.49%)

def predict_output(A, B, C, D, E):
    if B > 70 and C > 90 and E > 80:
        return 1
    if B > 60 and C > 70:
        return 2
    if B > 60 and C > 60 and E < 10:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 60 and C < 30:
        return 1
    if B > 90 and C > 60 and E < 20 and D > 90:
        return 3
    if E > 70 and D > 90:
        return 3
    if E > 90 and C > 40:
        return 3
    if B > 60 and C > 65 and E < 20 and A < 40:
        return 4
    if C > 70 and B < 40 and E > 60:
        return 4
    if C < 30 and E > 50:
        if B < 45:
            return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            return 4
    elif C < 30:
        if B < 20:
            if C < 15:
                return 3
            else:
                return 1
        if B > 60:
            return 1
        elif D > 80 and E < 20:
            return 1
        else:
            return 3
    if A < 20 and B > 55 and E < 15:
        return 4
    if A < 10 and B < 40 and C > 40 and E < 40:
        return 3
    if B > 60 and E > 50 and A > 60 and C > 40:
        if C > 60:
            return 1
        else:
            return 2
    if A < 35 and B > 40 and C > 40 and E > 50 and D < 30:
        return 2
    if 50 < B < 65 and C > 35 and E < 30 and D > 70:
        return 3
    if B < 40 and C > 50 and E < 25:
        return 3
    if D > 50 and B < 40 and C > 45:
        return 1
    if D > 50 and B < 40 and C < 45:
        return 3
    return 1