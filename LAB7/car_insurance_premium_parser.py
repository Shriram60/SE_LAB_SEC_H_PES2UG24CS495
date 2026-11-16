def normalize_registration(plate):
    """
    Removes spaces and dashes from a registration number and upper-cases it.
    Fixed: any non-string input (e.g. None) returns an empty string instead of
    crashing, and every kind of whitespace (tabs, newlines, unicode spaces) is
    removed, not just the plain space.
    """
    if not isinstance(plate, str):
        return ""
    plate = plate.upper()
    plate = "".join(ch for ch in plate if not ch.isspace())
    for ch in ['-', '.']:
        plate = plate.replace(ch, '')
    return plate

def total_claim_amount(text):
    """
    Adds up claim amounts separated by semicolons.
    Fixed: non-string input returns 0, blank parts (e.g. "100;;200" or a
    trailing ";") are skipped, and anything that is not a whole number
    >= 0 (letters, decimals, negatives, absurdly long digit strings) is
    ignored instead of raising an exception.
    """
    if not isinstance(text, str):
        return 0
    total = 0
    for part in text.split(';'):
        part = part.strip()
        if not part:
            continue
        try:
            amount = int(part)
        except ValueError:
            continue
        if amount < 0:
            continue
        total += amount
    return total

def driver_age(dob, current_year=2026):
    """
    Works out the driver's age from a DD/MM/YYYY date of birth.
    Fixed: returns None for anything that is not a valid DD/MM/YYYY date
    (None, missing parts, non-numeric parts, impossible day/month, or a
    year in the future / before 1900) instead of crashing or returning a
    nonsense age.
    """
    if not isinstance(dob, str):
        return None
    parts = dob.strip().split('/')
    if len(parts) != 3:
        return None
    try:
        day, month, year = (int(p) for p in parts)
    except ValueError:
        return None
    if not (1 <= day <= 31 and 1 <= month <= 12):
        return None
    if not (1900 <= year <= current_year):
        return None
    return current_year - year

def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    result = normalize_registration(value)
    print("Normalized registration:", result if result else "(invalid / empty registration)")

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    age = driver_age(value)
    print("Driver age in 2026:", age if age is not None else "invalid date of birth")

if __name__ == "__main__":
    main()
