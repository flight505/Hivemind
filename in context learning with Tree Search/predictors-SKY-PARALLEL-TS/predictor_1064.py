"""
Predictor 1064
Generated on: 2025-09-10 01:25:44
Accuracy: 51.39%
"""


# PREDICTOR 1064 - Accuracy: 51.39%
# Correct predictions: 5139/10000 (51.39%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 80 and D < 20 and E > 90) or (C > 80 and A > 60) or (B < 10 and E < 20):
        return 4
    elif (B > 85 and C > 80) or (B > 85 and D > 80):
        return 2
    elif (A > 45 and C < 50 and D > 60 and B > 40) or (C <= 10 and E < 60 and B < 50) or (A < 5 and C < 10 and D < 10) or (A > 90 and B < 50):
        return 3
    else:
        return 1