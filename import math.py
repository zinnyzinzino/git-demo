def get_fractions(a_b: str, c_b: str) -> str:
    try:
        a_parts = a_b.split('/')
        if len(a_parts) != 2:
            raise ValueError(f"Invalid fraction format for '{a_b}'. Expected 'numerator/denominator'.")
        
        a_numerator = int(a_parts[0])
        a_denominator = int(a_parts[1])

        c_parts = c_b.split('/')
        if len(c_parts) != 2:
            raise ValueError(f"Invalid fraction format for '{c_b}'. Expected 'numerator/denominator'.")
        
        c_numerator = int(c_parts[0])
        c_denominator = int(c_parts[1])
        
        if a_denominator != c_denominator:
            return f"Error: Denominators do not match. Found {a_denominator} and {c_denominator}."
        
        if a_denominator == 0:
             return "Error: Cannot divide by zero (denominator is 0)."

        sum_numerator = a_numerator + c_numerator
        common_denominator = a_denominator
        
        sum_result = f"{sum_numerator}/{common_denominator}"
        
        result_string = f"{a_b} + {c_b} = {sum_result}"
        
        return result_string

    except ValueError as e:
        return f"Error: Invalid input. {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"