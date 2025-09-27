"""
Predictor 884
Generated on: 2025-09-09 21:44:17
Accuracy: 58.10%
"""


# PREDICTOR 884 - Accuracy: 58.10%
# Correct predictions: 5810/10000 (58.10%)

def predict_output(A, B, C, D, E):
    if C < 20 and E > 80:
        return 4
    if B > 80 and C < 30 and E < 20:
        return 1
    if D > 90 and E > 80:
        return 4
    if C > 80 and B < 20:
        return 1
    if D > 70 and C < 40 and E > 70 and B > 50:
        return 3
    if B > 60 and C < 20:
        return 4
    if B < 40 and C > 50 and E < 20:
        return 4
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 90 and 30 <= C < 50:
        return 2
    if D > 80 and C < 15:
        return 3
    if B < 30 and C < 20 and E < 30:
        return 3
    return 1