"""
Predictor 65
Generated on: 2025-09-09 06:03:45
Accuracy: 49.57%
"""


# PREDICTOR 65 - Accuracy: 49.57%
# Correct predictions: 4957/10000 (49.57%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 30 and D >= 80 and C < 50 and E >= 20) or \
       (E < 15 and D >= 80) or \
       (E < 20 and D >= 60):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36 and C < 70) or \
         (B >= 80 and C <= 35 and D >= 60 and A >= 50) or \
         (B <= 20 and A >= 80 and E >= 60) or \
         (A >= 85 and B >= 65 and C <= 40) or \
         (B >= 40 and B <= 45 and D >= 30 and E >= 80) or \
         (E >= 90):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 85 and C >= 80 and A <= 20) or \
         (B >= 75 and A <= 10 and C <= 10):
        return 2
    
    # Default to class 1
    else:
        return 1