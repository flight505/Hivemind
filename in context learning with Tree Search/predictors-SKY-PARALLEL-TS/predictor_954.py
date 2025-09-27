"""
Predictor 954
Generated on: 2025-09-10 01:09:35
Accuracy: 46.85%
"""


# PREDICTOR 954 - Accuracy: 46.85%
# Correct predictions: 4685/10000 (46.85%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B < 20 and C > 60):
        return 4
    elif (B > 90) or (B >= 70 and C >= 70) or (D < 20 and E > 60):
        return 2
    elif (B > 50 and C < 20 and D < 25) or (B < 10 and C < 20 and D > 50) or (A < 10 and C < 15 and D > 30):
        return 3
    else:
        return 1