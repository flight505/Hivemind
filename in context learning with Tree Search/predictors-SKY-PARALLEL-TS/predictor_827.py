"""
Predictor 827
Generated on: 2025-09-10 00:53:24
Accuracy: 57.93%
"""


# PREDICTOR 827 - Accuracy: 57.93%
# Correct predictions: 5793/10000 (57.93%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 15 and D > 55 and A > 30) or
        (C < 25 and E > 70 and B < 65) or
        (D < 5 and A > 50 and E > 70) or
        (C > 90 and D > 50 and E < 15 and B < 40)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 85 and C > 80) or
          (A < 10 and B > 90) or
          (D < 5 and E > 70 and B < 20) or
          (A - C > 10 and E > 75 and B > 50) or
          (A < 5 and C < 12 and E > 50) or
          (B > 70 and C > 90 and E < 5) or
          (A < 10 and E > 90) or
          (B > 95) or
          (E > 90 and D < 25)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80) or
          (C < 10 and E < 60) or
          (A > 50 and C < 15 and E < 20) or
          (A < 20 and C < 20 and D > 40) or
          (C < 10 and D > 60) or
          (C > 80 and B < 10 and D < 15)):
        return 3
    else:
        return 1