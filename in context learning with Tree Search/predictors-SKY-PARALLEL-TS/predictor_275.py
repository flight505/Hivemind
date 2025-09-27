"""
Predictor 275
Generated on: 2025-09-09 23:43:38
Accuracy: 56.28%
"""


# PREDICTOR 275 - Accuracy: 56.28%
# Correct predictions: 5628/10000 (56.28%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (A > 50 and B < 20 and C < 20 and E > 60):
        return 4
    elif B > 90 and C < 50:
        return 2
    elif (A > 70 and B < 15 and C < 5) or (A > 80 and B < 10 and D < 10):
        return 3
    else:
        return 1