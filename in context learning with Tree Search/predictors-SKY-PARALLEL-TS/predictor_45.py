"""
Predictor 45
Generated on: 2025-09-09 23:21:45
Accuracy: 56.78%
"""


# PREDICTOR 45 - Accuracy: 56.78%
# Correct predictions: 5678/10000 (56.78%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 25 and (D > 50 or E > 70)) or (E > 80 and D < 40):
        return 4
    if (B > 85 and C > 80) or (A > 90 and E < 10):
        return 2
    if (D < 15 and C > 40 and B < 80) or (C < 15 and B < 70) or (B < 15 and D > 80 and C < 60) or (A < 5 and C < 10):
        return 3
    else:
        return 1