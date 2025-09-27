"""
Predictor 94
Generated on: 2025-09-09 23:27:20
Accuracy: 57.66%
"""


# PREDICTOR 94 - Accuracy: 57.66%
# Correct predictions: 5766/10000 (57.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55 and A < 70) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10) or (C < 30 and E > 65 and D < 20) or (E < 5 and A > 50) or (C > 75 and B < 10) or (C < 5 and E > 60):
        return 4
    if (B > 85 and C > 80 and A < 80) or (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80 and A < 70) or (C <= 10 and E < 60) or (A > 70 and B < 30 and D > 60):
        return 3
    else:
        return 1