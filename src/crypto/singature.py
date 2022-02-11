import hashlib


class SignatureFactory(type):
    signers = {}

    def __new__(cls, classname, superclasses, attributedict):
        if "__call__" not in attributedict:
            raise Exception(f"Signer class must implement {classname}.__call__ function")
        signer_class = type(classname, superclasses, attributedict)
        if "label" not in attributedict:
            signer_class.label = classname.lower()
        SignatureFactory.signers[signer_class.label] = signer_class()
        return signer_class

    @staticmethod
    def get_signer(label):
        return SignatureFactory.signers[label]


class Md5Signer(metaclass=SignatureFactory):
    label = "md5"

    def __call__(self, data):
        return hashlib.md5(data.encode()).hexdigest()


class Sha512Signer(metaclass=SignatureFactory):
    label = 'sha512'

    def __call__(self, data):
        return hashlib.sha512(data.encode()).hexdigest()


if __name__ == "__main__":
    print("test sign")
    data = "test"
    encoded_data = hashlib.md5(data.encode()).hexdigest()
    print(encoded_data)
    print(f"Md5Signer.label = {Md5Signer.label}")
    print(f"Sha512Signer.label = {Sha512Signer.label}")
