"""
Predictor 82
Generated on: 2025-09-09 23:27:20
Accuracy: 54.87%
"""


# PREDICTOR 82 - Accuracy: 54.87%
# Correct predictions: 5487/10000 (54.87%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (B > 60 and E > 80) or (B < 20 and C > 60 and D < 30) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10):
        return 4
    if (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40) or (C > 60 and E > 80) or (B > 80 and C > 70) or (B > 90 and D > 90 and E < 15):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60 and B < 70):
        return 3
    else:
        return 1