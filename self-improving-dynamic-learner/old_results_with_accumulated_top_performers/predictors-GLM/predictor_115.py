"""
Predictor 115
Generated on: 2025-09-09 07:43:58
Accuracy: 54.71%
"""


# PREDICTOR 115 - Accuracy: 54.71%
# Correct predictions: 5471/10000 (54.71%)

def predict_output(A, B, C, D, E):
    # Class 1 conditions: very high values or specific patterns
    if (A >= 90 and B >= 90 and C >= 90 and D >= 90) or \
       (A >= 30 and B >= 89 and D <= 5) or \
       (A <= 10 and B >= 89 and C >= 75 and D >= 60) or \
       (A >= 50 and B <= 10 and C >= 90 and E >= 40) or \
       (B <= 10 and C >= 80) or \
       (D >= 95 and E >= 90) or \
       (A >= 90 and C <= 20) or \
       (C >= 90) or \
       (E >= 95):
        return 1
    
    # Class 3 conditions: low B, low C, low E patterns
    if (B <= 15 and C <= 12 and E < 40) or \
       (B >= 55 and C <= 5 and E < 20) or \
       (B >= 60 and C >= 70 and D >= 60 and E < 20) or \
       (B >= 40 and B <= 60 and C >= 40 and C <= 50 and E >= 90) or \
       (C <= 10 and E < 50 and B <= 70) or \
       (E < 20 and B > 50 and C < 50 and D > 80) or \
       (E <= 5):
        return 3
    
    # Class 4 conditions: specific B and D ranges or very high E
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90) or \
       (B >= 80 and E >= 80) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 75 and C <= 10) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (A >= 90 and B >= 70 and C <= 25 and D >= 80) or \
       (B >= 95) or \
       (B <= 10 and C >= 70 and C <= 90) or \
       (B >= 80 and E >= 80 and C < 50) or \
       (B >= 55 and B <= 60 and C >= 60 and D >= 15 and D <= 25) or \
       (B <= 10 and C <= 5 and D >= 60 and E >= 60) or \
       (B <= 10 and D >= 40 and E < 10) or \
       (B >= 50 and C <= 20 and D >= 80 and E >= 60) or \
       (B >= 75 and C <= 10 and E >= 20) or \
       (C <= 10 and D >= 90) or \
       (A >= 90 and B <= 10 and E >= 60) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (E >= 90 and D < 80 and 
        not (B <= 20 and C >= 50) and 
        not (B >= 30 and C >= 70) and 
        not (B >= 50 and C >= 70)) or \
       (B >= 65 and C >= 45 and C <= 65 and E <= 10) or \
       (B >= 60 and B <= 70 and C >= 45 and D >= 25 and D <= 35):
        return 4
    
    # Class 2 conditions: high B with moderate A and high C, or very high B and C
    if (B >= 65 and A <= 50 and C >= 70 and A > 20) or \
       (B >= 90 and C >= 80) or \
       (B >= 85 and A >= 80 and C >= 40 and C <= 50 and E >= 70) or \
       (A >= 45 and B <= 10 and C >= 90 and D <= 10):
        return 2
    
    # Default to class 1
    return 1