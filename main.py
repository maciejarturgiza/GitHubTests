
def add_numbers(a, b):
    """
    A simple function that adds two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    return a + b

def create_output_file():
    """
    Creates a simple output file with some content.
    
    Returns:
        str: Path of the created file
    """
    output_path = "output.txt"
    with open(output_path, 'w') as f:
        f.write("This file was created by the Python script.")
    return output_path
