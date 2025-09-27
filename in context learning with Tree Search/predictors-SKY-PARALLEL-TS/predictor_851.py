"""
Predictor 851
Generated on: 2025-09-10 00:55:50
Accuracy: 49.52%
"""


# PREDICTOR 851 - Accuracy: 49.52%
# Correct predictions: 4952/10000 (49.52%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 50) or (C > 90) or (E > 90) or (C < 20 and D > 70) or (A < 15 and C > 60 and D < 20) or (E > 85 and D < 20) or (C > 90 and E > 90):
        return 4
    elif (B > 85 and C > 80) or (A < 10 and E > 90):
        return 2
    elif (A > 70 and B < 30 and C > 70 and D < 10) or (A > 50 and E < 10 and D < 30):
        return 3
    else:
        return 1