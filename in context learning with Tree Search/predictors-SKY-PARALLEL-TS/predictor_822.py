"""
Predictor 822
Generated on: 2025-09-10 00:50:44
Accuracy: 52.88%
"""


# PREDICTOR 822 - Accuracy: 52.88%
# Correct predictions: 5288/10000 (52.88%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A < 15 and C > 65 and D < 35) or
        (A > 80 and D < 25 and E > 80) or
        (A < 15 and C > 90) or
        (A > 90 and C < 5 and D > 80)):
        return 4
    elif ((A > 90 and E < 10) or
          (C > 70 and D < 10)):
        return 2
    elif ((B < 10 and D > 80) or
          (D > 90 and (A > 70 or B > 70))):
        return 3
    else:
        return 1