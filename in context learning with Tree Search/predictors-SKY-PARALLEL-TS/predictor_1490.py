"""
Predictor 1490
Generated on: 2025-09-10 02:35:36
Accuracy: 57.65%
"""


# PREDICTOR 1490 - Accuracy: 57.65%
# Correct predictions: 5765/10000 (57.65%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 80 and E > 90) or (A > 60 and C < 15 and D > 60) or (B > 90 and C < 10) or (C < 5 and E > 60):
        return 4
    elif (A < 15 and B > 85):
        return 2
    elif (A > 60 and B > 80 and C < 55 and D > 95):
        return 3
    else:
        return 1