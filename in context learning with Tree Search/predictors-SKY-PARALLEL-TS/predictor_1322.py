"""
Predictor 1322
Generated on: 2025-09-10 02:07:02
Accuracy: 54.63%
"""


# PREDICTOR 1322 - Accuracy: 54.63%
# Correct predictions: 5463/10000 (54.63%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (C > 80 and D < 20 and E < 20) or
        (A > 80 and B < 10 and D < 5 and E > 70) or
        (A > 70 and E > 80 and D < 40) or
        (B < 10 and C > 70 and E > 70)):
        return 4
    elif ((B > 80 and C > 90) or
          (B > 95 and A < 20) or
          (E > 90 and A < 15 and B < 10) or
          (B > 70 and C > 80 and D > 60)):
        return 2
    elif ((A < 15 and B < 20 and C < 20 and D < 30 and E < 25) or
          (A > 90 and B < 5 and C < 10 and D < 5) or
          (D > 90 and E < 30 and A > 80) or
          (A > 80 and B > 70 and C > 45 and D > 90)):
        return 3
    else:
        return 1