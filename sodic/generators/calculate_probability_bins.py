from typing import List


def calculate_probability_bins(
    probability_weights: List[float],
) -> List[float]:
    """Calculates probability bins for a given list of probability weights.

    Example:
        probability_weights = [1, 1, 2]
        probability_bins = [0.25, 0.5, 1]
    Args:
        probability_weights: List of probability weights.
    Returns:
        Probability bins for given probability weights.
    """
    total_probability_weight = sum(probability_weights)
    current_probability_sum = 0.0
    probability_bins = []
    for probability_weight in probability_weights:
        current_probability_sum += probability_weight / total_probability_weight
        probability_bins.append(current_probability_sum)
    return probability_bins
