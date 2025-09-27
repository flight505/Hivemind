"""
Predictor 12
Generated on: 2025-09-09 03:03:55
Accuracy: 46.60%
"""


# PREDICTOR 12 - Accuracy: 46.60%
# Correct predictions: 4660/10000 (46.60%)

def predict_output(A, B, C, D, E):
    # Calculate key features using improved combinations
    sum_ABC = A + B + C
    sum_DE = D + E
    diff_AE = A - E
    diff_BD = B - D
    ratio_BD = B / (D + 1)
    avg_all = (A + B + C + D + E) / 5
    
    # Primary decision tree with refined conditions
    if C > 50 or (B > 60 and sum_ABC > 120):
        return 1
    elif E > 70 and (D > 50 or C < 25):
        return 4
    elif D > 80 and E < 35:
        return 3
    elif B > 65 and C > 70:
        return 2
    elif low_B and A > 70:
        return 4
    else:
        # Secondary decision tree with additional patterns
        if avg_all > 55 and diff_BD > 0:
            return 1
        elif sum_DE > 140 and C < 20:
            return 4
        elif diff_AE < -20 and D > 60:
            return 3
        elif sum_ABC > 150 and B > 50:
            return 2
        else:
            return 1