"""
Predictor 1324
Generated on: 2025-09-10 02:07:02
Accuracy: 54.15%
"""


# PREDICTOR 1324 - Accuracy: 54.15%
# Correct predictions: 5415/10000 (54.15%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 20 and E < 20:
        return 3
    if B > 85:
        return 2
    if (A < 10 and B > 70 and C < 70 and E < 70) or (C < 25 and E > 80) or (C < 15 and D > 90):
        return 4
    else:
        return 1