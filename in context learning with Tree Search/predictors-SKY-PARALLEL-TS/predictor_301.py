"""
Predictor 301
Generated on: 2025-09-09 23:47:14
Accuracy: 54.12%
"""


# PREDICTOR 301 - Accuracy: 54.12%
# Correct predictions: 5412/10000 (54.12%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and D < 50) or
        (C < 10 and D > 90) or
        (A < 40 and E < 20 and C > 40) or
        (A > 95 and E > 85) or
        (B < 15 and C > 75 and D < 20 and E > 60)):
        return 4
    elif ((A > 90 and E < 10 and B > 50) or
          (B > 70 and C > 70 and E < 15)):
        return 2
    elif ((B < 10 and D > 80) or
          (C < 20 and D < 25)):
        return 3
    else:
        return 1