"""
Predictor 833
Generated on: 2025-09-10 00:53:24
Accuracy: 51.71%
"""


# PREDICTOR 833 - Accuracy: 51.71%
# Correct predictions: 5171/10000 (51.71%)

def predict_output(A, B, C, D, E):
    if ((A < 30 and B > 70) or
        (C < 20 and D > 80) or
        (E > 80 and C < 30 and B < 70 and A < 50) or
        (A > 85 and B > 85 and C < 30) or
        (A < 25 and B < 20 and C > 65 and D < 25) or
        (C < 10 and B > 70 and D > 90) or
        (B > 70 and C < 10)):
        return 4
    elif ((B >= 80 and C > 60) or
          (A > 70 and B < 25 and C > 90 and D < 15 and E > 60)):
        return 2
    elif ((D < 25 and C > 40 and B < 50) or
          (A > 90 and D > 90 and C < 30)):
        return 3
    else:
        return 1