"""
Predictor 1491
Generated on: 2025-09-10 02:35:36
Accuracy: 59.84%
"""


# PREDICTOR 1491 - Accuracy: 59.84%
# Correct predictions: 5984/10000 (59.84%)

def predict_output(A, B, C, D, E):
    if A < 20 and B > 85:
        return 2
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and E > 50) or (B > 80 and E > 90 and D < 25) or (A > 60 and C < 15 and D > 60) or (B > 90 and C < 10 and A > 10) or (C < 5 and E > 60) or (B > 50 and C < 20 and E > 55):
        return 4
    if B > 75 and D > 95 or (A > 50 and C < 55 and D > 90):
        return 3
    else:
        return 1