"""
Predictor 1220
Generated on: 2025-09-10 01:46:44
Accuracy: 48.74%
"""


# PREDICTOR 1220 - Accuracy: 48.74%
# Correct predictions: 4874/10000 (48.74%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B > 60 and D < 50 and C < 80):
        return 4
    if (A > 90 and E < 10) or (B > 85 and C > 80 and A > 20):
        return 2
    if A > 80 and D > 90:
        return 3
    else:
        return 1