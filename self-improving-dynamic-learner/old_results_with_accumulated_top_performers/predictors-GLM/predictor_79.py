"""
Predictor 79
Generated on: 2025-09-09 06:17:47
Accuracy: 39.34%
"""


# PREDICTOR 79 - Accuracy: 39.34%
# Correct predictions: 3934/10000 (39.34%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 25 and C <= 35 and E < 30) or \
       (B <= 35 and E < 25 and D < 20) or \
       (B >= 80 and E < 20 and D < 10) or \
       (A >= 50 and B >= 20 and C <= 25 and E >= 30):
        return 3
    
    # Class 4 conditions
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (B <= 10 and D >= 40 and E < 15) or \
         (B >= 70 and B <= 80 and C >= 40 and D >= 80) or \
         (B >= 80 and C >= 40 and D >= 80) or \
         (A >= 85 and B >= 95 and D >= 50) or \
         (A >= 40 and B >= 70 and C >= 80 and D >= 80):
        return 4
    
    # Class 2 conditions
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 85 and C >= 30 and C <= 50) or \
         (B >= 80 and C >= 20 and D >= 70) or \
         (B <= 15 and C >= 90 and D <= 10) or \
         (A <= 20 and B >= 40 and C >= 50) or \
         (A >= 30 and B >= 45 and C >= 45) or \
         (A <= 10 and B >= 75 and E >= 85):
        return 2
    
    # Default to class 1
    else:
        return 1