"""
Predictor 86
Generated on: 2025-09-09 06:25:31
Accuracy: 51.43%
"""


# PREDICTOR 86 - Accuracy: 51.43%
# Correct predictions: 5143/10000 (51.43%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low values
    if (B <= 15 and C < 50) or \
       (B <= 20 and E <= 25 and C <= 15) or \
       (E < 15 and B >= 80 and D <= 30) or \
       (B >= 75 and C >= 75 and D <= 20):
        return 3
    
    # Class 4 conditions: specific ranges and combinations
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
         (E >= 90 and not (A <= 15 and B <= 15 and C >= 75)) or \
         (C <= 10 and D >= 90 and B > 15) or \
         (B >= 80 and E >= 80 and C < 50) or \
         (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
         (B <= 10 and D >= 40 and E < 10) or \
         (A >= 90 and B <= 10 and E >= 60) or \
         (B >= 95 and C <= 20) or \
         (C <= 20 and B >= 85 and D >= 80) or \
         (B <= 35 and D >= 90 and E <= 25) or \
         (A >= 90 and B >= 50 and C >= 50 and E >= 70):
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