"""
Predictor 1178
Generated on: 2025-09-10 01:39:40
Accuracy: 45.92%
"""


# PREDICTOR 1178 - Accuracy: 45.92%
# Correct predictions: 4592/10000 (45.92%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and E > 50) or (B < 10 and D > 65):
        return 4
    elif B > 75 or (E > 60 and D < 40 and A > 10):
        return 2
    elif (B < 20 and C < 10 and D > 80) or (A > 50 and B < 45 and C < 25 and D < 35 and E > 40):
        return 3
    else:
        return 1