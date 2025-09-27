"""
Predictor 1425
Generated on: 2025-09-10 02:26:25
Accuracy: 56.62%
"""


# PREDICTOR 1425 - Accuracy: 56.62%
# Correct predictions: 5662/10000 (56.62%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 20 and D > 75 and E > 80) or (C < 30 and E > 80 and A > 60) or (E > 90 and A > 80) or (B > 70 and C < 25 and D > 95):
        return 4
    elif (B > 75 and C > 90) or (B > 90 and C > 75) or (B > 90 and E < 25) or (A > 90 and E < 10) or (A > 60 and B < 20 and C > 70 and E > 70):
        return 2
    elif (A > 50 and C < 50 and D > 65 and B > 40) or (A < 15 and C > 80 and D < 15) or (A < 40 and B > 70 and C < 50 and D > 75) or (C <= 10 and E < 60) or (B > 75 and C > 70 and D > 80) or (A < 10 and C < 30 and D < 20):
        return 3
    else:
        return 1