"""
Predictor 74
Generated on: 2025-09-09 06:15:49
Accuracy: 55.43%
"""


# PREDICTOR 74 - Accuracy: 55.43%
# Correct predictions: 5543/10000 (55.43%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 25 and C <= 35 and E < 30) or \
       (B <= 35 and E < 25 and D < 20) or \
       (B >= 80 and E < 20 and D < 10):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90 and B < 85 and C < 90) or \
         (B <= 15 and C >= 90 and D < 20) or \
         (B >= 75 and C <= 10) or \
         (B <= 10 and D >= 40 and E < 15):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 85 and C >= 30 and C <= 50) or \
         (B >= 80 and C >= 20 and D >= 70) or \
         (B <= 15 and C >= 90 and D <= 10):
        return 2
    
    # Default to class 1
    else:
        return 1