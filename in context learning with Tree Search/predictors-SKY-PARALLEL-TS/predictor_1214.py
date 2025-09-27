"""
Predictor 1214
Generated on: 2025-09-10 01:46:44
Accuracy: 49.01%
"""


# PREDICTOR 1214 - Accuracy: 49.01%
# Correct predictions: 4901/10000 (49.01%)

def predict_output(A, B, C, D, E):
    total = A + B + C + D + E
    if ((A < 20 and B > 70 and C < 40) or
        (C < 20 and D > 70 and A > 50) or
        (abs(A - B) < 20 and abs(C - D) < 20 and total < 200) or
        (C > 60 and B < 20) or
        (A > 80 and B > 70 and D < 50)):
        return 4
    elif ((D < 10 and C > 50 and E >= 50) or
          (B > 80 and C < 40) or
          (A > 80 and B > 70 and D > 60)):
        return 2
    elif (A > 90 and E > 90):
        return 3
    else:
        return 1