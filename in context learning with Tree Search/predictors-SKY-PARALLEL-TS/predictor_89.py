"""
Predictor 89
Generated on: 2025-09-09 23:27:20
Accuracy: 55.57%
"""


# PREDICTOR 89 - Accuracy: 55.57%
# Correct predictions: 5557/10000 (55.57%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55 and E > 50) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10) or (D < 5 and E > 60) or (B > 80 and E > 90) or (C < 35 and E > 70):
        return 4
    if (B > 85 and C > 80 and D < 50) or (B > 70 and D < 20 and A < 50 and E > 40) or (B > 70 and C > 80 and A < 50 and E < 15):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60) or (C > 80 and D > 70 and A < 50) or (B < 20 and A < 40):
        return 3
    else:
        return 1