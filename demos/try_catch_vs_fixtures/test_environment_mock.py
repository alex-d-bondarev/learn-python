class TestEnvironment:
    def __init__(self):
        self.account: bool = False
        self.account_name: str = 'an Account'

        self.short_code: bool = False
        self.short_code_name: str = 'a Short Code'

        self.interested_party: bool = False
        self.interested_party_name: str = 'an IP'

    def create_account(self):
        self.account = _create_something(self.account, self.account_name)

    def delete_account(self):
        self.account = _delete_something(self.account, self.account_name)

    def create_short_code(self):
        if self.account:
            self.short_code = _create_something(self.short_code, self.short_code_name)
        else:
            raise Exception(f'Impossible to create {self.short_code_name} without {self.account_name}')

    def delete_short_code(self):
        self.short_code = _delete_something(self.short_code, self.short_code_name)

    def create_interested_party(self):
        if self.short_code_name:
            self.interested_party = _create_something(self.interested_party, self.interested_party_name)
        else:
            raise Exception(f'Impossible to create {self.interested_party_name} without {self.short_code_name}')

    def delete_interested_party(self):
        self.interested_party = _delete_something(self.interested_party, self.interested_party_name)


def _create_something(something: bool, name: str) -> bool:
    if not something:
        print(f'Successfully created {name}')
        return True

    raise Exception(f'Failed to create {name}. It already existed.')


def _delete_something(something: bool, name: str) -> bool:
    if something:
        print(f'Successfully deleted {name}')
        return False

    raise Exception(f'Failed to delete {name}. It did not exist.')


ENV_OK = TestEnvironment()
ENV_FAIL = TestEnvironment()
ENV_FAIL.account = True
ENV_FAIL.short_code = True


if __name__ == '__main__':
    print('\n=== Flow is OK ===')
    ENV_OK.create_account()
    ENV_OK.create_short_code()
    ENV_OK.create_interested_party()
    ENV_OK.delete_interested_party()
    ENV_OK.delete_short_code()
    ENV_OK.delete_account()

    print('\n=== Flow is broken ===')
    ENV_FAIL.create_account()
    ENV_FAIL.create_short_code()
    ENV_FAIL.create_interested_party()
    ENV_FAIL.delete_interested_party()
    ENV_FAIL.delete_short_code()
    ENV_FAIL.delete_account()
