"""
Predictor 1153
Generated on: 2025-09-10 01:37:38
Accuracy: 50.49%
"""


# PREDICTOR 1153 - Accuracy: 50.49%
# Correct predictions: 5049/10000 (50.49%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (B < 10 and C > 30 and D > 40) or (A > 50 and B < 40 and C < 35 and D < 30 and E > 70):
        return 4
    elif (B > 85 and C > 80) or (A > 90 and E < 10 and B < 30):
        return 2
    elif (A > 50 and B < 20 and D < 10 and E < 10) or (C > 80 and D > 70 and A < 50):
        return 3
    else:
        return 1