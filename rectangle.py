def area_of_rectangle(width:int|float, height:int|float) -> int|float:
    """Find the area of a rectangle. 

    Given the width and height of a rectangle, calculate the rectangle's area through multiplication. 

    Args: 
	width: The width of the rectangle. Integer or float.
	height: The height of the rectangle. Integer or float.
    Returns: 
	The rectangle's area. An integer or float. 

"""
    return width * height


def perimeter_of_rectangle(width:int|float, height:int|float) -> int|float:
    """Find the perimeter of a rectangle. 

    Given the width and height of a rectangle, calculate the rectangle's perimeter as twice the sum of the width and the height.

    Args: 
	width: The width of the rectangle. Integer or float. 
	height: The height of the rectangle. Integer or float.
    Returns: 
	The rectangle's perimeter. Integer or float.
"""

    return 2 * (width + height)
