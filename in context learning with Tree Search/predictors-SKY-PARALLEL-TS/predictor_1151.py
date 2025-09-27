"""
Predictor 1151
Generated on: 2025-09-10 01:37:38
Accuracy: 55.64%
"""


# PREDICTOR 1151 - Accuracy: 55.64%
# Correct predictions: 5564/10000 (55.64%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and E > 70):
        return 4
    if (B > 80 and C > 90 and D > 80 and E < 10) or (D > 75 and E < 30 and B < 60) or (B < 10 and A > 60):
        return 3
    if B > 75 and D > 70 and C < 50:
        return 2
    else:
        return 1