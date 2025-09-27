"""
Predictor 30
Generated on: 2025-09-09 23:19:12
Accuracy: 45.75%
"""


# PREDICTOR 30 - Accuracy: 45.75%
# Correct predictions: 4575/10000 (45.75%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 60 and D < 30 and E > 70):
        return 4
    elif (B > 70 and C > 60 and E < 30) or (A < 10 and B < 20 and E > 40):
        return 2
    elif B < 10 or A > 90 or (C < 15 and D > 60) or (B > 70 and C < 30 and D > 70) or (A > 60 and B < 20) or (B > 70 and D > 90):
        return 3
    else:
        return 1