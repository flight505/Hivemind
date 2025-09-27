"""
Predictor 1374
Generated on: 2025-09-10 02:16:28
Accuracy: 56.01%
"""


# PREDICTOR 1374 - Accuracy: 56.01%
# Correct predictions: 5601/10000 (56.01%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (C < 20 and E > 80 and B > 50) or (B > 70 and D < 20) or (A < 20 and C > 75 and D < 30) or (30 < A < 50 and B > 50 and C > 80 and E < 5) or (A > 70 and B < 20 and C < 15 and E > 50) or (A > 40 and B < 25 and C < 35 and D < 20 and E > 60):
        return 4
    elif (B > 85 and C > 80 and A < 60) or (A < 20 and B > 90 and C < 35 and D > 70) or (B > 70 and E > 80 and C > 50) or (A < 50 and B > 70 and D < 20 and E > 40) or (A < 50 and B > 70 and C > 50 and E > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70) or (D < 15 and C > 40) or (C < 10 and E < 60) or (A < 10 and B > 80 and C > 80 and D < 5) or (A > 50 and B < 30 and C < 15 and E < 20):
        return 3
    else:
        return 1