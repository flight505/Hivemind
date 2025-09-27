"""
Predictor 874
Generated on: 2025-09-10 00:58:03
Accuracy: 60.57%
"""


# PREDICTOR 874 - Accuracy: 60.57%
# Correct predictions: 6057/10000 (60.57%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70) or
        (D < 5 and E > 70) or
        (B < 20 and C > 60 and E < 10) or
        (C < 25 and D > 95) or
        (A > 50 and B < 30 and D < 5 and E > 75)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 85 and C > 80) or
          (B > 90 and C > 95)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B > 60 and A < 70 and E < 50) or
          (C <= 10 and E < 60)):
        return 3
    else:
        return 1