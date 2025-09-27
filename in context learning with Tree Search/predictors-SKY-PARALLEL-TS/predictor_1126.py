"""
Predictor 1126
Generated on: 2025-09-10 01:35:54
Accuracy: 53.77%
"""


# PREDICTOR 1126 - Accuracy: 53.77%
# Correct predictions: 5377/10000 (53.77%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (A > 60 and B < 20 and C < 15 and D < 40):
        return 4
    elif (D < 10 and E > 80) or (B > 70 and D < 15 and C > 40):
        return 2
    elif (D > 90 and C > 40 and B > 50) or (A > 60 and B < 20 and C < 15 and D > 40) or (A < 30 and E < 15 and D < 20) or (A > 50 and C < 25 and E < 40 and B < 25 and D < 20):
        return 3
    else:
        return 1