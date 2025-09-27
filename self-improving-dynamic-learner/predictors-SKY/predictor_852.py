"""
Predictor 852
Generated on: 2025-09-09 21:28:57
Accuracy: 53.20%
"""


# PREDICTOR 852 - Accuracy: 53.20%
# Correct predictions: 5320/10000 (53.20%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 60 and E < 20:
        return 2
    if B < 30 and C > 70 and E < 20:
        return 4
    if 40 <= B <= 75 and 40 <= C <= 50:
        return 3
    if B > 45 and C < 20 and E > 40:
        return 2
    if B > 60 and C < 60 and E > 70:
        return 4
    if B > 60 and C > 75:
        if A < 35:
            return 2
        else:
            return 1
    if C < 25 and E > 90:
        return 4
    if C < 10 and D > 80 and E > 60:
        return 4
    if B < 20 and C < 20:
        return 3
    if E < 15 and B < 60:
        if D > 80:
            return 1
        else:
            return 3
    if B < 40 and C < 30 and D > 70 and E > 40:
        return 3
    if B < 50 and C < 40 and D > 80 and E > 80:
        return 3
    if B < 50 and D < 20 and E > 70:
        return 2
    return 1