"""
Predictor 23
Generated on: 2025-09-09 12:18:51
Accuracy: 43.06%
"""


# PREDICTOR 23 - Accuracy: 43.06%
# Correct predictions: 4306/10000 (43.06%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 65 and B < 45:
        return 4
    if B < 40 and C > 60 and E > 50:
        return 4
    if B > 90 and E < 30:
        return 2
    if C > 70 and E < 20:
        return 3
    if B < 20 and C < 25:
        return 3
    if D > 80 and B > 40 and C < 60 and E > 70:
        return 3
    if B > 60 and C > 75:
        return 2
    if B > 40 and E > 85:
        return 2
    return 1