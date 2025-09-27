"""
Predictor 1371
Generated on: 2025-09-10 02:16:28
Accuracy: 54.88%
"""


# PREDICTOR 1371 - Accuracy: 54.88%
# Correct predictions: 5488/10000 (54.88%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 15 and D > 90) or (A < 10 and C > 65 and D < 35 and E < 30) or (A > 90 and B > 70 and C < 20 and D > 60) or (B > 80 and C > 60 and D < 25 and E > 95) or (B > 70 and D < 20 and E > 90):
        return 4
    elif (B > 90 and C > 80) or (B > 70 and C > 90 and E < 5) or (A < 30 and B > 90 and C > 80 and D > 85):
        return 2
    elif (B > 70 and C < 20) or (B > 90 and C > 60 and D > 90) or (C < 15 and D > 45 and E < 30 and A < 40 and B > 45) or (A < 30 and B > 70 and C < 20 and D > 40):
        return 3
    else:
        return 1