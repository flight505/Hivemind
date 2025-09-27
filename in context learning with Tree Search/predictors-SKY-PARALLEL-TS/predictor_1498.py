"""
Predictor 1498
Generated on: 2025-09-10 02:35:36
Accuracy: 55.67%
"""


# PREDICTOR 1498 - Accuracy: 55.67%
# Correct predictions: 5567/10000 (55.67%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 20 and D > 70) or
        (C < 10 and D > 90 and E > 80) or
        (A > 60 and B < 40 and C < 10 and E > 50) or
        (E < 5 and D > 70) or
        (E < 10 and C < 40 and A < 40)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (B > 70 and D > 60 and E < 20) or
          (D < 15 and E > 80) or
          (A < 40 and D < 25 and E > 50 and C > 40 and B > 40)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 45 and B < 80) or
          (C <= 10 and E < 60) or
          (A > 70 and B < 10 and D > 70)):
        return 3
    else:
        return 1