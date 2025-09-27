"""
Predictor 822
Generated on: 2025-09-09 21:12:57
Accuracy: 53.27%
"""


# PREDICTOR 822 - Accuracy: 53.27%
# Correct predictions: 5327/10000 (53.27%)

def predict_output(A, B, C, D, E):
    if C > 80 and B > 70 and E < 50:
        return 1
    if B < 10 and C > 70:
        return 1
    if B > 70 and C > 70 and E < 20:
        return 1
    if B > 80 and C > 50 and E < 50:
        return 1
    if B > 90 and E < 35:
        return 1
    if B > 80 and C > 50:
        if E > 50:
            return 2
        return 1
    if E > 90:
        if B > 50 and C > 40:
            if D > 80:
                return 3
            return 4
        if C < 30:
            return 4
        return 1
    if C < 25 and E > 50 and B < 60:
        return 4
    if B < 10 and E > 70:
        return 4
    if C < 10 and B < 20 and E > 50:
        return 4
    if B > 60 and D < 30 and E < 40 and C > 30:
        return 4
    if B < 40 and C > 60 and D > 40 and E < 40:
        return 4
    if B < 20 and C > 60 and E < 20 and D > 50:
        return 4
    if B > 70 and C < 15 and E > 60:
        return 4
    if D > 90 and B > 60 and E > 70:
        return 3
    if D > 90 and E < 20 and C > 50:
        return 3
    if C > 90 and E < 20:
        return 3
    if C > 80 and B < 40 and E < 30:
        return 3
    if B > 60 and C > 70 and D < 10 and E < 50:
        return 3
    if B < 25 and C < 35 and D > 80:
        return 3
    if B < 20 and C < 20:
        return 3
    if B < 40 and C < 45 and E < 40 and D < 50:
        return 3
    if B > 60 and C > 70:
        return 2
    if B > 80 and C < 25 and D < 50:
        return 2
    if B > 80 and E < 20:
        return 2
    if C > 80 and E > 80 and B < 30:
        return 2
    return 1