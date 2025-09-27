"""
Predictor 1183
Generated on: 2025-09-10 01:39:40
Accuracy: 58.88%
"""


# PREDICTOR 1183 - Accuracy: 58.88%
# Correct predictions: 5888/10000 (58.88%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and E > 80) or (A < 40 and B > 60 and D < 30) or (A > 85 and C < 30 and D > 65) or (C < 25 and E > 70):
        return 4
    elif (B > 85 and C > 80) or (A > 90 and E < 10) or (A < 10 and C > 80 and D < 10 and E > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (C < 15 and D > 30 and B > 30) or (B > 65 and C < 35 and D > 90 and A < 40) or (A > 80 and C < 25 and D > 90 and B > 50):
        return 3
    else:
        return 1