"""
Predictor 1182
Generated on: 2025-09-10 01:39:40
Accuracy: 56.18%
"""


# PREDICTOR 1182 - Accuracy: 56.18%
# Correct predictions: 5618/10000 (56.18%)

def predict_output(A, B, C, D, E):
    if A > 70 and C < 35 and D > 90:
        return 3
    if B > 65 and C < 35 and D > 90 and E > 70:
        return 3
    if A < 10 and C < 15 and B > 30 and D > 30 and E > 30:
        return 3
    if A > 50 and C < 50 and D > 70 and B > 40:
        return 3
    if (A < 10 and B > 70 and E < 30) or (C < 15 and D > 90):
        return 4
    if A < 40 and B > 60 and D < 50:
        return 4
    if A > 80 and C < 30 and D > 60:
        return 4
    if C < 30 and D > 65 and B > 40:
        return 4
    if C > 80 and D < 10 and E > 80:
        return 2
    if A > 90 and E < 10:
        return 2
    else:
        return 1