"""
Predictor 1318
Generated on: 2025-09-10 02:07:02
Accuracy: 53.36%
"""


# PREDICTOR 1318 - Accuracy: 53.36%
# Correct predictions: 5336/10000 (53.36%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B < 10 and C > 70) or (A > 75 and E > 85) or (B < 10 and C > 90) or (C < 15 and D > 80 and B > 80) or (A > 90 and C < 15 and E > 60) or (B < 30 and C > 75) or (A > 60 and B > 80 and C < 15 and D > 80) or (A > 75 and B < 30 and E > 85):
        return 4
    elif (B > 90 and E > 85) or (A > 90 and E < 10 and B < 50):
        return 2
    elif (B > 75 and C > 70 and D > 80) or (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and B > 75 and C > 70 and D > 80 and E < 30):
        return 3
    else:
        return 1