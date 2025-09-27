"""
Predictor 1008
Generated on: 2025-09-10 01:15:51
Accuracy: 49.52%
"""


# PREDICTOR 1008 - Accuracy: 49.52%
# Correct predictions: 4952/10000 (49.52%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 70 and C < 30) or (C > 80 and B < 40) or (B > 80 and E > 90) or (A > 80 and E > 90):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80 and D < 15):
        return 2
    elif (B > 70 and D > 90) or (C < 5 and B > 50) or (B < 20 and C > 30 and A < 20):
        return 3
    else:
        return 1