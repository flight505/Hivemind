"""
Predictor 1154
Generated on: 2025-09-10 01:37:38
Accuracy: 51.04%
"""


# PREDICTOR 1154 - Accuracy: 51.04%
# Correct predictions: 5104/10000 (51.04%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90 and E > 80) or (A < 10 and B < 10 and C > 30 and D > 40) or (A > 50 and C < 35 and D < 30 and E > 70 and B < 40) or (B < 10 and C > 40 and D > 60) or (A > 60 and B < 5 and C > 40 and D > 60):
        return 4
    elif (A > 90 and E < 10 and B < 30) or (D < 5 and E > 70 and A < 20) or (B > 80 and C > 80):
        return 2
    elif (A > 60 and B < 20 and D < 10 and E < 10) or (C > 80 and D > 70 and A < 50) or (A > 50 and B < 40 and C < 20 and D < 30):
        return 3
    else:
        return 1