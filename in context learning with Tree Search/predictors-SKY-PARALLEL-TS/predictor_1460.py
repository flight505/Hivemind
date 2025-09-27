"""
Predictor 1460
Generated on: 2025-09-10 02:31:46
Accuracy: 56.42%
"""


# PREDICTOR 1460 - Accuracy: 56.42%
# Correct predictions: 5642/10000 (56.42%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 80) or (C < 10 and D < 10 and E > 50):
        return 4
    elif B > 80 and E <= 20 and D > 70 and C > 30:
        return 2
    elif 40 < A < 60 and D < 25 and E < 30 and C < 20 and B < 40:
        return 3
    else:
        return 1