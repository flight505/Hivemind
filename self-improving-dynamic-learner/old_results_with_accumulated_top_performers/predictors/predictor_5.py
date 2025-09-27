"""
Predictor 5
Generated on: 2025-09-09 03:03:33
Accuracy: 51.46%
"""


# PREDICTOR 5 - Accuracy: 51.46%
# Correct predictions: 5146/10000 (51.46%)

def predict_output(A, B, C, D, E):
    # Calculate key features
    sum_ABC = A + B + C
    sum_DE = D + E
    avg_all = (A + B + C + D + E) / 5
    diff_BD = B - D
    ratio_CE = C / (E + 1)
    
    # Primary decision tree
    if C > 60 or (B > 50 and sum_ABC > 120):
        return 1
    elif E > 80 and (D > 20 or C < 30):
        return 4
    elif D > 70 and E < 40:
        return 3
    elif B > 60 and C > 70:
        return 2
    else:
        # Secondary decision tree
        if avg_all > 60 and diff_BD > 0:
            return 1
        elif sum_DE > 150 and B < 40:
            return 4
        elif ratio_CE < 0.5 and A > 50:
            return 3
        elif sum_ABC < 100:
            return 2
        else:
            return 1