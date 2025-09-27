"""
Predictor 562
Generated on: 2025-09-09 18:04:32
Accuracy: 44.99%
"""


# PREDICTOR 562 - Accuracy: 44.99%
# Correct predictions: 4499/10000 (44.99%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B > 80:
            return 1
        if B < 20:
            if E > 50:
                return 4
            else:
                if A > 80 and D < 20:
                    return 1
                else:
                    return 3
        if D > 80:
            return 1
        if E < 45:
            return 3
        if E > 90:
            return 4
        return 1
    if B > 60 and C > 70:
        if E > 60:
            return 2
        else:
            return 4
    if B > 60 and C < 50 and E > 80:
        if D > 60:
            return 2
        else:
            return 4
    if B < 30 and C > 60 and E > 50:
        return 2
    if B < 30 and 40 < C < 60 and E > 50:
        if A < 50:
            return 2
        else:
            return 4
    if B < 30 and C > 40 and E < 20 and D < 30:
        return 4
    if E > 90:
        return 4
    if D > 50:
        return 1
    return 1