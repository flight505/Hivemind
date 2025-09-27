"""
Predictor 970
Generated on: 2025-09-10 01:09:35
Accuracy: 61.44%
"""


# PREDICTOR 970 - Accuracy: 61.44%
# Correct predictions: 6144/10000 (61.44%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 55 and E > 50) or (C < 25 and E > 70) or (B > 65 and E < 10 and D > 60 and C > 20) or (C > 85 and E < 5) or (A > 80 and B < 10 and D > 70 and E < 10) or (A + B < 100 and C > 50 and D > 50 and E < 30):
        return 4
    elif (B > 80 and C > 75 and D > 20) or (B > 70 and D < 20 and A < 50 and E > 40) or (D < 10 and E > 50) or (B < 15 and E > 55 and D < 10):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60 and B < 60) or (A < 60 and B < 30 and C < 20 and D < 30) or (A > 40 and B < 10 and C < 20):
        return 3
    else:
        return 1