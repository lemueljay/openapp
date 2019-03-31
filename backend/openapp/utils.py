import string
import random


class CodeGenerator:

    code = None

    def __init__(self):
        self.code = self.generator()

    def generator(self, size=10, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def getCode(self):
        return self.code
