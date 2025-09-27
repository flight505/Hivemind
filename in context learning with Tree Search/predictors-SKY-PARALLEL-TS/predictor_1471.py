"""
Predictor 1471
Generated on: 2025-09-10 02:31:46
Accuracy: 52.66%
"""


# PREDICTOR 1471 - Accuracy: 52.66%
# Correct predictions: 5266/10000 (52.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E > 80 and D < 40) or (B > 70 and C < 40) or (A > 60 and B < 20 and C > 80) or (D < 30 and E < 10):
        return 4
    elif (A < 10 and B < 5 and C > 90 and E > 70) or (B > 85 and C > 80 and E < 10):
        return 2
    elif (B > 60 and C > 70 and D > 75) or (A > 95 and D > 85) or (A > 45 and C < 50 and D > 60):
        return 3
    else:
        return 1