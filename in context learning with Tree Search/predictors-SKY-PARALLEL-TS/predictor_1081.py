"""
Predictor 1081
Generated on: 2025-09-10 01:28:10
Accuracy: 48.17%
"""


# PREDICTOR 1081 - Accuracy: 48.17%
# Correct predictions: 4817/10000 (48.17%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 90 and E > 80):
        return 4
    if (B > 65 and C > 75) or (B > 90 and E < 10) or (E > 90 and B < 20 and C < 70):
        return 2
    if (C < 10 and D > 60) or (D > 90):
        return 3
    else:
        return 1