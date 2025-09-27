"""
Predictor 1212
Generated on: 2025-09-10 01:46:44
Accuracy: 48.63%
"""


# PREDICTOR 1212 - Accuracy: 48.63%
# Correct predictions: 4863/10000 (48.63%)

def predict_output(A, B, C, D, E):
    total = A + B + C + D + E
    if ((A < 20 and B > 70 and C < 40) or
        (C < 20 and D > 70 and A > 50) or
        (abs(A - B) < 20 and abs(C - D) < 20 and total < 200) or
        (C > 60 and B < 20) or
        (A > 80 and B > 70)):
        return 4
    elif ((D < 10 and C > 50 and E >= 50) or
          (B > 80 and C < 40)):
        return 2
    elif (A > 90 and E > 90):
        return 3
    else:
        return 1