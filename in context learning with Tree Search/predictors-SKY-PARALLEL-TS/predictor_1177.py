"""
Predictor 1177
Generated on: 2025-09-10 01:39:40
Accuracy: 49.55%
"""


# PREDICTOR 1177 - Accuracy: 49.55%
# Correct predictions: 4955/10000 (49.55%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B < 10 and C > 50 and D > 65) or (C < 10 and E > 50):
        return 4
    elif B > 75 or (E > 60 and A < 30 and C < 45):
        return 2
    elif (A < 30 and B < 25 and C < 10 and D > 80) or (A > 50 and B < 45 and C < 22 and D < 35 and E > 10):
        return 3
    else:
        return 1