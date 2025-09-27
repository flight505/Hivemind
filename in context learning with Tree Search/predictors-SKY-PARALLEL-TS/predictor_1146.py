"""
Predictor 1146
Generated on: 2025-09-10 01:37:38
Accuracy: 53.08%
"""


# PREDICTOR 1146 - Accuracy: 53.08%
# Correct predictions: 5308/10000 (53.08%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 90 and D < 20 and E > 90) or (C > 80 and B < 30 and E < 20) or (B > 90 and E > 90) or (B > 80 and C > 95 and E < 20) or (C > 90 and D < 20 and E > 50) or (A > 80 and B > 70 and E > 70) or (A < 20 and C > 75 and D < 30) or (C < 15 and D > 80):
        return 4
    elif (B > 60 and C > 70 and E < 30) or (A > 90 and E < 10 and C < 50) or (B > 85 and C > 80) or (A + B > 140 and E > 90):
        return 2
    elif (C > 90 and D > 90 and E > 90) or (D > 90 and E < 10) or (A > 60 and C < 15 and E < 20) or (A < 50 and C > 90 and D > 70 and E < 20) or (B > 50 and C + D + E > 280):
        return 3
    else:
        return 1