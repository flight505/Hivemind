"""
Predictor 137
Generated on: 2025-09-09 04:18:41
Accuracy: 36.38%
"""


# PREDICTOR 137 - Accuracy: 36.38%
# Correct predictions: 3638/10000 (36.38%)

def predict_output(A, B, C, D, E):
    # Primary decision tree based on key thresholds from successful patterns
    if C > 60:
        if B > 70:
            return 1
        else:
            return 2
    elif E > 80:
        return 4
    elif B < 25 and C < 25:
        return 3
    else:
        # Secondary decision tree with refined arithmetic combinations
        total_sum = A + B + C + D + E
        ab_sum = A + B
        cd_sum = C + D
        be_sum = B + E
        ad_diff = A - D
        bc_diff = B - C
        ce_ratio = C / (E + 1)
        
        # Use new combinations to break stagnation
        if total_sum > 300 and bc_diff > 20:
            return 1
        elif ad_diff < -10 and ce_ratio < 0.5:
            return 4
        elif ab_sum < 50 and cd_sum > 80:
            return 3
        elif be_sum > 120 and C < 25:
            return 2
        else:
            return 1