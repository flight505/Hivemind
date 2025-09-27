"""
Predictor 1470
Generated on: 2025-09-10 02:31:46
Accuracy: 54.15%
"""


# PREDICTOR 1470 - Accuracy: 54.15%
# Correct predictions: 5415/10000 (54.15%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E > 80 and D < 40) or (B > 75 and C < 40) or (A > 70 and B < 20 and C > 80) or (E < 10 and A < 30 and C < 45) or (A > 70 and D < 40 and E > 80):
        return 4
    elif (B > 85 and C > 80 and D > 50) or (A < 10 and B < 5 and C > 90) or (B < 10 and D < 10 and E > 70):
        return 2
    elif (A > 30 and B > 65 and C > 70 and D > 75) or (A > 95 and D > 85) or (A > 45 and C < 50 and D > 60) or (A > 45 and B > 45 and C > 90 and D > 90):
        return 3
    else:
        return 1