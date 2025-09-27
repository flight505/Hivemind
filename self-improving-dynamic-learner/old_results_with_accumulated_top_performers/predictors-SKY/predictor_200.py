"""
Predictor 200
Generated on: 2025-09-09 08:07:17
Accuracy: 30.59%
"""


# PREDICTOR 200 - Accuracy: 30.59%
# Correct predictions: 3059/10000 (30.59%)

def predict_output(A, B, C, D, E):
    vals = [A, B, C, D, E]
    max_val = max(vals)
    max_idx = vals.index(max_val)
    if max_idx == 4:  # E
        return 4
    elif max_idx == 2:  # C
        return 2
    elif max_idx == 0:  # A
        return 3
    elif max_idx == 3:  # D
        if B < 20:
            return 3
        else:
            return 1
    else:  # B
        if C > 70:
            return 2
        else:
            return 1