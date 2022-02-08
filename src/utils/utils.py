import uuid


def random_string() -> str:
    """
    Generate random string

    :return: generated string
    """
    return str(uuid.uuid4())
    # return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
