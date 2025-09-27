"""
Predictor 660
Generated on: 2025-09-10 00:31:36
Accuracy: 51.59%
"""


# PREDICTOR 660 - Accuracy: 51.59%
# Correct predictions: 5159/10000 (51.59%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or \
       (C < 15 and D > 90) or \
       (A > 85 and B < 15 and E < 15) or \
       (C > 85 and E < 10) or \
       (B > 95 and E > 90) or \
       (A > 75 and D < 25 and E > 80):
        return 4
    elif (B + E > 160) or \
         (B < 25 and C > 70 and E > 90) or \
         (B > 50 and E < 10 and C > 40) or \
         (A < 15 and B > 85):
        return 2
    elif D > 60 and E < 20:
        return 3
    else:
        return 1