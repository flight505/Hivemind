"""
Predictor 375
Generated on: 2025-09-09 15:59:22
Accuracy: 53.83%
"""


# PREDICTOR 375 - Accuracy: 53.83%
# Correct predictions: 5383/10000 (53.83%)

def predict_output(A, B, C, D, E):
    if C > 70 and E >= 70:
        if B >= 60:
            return 2
        elif A > 50:
            return 4
        else:
            return 1
    if C > 90 and E < 30:
        return 4
    if B > 90 and C < 20:
        return 4
    if E > 80 and C < 25 and B > 20:
        return 4
    if B < 20 and 30 < C < 50 and 30 < E < 50:
        return 4
    if B < 20 and C > 50 and D < 20:
        return 3
    if B < 20 and C < 20 and E < 40:
        return 3
    return 1