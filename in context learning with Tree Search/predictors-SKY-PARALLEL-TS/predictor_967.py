"""
Predictor 967
Generated on: 2025-09-10 01:09:35
Accuracy: 53.15%
"""


# PREDICTOR 967 - Accuracy: 53.15%
# Correct predictions: 5315/10000 (53.15%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and B > 50) or (B > 90 and D > 90) or (C > 60 and E < 10 and D > 30) or (A > 25 and B > 90 and C < 20 and D > 95):
        return 4
    elif (A < 15 and E > 90 and B < 40) or (B > 95 and C < 40) or (A < 10 and B > 25 and C > 45 and E > 90):
        return 2
    elif (A > 50 and C < 5 and D < 25 and E < 30) or (B < 10 and D > 80) or (A > 55 and B < 45 and C < 5 and D < 25):
        return 3
    else:
        return 1