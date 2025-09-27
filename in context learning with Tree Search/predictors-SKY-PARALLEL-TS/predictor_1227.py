"""
Predictor 1227
Generated on: 2025-09-10 01:48:40
Accuracy: 54.29%
"""


# PREDICTOR 1227 - Accuracy: 54.29%
# Correct predictions: 5429/10000 (54.29%)

def predict_output(A, B, C, D, E):
    if B > 90 and E < 20:
        return 3
    elif (B > 85 and C > 80 and A < 50) or (A < 10 and E > 80 and B < 60):
        return 2
    elif (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 60 and D < 20) or (C < 30 and E > 80 and B > 60) or (B > 70 and D < 25 and E > 70) or (C > 80 and E < 10) or (E < 20 and A < 40 and C < 40) or (E >= 80 and D < 25) or (C > 60 and E < 10):
        return 4
    else:
        return 1