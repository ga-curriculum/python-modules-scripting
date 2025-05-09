"""
My Utilities Module

This module contains utility functions for common tasks.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9

def format_name(first_name, last_name):
    """
    Format a name in 'Last, First' format.
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    
    Returns:
        str: Formatted name
    """
    return f"{last_name.title()}, {first_name.title()}"

# Constants
PI = 3.14159265359
GOLDEN_RATIO = 1.61803398875

# Version information
__version__ = "0.1.0"
