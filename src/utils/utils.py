import uuid


def random_string():
    return uuid.uuid4().hex
    # return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


