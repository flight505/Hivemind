"""
Predictor 103
Generated on: 2025-09-09 07:01:28
Accuracy: 54.25%
"""


# PREDICTOR 103 - Accuracy: 54.25%
# Correct predictions: 5425/10000 (54.25%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: expanded to cover more low C and E patterns
    if (B <= 15 and C <= 12 and E < 40) or (C <= 10 and E < 40) or (E <= 30 and C < 50 and B >= 60):
        return 3
    
    # Class 4 conditions: expanded to cover patterns from errors
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90 and D < 80) or \
         (C <= 10 and D >= 90) or (B <= 20 and D <= 25 and E <= 70) or \
         (B >= 40 and B <= 50 and D <= 25 and E >= 50) or (D <= 10 and E >= 80) or \
         (B <= 10 and E >= 80):
        return 4
    
    # Class 2 conditions: added condition for very low A with high B and low C
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80) or \
         (A <= 10 and B >= 85 and C <= 15):
        return 2
    
    # Default to class 1
    else:
        return 1