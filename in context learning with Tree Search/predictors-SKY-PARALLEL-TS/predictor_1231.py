"""
Predictor 1231
Generated on: 2025-09-10 01:48:40
Accuracy: 49.08%
"""


# PREDICTOR 1231 - Accuracy: 49.08%
# Correct predictions: 4908/10000 (49.08%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (A > 60 and B > 50 and C < 50 and D < 40 and E > 60) or (D > 65 and E < 15 and A > 60) or (B < 5 and C < 10 and E > 50) or (A > 70 and B > 70 and C < 25 and D > 75) or (B < 10 and C < 15 and E > 60):
        return 4
    elif (B < 10 and D > 40) or (B > 70 and C < 20):
        return 3
    elif (B > 85 and C > 60) or (E > 70 and D < 5 and B < 20):
        return 2
    else:
        return 1