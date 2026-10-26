
def check_status(heart_rate, temp_c, motion, sound):
    """Demonstration logic for the LifeBeacon prototype."""

    if heart_rate is None or temp_c is None:
        return "SENSOR CHECK REQUIRED"

    if heart_rate < 45 or temp_c < 35:
        return "CHECK REQUIRED"

    if heart_rate < 50 and motion == 0 and sound == 0:
        return "POSSIBLE SOS"

    return "NORMAL"


if __name__ == "__main__":
    # Sample values for demonstration only
    result = check_status(
        heart_rate=48,
        temp_c=36.5,
        motion=0,
        sound=0
    )
    print("LifeBeacon Status:", result)
  
