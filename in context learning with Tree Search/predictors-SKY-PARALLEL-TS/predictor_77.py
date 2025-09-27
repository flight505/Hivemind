"""
Predictor 77
Generated on: 2025-09-09 23:27:20
Accuracy: 59.02%
"""


# PREDICTOR 77 - Accuracy: 59.02%
# Correct predictions: 5902/10000 (59.02%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10) or (A > 75 and B < 5 and C < 20) or (B > 75 and C < 12) or (C > 85 and D < 25):
        return 4
    if (B > 85 and C > 70) or (B > 70 and D < 20 and A < 50 and E > 40) or (B > 90 and C > 35 and D > 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60 and B < 60) or (A > 40 and B > 50 and C > 50 and D > 50 and E < 15) or (A > 90 and C < 35 and E > 90):
        return 3
    else:
        return 1