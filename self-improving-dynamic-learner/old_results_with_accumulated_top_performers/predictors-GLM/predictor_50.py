"""
Predictor 50
Generated on: 2025-09-09 05:44:37
Accuracy: 56.28%
"""


# PREDICTOR 50 - Accuracy: 56.28%
# Correct predictions: 5628/10000 (56.28%)

def predict_output(A, B, C, D, E):
    # Special case: very high values
    if A >= 90 and B >= 90 and C >= 80 and D >= 80:
        return 1
    
    # Class 3 conditions: low E with specific patterns
    if (E <= 16 and B >= 35 and B <= 40 and C >= 30 and C <= 40) or \
       (E <= 16 and D >= 45 and D <= 60 and C >= 35 and C <= 40) or \
       (B <= 15 and C <= 12 and E < 40) or \
       (E < 20 and B >= 60 and C < 50) or \
       (B <= 20 and E < 20 and C < 50 and not (D >= 90)) or \
       (A <= 10 and B >= 60 and C >= 75 and D <= 10 and E < 50) or \
       (A <= 20 and B >= 40 and B <= 50 and C >= 60 and D <= 10) or \
       (E < 30 and B <= 25 and C <= 10 and D >= 60) or \
       (B <= 20 and C >= 70 and D <= 10 and E < 30) or \
       (B >= 80 and C >= 90 and D >= 80 and E <= 40) or \
       (C >= 80 and B >= 50 and D >= 60 and E >= 60) or \
       (B >= 20 and B <= 25 and C >= 10 and C <= 20 and D >= 25 and E <= 25):
        return 3
    
    # Class 2 conditions: high B with specific constraints
    if (B >= 65 and A <= 50 and C >= 70 and A > 20 and D <= 10) or \
       (B >= 90 and C >= 80 and D >= 40 and E >= 40) or \
       (B >= 95 and D >= 90 and E >= 80) or \
       (C >= 90 and D <= 10) or \
       (A <= 10 and B >= 90 and C >= 70 and D <= 5) or \
       (A <= 15 and B >= 50 and B <= 60 and C <= 20 and E >= 70) or \
       (A <= 20 and B >= 95 and C >= 30 and C <= 40 and D >= 60 and E >= 50) or \
       (A <= 10 and B >= 85 and C <= 15 and D <= 20) or \
       (B >= 85 and C >= 70 and D >= 50 and E >= 50):
        return 2
    
    # Class 4 conditions: specific patterns with moderate B and D ranges
    if (B >= 28 and B <= 36 and D >= 15 and D <= 36) or \
       (E >= 90 and B < 50 and C <= 60) or \
       (E >= 90 and B >= 50 and C <= 50 and D <= 40) or \
       (B <= 20 and D >= 50 and E <= 25) or \
       (C <= 10 and D >= 90) or \
       (B >= 75 and C <= 10) or \
       (A >= 50 and B >= 55 and C <= 25 and E >= 90) or \
       (A <= 10 and B >= 90 and D <= 5) or \
       (C <= 20 and D >= 30 and E >= 90) or \
       (C <= 15 and B >= 60 and D >= 50) or \
       (A >= 95 and B >= 60 and C <= 20 and D >= 70 and E >= 65) or \
       (A >= 90 and C >= 60 and E >= 90) or \
       (B <= 10 and C <= 10 and D >= 60) or \
       (B >= 25 and B <= 35 and C >= 15 and C <= 25 and D >= 80 and E >= 15) or \
       (A >= 60 and B <= 10 and C >= 40 and D <= 5 and E >= 70) or \
       (A >= 70 and B >= 25 and B <= 35 and C >= 15 and C <= 25 and E >= 10) or \
       (B >= 95 and C >= 30 and C <= 40 and D >= 60) or \
       (A >= 40 and B >= 15 and B <= 25 and C >= 20 and C <= 30 and D >= 60 and E <= 20) or \
       (C <= 15 and B >= 60 and D >= 50 and E >= 30):
        return 4
    
    # Default to class 1
    return 1