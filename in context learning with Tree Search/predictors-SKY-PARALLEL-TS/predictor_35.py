"""
Predictor 35
Generated on: 2025-09-09 23:19:12
Accuracy: 51.91%
"""


# PREDICTOR 35 - Accuracy: 51.91%
# Correct predictions: 5191/10000 (51.91%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or \
       (A < 10 and E < 10) or \
       (B < 10 and C > 60) or \
       (C < 15 and D > 55) or \
       (D < 15 and C > 50):
        return 4
    elif (A > 90 and E < 10) or (C > 90 and D < 10):
        return 2
    elif (D < 10 and A > 40) or (E < 5 and B > 50 and D < 30) or (D > 75 and C < 45 and B > 20):
        return 3
    else:
        return 1