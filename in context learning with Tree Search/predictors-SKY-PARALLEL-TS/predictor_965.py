"""
Predictor 965
Generated on: 2025-09-10 01:09:35
Accuracy: 54.04%
"""


# PREDICTOR 965 - Accuracy: 54.04%
# Correct predictions: 5404/10000 (54.04%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or \
       (C < 15 and D > 90 and E > 80) or \
       (B > 90 and C < 20 and D > 90) or \
       (A < 25 and B < 35 and C > 60 and E < 10) or \
       (C > 60 and E < 10 and B < 40):
        return 4
    elif (A < 15 and E > 90 and D < 15) or \
         (B > 95 and A > 50) or \
         (B > 85 and C > 80):
        return 2
    elif (A > 60 and C < 5 and D < 20) or \
         (B < 10 and D > 80 and E > 50):
        return 3
    else:
        return 1