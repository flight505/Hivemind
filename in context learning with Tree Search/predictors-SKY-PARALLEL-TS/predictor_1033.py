"""
Predictor 1033
Generated on: 2025-09-10 01:20:29
Accuracy: 56.31%
"""


# PREDICTOR 1033 - Accuracy: 56.31%
# Correct predictions: 5631/10000 (56.31%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or \
       (A > 70 and B < 5 and D > 60 and E < 5) or \
       (A < 35 and B < 20 and C > 50 and D > 60 and E < 15) or \
       (A > 40 and B > 65 and C < 10 and D > 80) or \
       (A < 10 and B > 50 and C > 40 and D < 30 and E < 40) or \
       (A < 45 and B < 25 and C > 80 and E < 20):
        return 4
    elif (A < 30 and B > 80 and C < 50 and D > 80 and E < 15):
        return 2
    elif (A < 5 and B > 55 and C < 10 and D < 30 and E > 30):
        return 3
    else:
        return 1