"""
Predictor 1283
Generated on: 2025-09-10 01:58:17
Accuracy: 56.31%
"""


# PREDICTOR 1283 - Accuracy: 56.31%
# Correct predictions: 5631/10000 (56.31%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (40 < A < 50 and B > 60 and C < 35 and D > 60 and E > 50) or (A > 90 and B > 60 and C < 25 and D > 75 and E < 35) or (B < 10 and C < 10 and D < 10 and E > 60) or (A > 50 and B < 50 and C > 55 and D < 25 and E > 75) or (C < 30 and E > 65 and A > 10 and D < 95 and B > 60) or (A > 45 and B > 60 and C < 35 and D > 60):
        return 4
    elif A > 90 and E < 10 or (A < 10 and B < 20 and C < 10 and D > 80 and E > 70) or (A > 75 and B > 85 and C < 50 and D > 55 and E > 70):
        return 2
    elif B < 10 and D > 80 or (A < 35 and B > 65 and C < 35 and D > 95 and E > 80) or (A > 90 and B < 15 and C > 40 and D > 90 and E < 10):
        return 3
    else:
        return 1