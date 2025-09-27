"""
Predictor 85
Generated on: 2025-09-09 23:27:20
Accuracy: 59.67%
"""


# PREDICTOR 85 - Accuracy: 59.67%
# Correct predictions: 5967/10000 (59.67%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 60) or (C < 15 and D > 30) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10):
        return 4
    if (B > 85 and C > 75 and D < 60 and A < 70) or (B < 25 and E > 90) or (B > 70 and D < 20 and A < 50 and E > 40):
        return 2
    if (A > 50 and C <= 50 and D > 60 and B > 30) or (A < 50 and D < 30 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60):
        return 3
    else:
        return 1