"""
Predictor 1149
Generated on: 2025-09-10 01:37:38
Accuracy: 50.86%
"""


# PREDICTOR 1149 - Accuracy: 50.86%
# Correct predictions: 5086/10000 (50.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 25 and E > 65):
        return 4
    elif (B > 80 and C > 90 and D > 80 and E < 10) or (D > 75 and E < 30 and B < 60) or (B < 10 and A > 60):
        return 3
    elif (B > 75 and D > 70 and C < 50) or (A > 40 and B > 70 and E < 45):
        return 2
    else:
        return 1