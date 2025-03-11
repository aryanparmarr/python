"""There is an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.

Without altering the relative order of positive and negative numbers, you must return an array of alternative positive and negative values."""


def alternate_positive_negative(A):
    # Separate positive and negative numbers
    positives = [x for x in A if x > 0]
    negatives = [x for x in A if x < 0]
    
    # Resultant array to store the alternated values
    result = []
    
    # Alternate the positive and negative numbers
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])
    
    return result
