"""
Predictor 1474
Generated on: 2025-09-10 02:31:46
Accuracy: 53.30%
"""


# PREDICTOR 1474 - Accuracy: 53.30%
# Correct predictions: 5330/10000 (53.30%)

def predict_output(A, B, C, D, E):
    if (A < 15 and B > 70 and C > 20) or (C < 15 and D > 80) or (A > 65 and C < 30 and D > 50 and B < 70) or (C > 90 and E < 10):
        return 4
    elif (A > 90 and B > 70) or (A < 10 and B > 50 and E > 50):
        return 2
    elif (B < 10 and D > 80) or (A < 10 and B < 10 and C > 70):
        return 3
    else:
        return 1