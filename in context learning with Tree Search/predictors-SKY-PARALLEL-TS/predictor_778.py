"""
Predictor 778
Generated on: 2025-09-10 00:46:57
Accuracy: 53.33%
"""


# PREDICTOR 778 - Accuracy: 53.33%
# Correct predictions: 5333/10000 (53.33%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (A < 30 and B < 25 and C > 40 and D > 35 and E < 10):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80) or (A < 15 and B < 25 and C < 20 and E > 70 and D < 20) or (A < 5 and B < 45 and C < 10 and D > 70 and E > 65) or (A < 20 and B > 90 and C < 40 and D > 65 and E > 55) or (A > 60 and B > 80 and C < 50 and E < 10) or (A < 40 and B > 90 and C > 90 and D < 35 and E < 40):
        return 2
    elif (B < 10 and D > 80) or (A < 10 and B < 30 and C < 15 and D < 25 and E < 50):
        return 3
    else:
        return 1