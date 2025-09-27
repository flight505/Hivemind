"""
Predictor 1274
Generated on: 2025-09-10 01:54:58
Accuracy: 53.66%
"""


# PREDICTOR 1274 - Accuracy: 53.66%
# Correct predictions: 5366/10000 (53.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 15 and B > 30 and C > 55 and D < 40 and E > 40) or (A < 20 and B > 70 and C < 5 and D < 20 and E > 90) or (A > 70 and B > 70 and C > 95 and D < 20 and E > 80) or (A > 40 and B > 40 and C < 5 and D < 40 and E > 65):
        return 4
    elif (A > 90 and E < 10) or (A > 50 and B > 40 and C > 90 and D < 10 and E > 60):
        return 2
    elif (B < 10 and D > 80) or (A < 10 and B > 20 and C < 20 and D > 60 and E < 30) or (A < 40 and B < 25 and C < 15 and D > 65 and E < 25):
        return 3
    else:
        return 1