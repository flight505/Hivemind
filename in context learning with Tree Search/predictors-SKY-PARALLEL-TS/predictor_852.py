"""
Predictor 852
Generated on: 2025-09-10 00:55:50
Accuracy: 56.85%
"""


# PREDICTOR 852 - Accuracy: 56.85%
# Correct predictions: 5685/10000 (56.85%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A > 80 and C < 25 and D > 75) or
        (C > 65 and D > 75 and E < 5) or
        (A > 90 and E > 90 and D < 30) or
        (A > 45 and C > 50 and D < 30 and E < 10) or
        (A > 60 and C > 75 and D < 15)):
        return 4
    elif ((B > 90 and C < 25 and D > 85 and E > 80) or
          (A > 70 and B > 60 and C < 45 and D > 50 and E > 50)):
        return 2
    elif ((45 < A < 55 and C > 50 and D > 55 and E < 15) or
          (A < 10 and B > 40 and C < 20 and D < 30 and E > 40) or
          (A < 15 and B < 10 and C > 30 and D < 30 and E > 40) or
          (A > 50 and C < 50 and D > 70 and B > 40)):
        return 3
    else:
        return 1