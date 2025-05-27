class PasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords

    def set_password(self, password):
        if password in self.old_passwords:
            return self.old_passwords
        else:
            self.old_passwords.append(password)
        return self.old_passwords

    def is_correct(self, password):
        if self.old_passwords[-1] == password:
            return True
        else:
            return False
