"""
Predictor 424
Generated on: 2025-09-10 00:02:23
Accuracy: 58.61%
"""


# PREDICTOR 424 - Accuracy: 58.61%
# Correct predictions: 5861/10000 (58.61%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 30 and D > 70) or (C > 90 and D < 20) or (B < 5 and C > 70) or (B < 10 and E > 70) or (C < 25 and E > 70):
        return 4
    if (A > 90 and E < 10) or (B > 85 and C > 80 and A < 60 and D < 80) or (C > 70 and D < 5 and E > 60):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80 and A < 80) or (C < 10 and E < 60) or (A > 90 and B < 30 and D > 70):
        return 3
    else:
        return 1