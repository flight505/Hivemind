"""
Predictor 105
Generated on: 2025-09-09 07:03:13
Accuracy: 50.60%
"""


# PREDICTOR 105 - Accuracy: 50.60%
# Correct predictions: 5060/10000 (50.60%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: expanded patterns for low values and specific combinations
    if (B <= 15 and C <= 12 and E < 40) or (C <= 10 and E <= 30) or \
       (E <= 20 and B >= 60 and C < 50) or (B <= 20 and E <= 15) or \
       (B >= 30 and B <= 40 and C >= 35 and C <= 45 and E <= 40):
        return 3
    
    # Class 4 conditions: expanded patterns for moderate B/D, high E, and low C
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90) or \
         (B <= 20 and D >= 60 and E >= 60) or (B >= 80 and C <= 40) or \
         (C <= 10 and D >= 60) or (A >= 90 and B <= 10) or (D <= 10 and E >= 80) or \
         (B >= 40 and C <= 10 and D >= 70):
        return 4
    
    # Class 2 conditions: expanded patterns for high B with specific constraints
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80) or \
         (A <= 10 and B >= 80) or (B >= 80 and D <= 10) or (B >= 85 and C <= 40) or \
         (B >= 70 and C >= 90 and D >= 90):
        return 2
    
    # Default to class 1
    else:
        return 1