"""
Predictor 1299
Generated on: 2025-09-10 02:02:09
Accuracy: 54.16%
"""


# PREDICTOR 1299 - Accuracy: 54.16%
# Correct predictions: 5416/10000 (54.16%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 15 and C > 75 and E < 25) or (C < 15 and D > 60 and B > 70) or (C < 5 and E > 55 and D < 40) or (A > 45 and B < 25 and C < 30 and D < 5 and E > 60) or (B + C > 150 and A < 20 and E > 80):
        return 4
    elif (B > 85 and C > 80) or (A < 40 and D < 25 and E > 50 and C > 40) or (A + E < 50 and B > 70 and D < 30):
        return 2
    elif (B < 10 and D > 80) or (C <= 10 and E < 60 and B > 20 and A < 70) or (A > 45 and C < 50 and D > 60 and B < 60) or (C < 5 and D > 90 and B < 15) or (C < 15 and D > 70 and A < 40 and B < 50) or (A > 40 and B < 50 and C < 50 and D > 45) or (A - C > 20 and D > 70 and E < 50):
        return 3
    else:
        return 1