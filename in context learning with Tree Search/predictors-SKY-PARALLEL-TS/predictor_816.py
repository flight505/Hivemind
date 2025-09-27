"""
Predictor 816
Generated on: 2025-09-10 00:50:43
Accuracy: 47.06%
"""


# PREDICTOR 816 - Accuracy: 47.06%
# Correct predictions: 4706/10000 (47.06%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or \
       (C < 15 and D > 90) or \
       (D > 60 and B < 20) or \
       (C > 70 and D > 60 and E < 10) or \
       (A > 40 and C < 45 and E > 80 and D > 15):
        return 4
    elif C > 95 or (B < 10 and D > 80):
        return 3
    elif (B > 80 and E > 80 and C > 45) or \
         (B > 65 and C > 60 and D > 55 and E > 15) or \
         (A > 90 and E < 10):
        return 2
    else:
        return 1