from passlib.hash import pbkdf2_sha256

class PasswordValidate:
    @classmethod
    def very(self, clave, hash):
        return pbkdf2_sha256.verify(clave, hash)
    
    @classmethod
    def hashed(self, clave):
        return pbkdf2_sha256.hash(clave)

        