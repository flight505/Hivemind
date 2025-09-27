"""
Predictor 958
Generated on: 2025-09-10 01:09:35
Accuracy: 54.45%
"""


# PREDICTOR 958 - Accuracy: 54.45%
# Correct predictions: 5445/10000 (54.45%)

def predict_output(A, B, C, D, E):
    if ((A < 20 and B > 70 and E < 20) or
        (C < 15 and D > 70) or
        (B > 90 and D < 20 and E > 90) or
        (D < 30 and E > 45 and C > 50 and A > 20) or
        (C > 80 and E < 35 and A > 30) or
        (C < 30 and D < 10 and E > 50 and A < 70)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 70 and D < 20 and A < 50 and E > 40)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (C <= 10 and E < 60)):
        return 3
    else:
        return 1