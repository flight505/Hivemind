"""
Predictor 98
Generated on: 2025-09-09 06:34:40
Accuracy: 54.73%
"""


# PREDICTOR 98 - Accuracy: 54.73%
# Correct predictions: 5473/10000 (54.73%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions: very high values or specific patterns
    if (A >= 90 and B >= 90 and C >= 90 and D >= 90) or \
       (B >= 90 and C >= 85 and D <= 30) or \
       (B >= 85 and C >= 80 and E >= 70) or \
       (B <= 15 and C >= 90 and D >= 70) or \
       (A <= 10 and B >= 95 and C <= 25 and D <= 20):
        return 1
    
    # Class 3 conditions: low B with low C, or specific patterns
    if (B <= 15 and C <= 12 and E < 40) or \
       (B <= 25 and C <= 20 and E <= 40) or \
       (B >= 35 and B <= 45 and C <= 20 and E >= 30) or \
       (B >= 80 and C <= 25 and E <= 30) or \
       (A <= 10 and C <= 20 and E <= 40) or \
       (B >= 40 and B <= 50 and C >= 40 and C <= 50 and E >= 90):
        return 3
    
    # Class 4 conditions: specific B and D ranges, or high E patterns
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and B < 50 and C < 70) or \
       (B <= 15 and D >= 80 and E >= 60) or \
       (B >= 75 and C <= 15) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 15 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (B >= 60 and C <= 20 and E >= 90) or \
       (C <= 15 and D >= 80 and E <= 20) or \
       (B >= 50 and B <= 60 and C <= 25 and D >= 45 and E >= 75):
        return 4
    
    # Class 2 conditions: high B with specific constraints
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and C >= 70 and D >= 60) or \
       (A <= 20 and B >= 90 and C >= 70) or \
       (B >= 65 and C < 50 and D >= 60 and A <= 40) or \
       (B >= 85 and C >= 30 and C <= 50) or \
       (B >= 80 and C >= 20 and D >= 70) or \
       (B >= 55 and B <= 60 and C >= 45 and C <= 60 and D >= 35 and D <= 55):
        return 2
    
    # Default to class 1
    return 1