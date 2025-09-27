"""
Predictor 91
Generated on: 2025-09-09 23:27:20
Accuracy: 55.02%
"""


# PREDICTOR 91 - Accuracy: 55.02%
# Correct predictions: 5502/10000 (55.02%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55 and E > 50) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10) or (B > 80 and E > 90) or (D < 5 and E > 60) or (C < 35 and D > 50 and E > 70 and A < 50):
        return 4
    if (B > 85 and C > 80 and E > 30) or (B > 70 and C > 80 and A < 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60) or (C > 80 and D > 65) or (B < 20 and A < 40 and C < 30):
        return 3
    else:
        return 1