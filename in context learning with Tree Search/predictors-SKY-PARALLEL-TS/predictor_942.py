"""
Predictor 942
Generated on: 2025-09-10 01:07:55
Accuracy: 54.27%
"""


# PREDICTOR 942 - Accuracy: 54.27%
# Correct predictions: 5427/10000 (54.27%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80 and B > 55) or
        (C > 80 and D < 25 and E < 15) or
        (A > 70 and B < 10 and D < 25) or
        (A < 15 and C > 80) or
        (C < 30 and E > 65 and B > 60)):
        return 4
    elif ((D < 5 and E > 80) or
          (A < 5 and D > 50 and E > 50) or
          (B > 80 and C > 80)):
        return 2
    elif ((C > 60 and D < 20 and E < 10) or
          (C > 90 and D > 90) or
          (B > 70 and D > 80) or
          (C > 50 and D < 20 and E < 5)):
        return 3
    else:
        return 1