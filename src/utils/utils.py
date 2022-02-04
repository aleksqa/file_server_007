import uuid


def random_string():
    return str(uuid.uuid4())
    # return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


