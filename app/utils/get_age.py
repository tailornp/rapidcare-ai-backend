from datetime import date

def get_age(date_of_birth: date) -> int:
    """
    Calculate age based on date of birth and current date.
    
    Args:
        date_of_birth: The date of birth as a datetime.date object
        
    Returns:
        Age in years as an integer
    """
    today = date.today()
    age = today.year - date_of_birth.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    
    return age