"""
Predictor 85
Generated on: 2025-09-09 06:25:08
Accuracy: 55.55%
"""


# PREDICTOR 85 - Accuracy: 55.55%
# Correct predictions: 5555/10000 (55.55%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B, low C, low E
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 10 and C <= 30 and E <= 25) or \
       (E <= 10 and B >= 60 and C < 50 and D <= 40) or \
       (E <= 20 and B <= 25 and C <= 10):
        return 3
    
    # Class 4 conditions: specific ranges and combinations
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90 and not (C >= 70 and B >= 80) and not (C >= 90)) or \
         (C <= 10 and D >= 90 and B > 15) or \
         (B >= 80 and E >= 80 and C < 50) or \
         (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
         (B <= 10 and D >= 40 and E < 10) or \
         (A >= 90 and B <= 10 and E >= 60) or \
         (B >= 95 and C <= 20) or \
         (C <= 20 and B >= 85 and D >= 80) or \
         (B <= 35 and D >= 90 and E <= 25):
        return 4
    
    # Class 2 conditions: high B with specific constraints
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
         (B >= 90 and C >= 80) or \
         (B >= 85 and C >= 70 and D >= 60) or \
         (A <= 20 and B >= 90 and C >= 70):
        return 2
    
    # Default to class 1
    else:
        return 1