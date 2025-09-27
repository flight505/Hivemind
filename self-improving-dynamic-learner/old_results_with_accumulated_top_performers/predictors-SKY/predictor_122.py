"""
Predictor 122
Generated on: 2025-09-09 05:39:01
Accuracy: 48.92%
"""


# PREDICTOR 122 - Accuracy: 48.92%
# Correct predictions: 4892/10000 (48.92%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B > 50 and E > 50:
            return 4
        if B < 20:
            return 3
        if B > 50:
            return 1
        return 3
    if C > 70:
        if B > 60:
            if E < 20 or (D > 70 and E > 80):
                return 1
            return 2
        if D < 20:
            if E > 50:
                return 1
            return 3
        return 1
    if C < 40:
        if E > 80:
            return 4
        if E > 60 and D < 20:
            return 2
        if D < 20 and E < 20:
            return 3
        if B > 70 and E > 60:
            return 2
        if B > 50 and E < 40:
            return 3
        return 1
    if C > 60 and B < 30:
        return 4
    if B < 20 and D < 10:
        return 3
    if E > 80:
        return 4
    if D > 70 and E < 20:
        return 3
    if B > 50 and E > 60:
        return 2
    return 1