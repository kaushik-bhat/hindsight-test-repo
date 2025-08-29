# hindsight-test-repo/utils.py

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    
    This function contains a bug: it will crash if the input list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
        
    return sum(numbers) / len(numbers)
#hi
