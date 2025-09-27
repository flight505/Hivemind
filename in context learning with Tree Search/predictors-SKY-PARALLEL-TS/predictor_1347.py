"""
Predictor 1347
Generated on: 2025-09-10 02:10:24
Accuracy: 59.18%
"""


# PREDICTOR 1347 - Accuracy: 59.18%
# Correct predictions: 5918/10000 (59.18%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 30) or (C < 15 and E > 60) or (A > 50 and B > 30 and C < 40 and D > 60 and E < 10) or (C > 70 and B < 25 and D < 40 and D > 20 and E < 20) or (C < 30 and E > 65):
        return 4
    if (B > 85 and C > 80 and A < 80) or (B > 75 and C > 85) or (A > 70 and B > 70 and C < 50) or (A < 10 and B > 90 and D > 70):
        return 2
    if (A > 45 and C < 50 and D > 55 and B > 35 and E > 10) or (A < 10 and B > 90 and D < 25 and E < 25) or (A < 40 and B < 30 and C < 25 and D < 40) or (D < 15 and C > 40 and B < 80):
        return 3
    else:
        return 1