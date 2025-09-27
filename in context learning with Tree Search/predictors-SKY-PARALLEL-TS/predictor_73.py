"""
Predictor 73
Generated on: 2025-09-09 23:24:50
Accuracy: 53.48%
"""


# PREDICTOR 73 - Accuracy: 53.48%
# Correct predictions: 5348/10000 (53.48%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 30) or (E > 70 and C < 10) or (E > 70 and D < 5 and B >= 20) or (E > 70 and B < 30 and D >= 5) or (C < 15 and D > 55):
        return 4
    if (D < 5 and E > 70 and B < 20) or (A < 5 and C < 15 and E > 50) or (A < 5 and B > 90 and E > 50) or (B > 60 and E > 75) or (B > 85 and C > 80):
        return 2
    if (A > 60 and C < 15 and E < 20) or (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60):
        return 3
    else:
        return 1