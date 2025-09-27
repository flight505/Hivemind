"""
Predictor 1130
Generated on: 2025-09-10 01:35:54
Accuracy: 49.05%
"""


# PREDICTOR 1130 - Accuracy: 49.05%
# Correct predictions: 4905/10000 (49.05%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 80 and B > 20 and E > 50) or (B > 85 and C < 10) or (C > 60 and E < 40 and A < 50):
        return 4
    elif (C > 90 and B < 20) or (B > 70 and C > 90) or (B > 90) or (D < 5 and B > 60):
        return 2
    elif (B < 10 and D > 80) or (A > 50 and C < 50 and D > 70):
        return 3
    else:
        return 1