"""
Predictor 815
Generated on: 2025-09-10 00:50:43
Accuracy: 58.06%
"""


# PREDICTOR 815 - Accuracy: 58.06%
# Correct predictions: 5806/10000 (58.06%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 60) or
        (B > 80 and E > 80) or
        (A < 30 and B > 50 and C > 50 and D < 40) or
        (A < 40 and B > 50 and C > 40 and E < 10)):
        return 4
    elif ((B > 75 and C > 35 and A < 50) or
          (A > 90 and E < 10)):
        return 2
    elif (B < 10 and E < 10):
        return 3
    else:
        return 1