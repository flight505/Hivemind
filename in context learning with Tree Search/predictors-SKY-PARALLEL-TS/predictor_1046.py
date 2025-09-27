"""
Predictor 1046
Generated on: 2025-09-10 01:23:11
Accuracy: 54.60%
"""


# PREDICTOR 1046 - Accuracy: 54.60%
# Correct predictions: 5460/10000 (54.60%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or (C < 10 and D > 90) or (A > 70 and B < 35 and C < 15 and D > 50) or (A < 30 and C > 75 and D < 30 and E > 50) or (C > 85 and E < 20 and B < 30)):
        return 4
    elif ((A > 90 and E < 10) or (B > 85 and C > 80) or (A < 30 and B > 85 and C > 70) or (B > 65 and C > 80 and D < 30) or (A < 15 and B > 50 and C < 15 and D > 70)):
        return 2
    elif ((B < 10 and D > 80) or (A > 45 and C < 50 and D > 55 and B > 35) or (A < 40 and B < 50 and C < 15 and D > 70 and E > 40) or (A > 45 and C < 30 and B < 40 and D < 35) or (A > 95 and B < 20 and C < 50 and D < 50) or (A < 30 and C > 80 and D < 10) or (C > 90 and D < 25 and E < 30)):
        return 3
    else:
        return 1