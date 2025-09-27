"""
Predictor 21
Generated on: 2025-09-09 04:42:07
Accuracy: 56.95%
"""


# PREDICTOR 21 - Accuracy: 56.95%
# Correct predictions: 5695/10000 (56.95%)

def predict_output(A, B, C, D, E):
    # Class 3 conditions: low B, very low C and E
    if B <= 15 and C <= 12 and E < 40:
        return 3
    
    # Class 4 conditions: specific B and D range
    if B >= 28 and B <= 36 and D >= 15 and D <= 36:
        return 4
    
    # Class 2 conditions: either high B with moderate A/C or very high B and C
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80):
        return 2
    
    # Default to class 1 for all other cases
    return 1