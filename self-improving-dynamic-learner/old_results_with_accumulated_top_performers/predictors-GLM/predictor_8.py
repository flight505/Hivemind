"""
Predictor 8
Generated on: 2025-09-09 04:05:19
Accuracy: 53.91%
"""


# PREDICTOR 8 - Accuracy: 53.91%
# Correct predictions: 5391/10000 (53.91%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C < 50) or (B >= 45 and B <= 50 and C >= 40 and C <= 45 and E <= 30) or (C <= 10):
        return 3
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (B >= 15 and B <= 20 and D >= 30 and D <= 35) or \
         (B >= 40 and C >= 70 and D >= 20 and E <= 10) or \
         (B >= 60 and B <= 70 and E >= 75) or \
         (B >= 75 and C <= 10):
        return 4
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 80 and C >= 40 and A > 50 and C <= 45) or \
         (B >= 90 and C >= 45 and C <= 60):
        return 2
    # Default to class 1
    else:
        return 1