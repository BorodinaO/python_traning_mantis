import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Project(name=random_string("name", 10), status=random_string("1", 20),
                     description=random_string("description", 20))]
