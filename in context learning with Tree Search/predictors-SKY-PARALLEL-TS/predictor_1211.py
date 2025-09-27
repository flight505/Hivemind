"""
Predictor 1211
Generated on: 2025-09-10 01:46:44
Accuracy: 54.84%
"""


# PREDICTOR 1211 - Accuracy: 54.84%
# Correct predictions: 5484/10000 (54.84%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (E < 5 and D > 50) or
        (B < 10 and A > 60 and C < 40 and E > 70) or
        (B > 60 and E > 70) or
        (A < 30 and C > 75 and D < 30) or
        (A < 5 and B > 65 and E < 20)):
        return 4
    elif ((B > 85 and D > 80) or
          (B < 40 and E > 50 and C < 30)):
        return 2
    elif ((A + B + C + D + E < 120) or
          (B < 15 and E < 20)):
        return 3
    else:
        return 1