"""
Predictor 661
Generated on: 2025-09-10 00:31:36
Accuracy: 51.39%
"""


# PREDICTOR 661 - Accuracy: 51.39%
# Correct predictions: 5139/10000 (51.39%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or \
       (C < 15 and D > 90) or \
       (A > 85 and B < 15 and D > 60 and E < 20) or \
       (B < 10 and C > 85 and E < 10) or \
       (B > 95 and E > 90) or \
       (A > 75 and D < 25 and E > 80) or \
       (C > 65 and D < 25 and E > 80):
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