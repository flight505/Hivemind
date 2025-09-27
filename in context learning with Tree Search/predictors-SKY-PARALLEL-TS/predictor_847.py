"""
Predictor 847
Generated on: 2025-09-10 00:55:50
Accuracy: 53.57%
"""


# PREDICTOR 847 - Accuracy: 53.57%
# Correct predictions: 5357/10000 (53.57%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 55) or (A > 80 and B < 30 and C < 30 and D < 30 and E > 70):
        return 4
    elif B > 70 and C > 45 and A > 20:
        return 2
    elif (B > 60 and C > 70 and D > 60 and E < 20) or (A > 20 and B < 50 and C < 25 and D > 15 and D < 40 and E < 40):
        return 3
    else:
        return 1