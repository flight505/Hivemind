"""
Predictor 7
Generated on: 2025-09-09 04:02:01
Accuracy: 46.41%
"""


# PREDICTOR 7 - Accuracy: 46.41%
# Correct predictions: 4641/10000 (46.41%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12) or (D >= 90 and E <= 80):
        return 3
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 80) or \
         (B >= 15 and B <= 20 and D >= 30 and D <= 35) or \
         (B >= 28 and B <= 36 and D >= 60) or \
         (B >= 40 and C >= 70 and D >= 20 and E <= 10) or \
         (B <= 10 and D >= 20 and D <= 30):
        return 4
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70):
        return 2
    # Default to class 1
    else:
        return 1