"""
Predictor 1277
Generated on: 2025-09-10 01:58:17
Accuracy: 54.07%
"""


# PREDICTOR 1277 - Accuracy: 54.07%
# Correct predictions: 5407/10000 (54.07%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 80 and C < 20) or (C < 30 and E > 65 and B > 50 and D < 80) or (C > 90 and E < 10 and D > 50 and B < 50) or (C < 35 and E < 15 and B > 50 and D < 55):
        return 4
    elif (B > 70 and C > 40 and D > 60) or (A > 80 and B > 80):
        return 2
    elif (B > 80 and D > 90 and E > 90) or (A > 40 and C < 35 and D > 70 and E < 5):
        return 3
    else:
        return 1