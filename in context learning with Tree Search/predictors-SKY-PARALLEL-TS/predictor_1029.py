"""
Predictor 1029
Generated on: 2025-09-10 01:20:29
Accuracy: 51.33%
"""


# PREDICTOR 1029 - Accuracy: 51.33%
# Correct predictions: 5133/10000 (51.33%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and D > 80 and B > 50) or \
       (A > 80 and B > 70 and E > 70) or \
       (E < 5 and D > 50 and C < 40):
        return 4
    elif (B > 90) or \
         (A < 10 and E > 70 and D < 20):
        return 2
    elif (A > 60 and B < 30 and C < 20 and D > 70) or \
         (C > 70 and D < 20) or \
         (A < 40 and B > 70 and C > 70 and D > 80) or \
         (E > 90 and A > 50):
        return 3
    else:
        return 1