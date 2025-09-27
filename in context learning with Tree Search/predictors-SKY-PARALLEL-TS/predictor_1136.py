"""
Predictor 1136
Generated on: 2025-09-10 01:35:54
Accuracy: 50.80%
"""


# PREDICTOR 1136 - Accuracy: 50.80%
# Correct predictions: 5080/10000 (50.80%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 75 and B < 25 and D < 15) or (A > 50 and B < 20 and C > 75 and D < 35 and E < 20) or (A > 60 and B < 15 and C > 45 and D < 25 and E < 10) or (A > 60 and B < 35 and C > 40 and D > 40):
        return 4
    elif (B > 85 and C > 75) or (B > 95 and E > 80):
        return 2
    elif (C > 75 and D > 85 and E > 80) or (A < 5 and C < 15) or (C < 30 and D > 95):
        return 3
    else:
        return 1