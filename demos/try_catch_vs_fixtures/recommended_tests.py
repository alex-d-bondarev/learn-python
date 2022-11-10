import pytest

from demos.try_catch_vs_fixtures.test_environment_mock import (  # noqa
    ENV_OK, ENV_FAIL, TestEnvironment)


@pytest.fixture(scope='function')
def param1() -> bool:
    yield False


@pytest.fixture(scope='function')
def param2() -> str:
    yield '987'


@pytest.fixture(scope='function')
def account_fixture() -> TestEnvironment:
    env = ENV_OK
    # env = ENV_FAIL

    if not env.account:
        env.create_account()

    yield env

    env.delete_account()


@pytest.fixture(scope='function')
def sc_fixture(account_fixture: TestEnvironment) -> TestEnvironment:
    env = account_fixture
    # raise Exception('surprise')

    if not env.short_code:
        env.create_short_code()

    yield env

    env.delete_short_code()
    # raise Exception('surprise')


@pytest.fixture(scope='function')
def ip_fixture(sc_fixture: TestEnvironment) -> TestEnvironment:
    env = sc_fixture

    if not env.interested_party:
        env.create_interested_party()

    yield env

    env.delete_interested_party()


@pytest.fixture(scope="function")
def setup_fixture(ip_fixture, param1, param2) -> TestEnvironment:
    print(f'Fixture received params: '
          f'param1={param1}, '
          f'param2={param2}\n')

    yield ip_fixture


@pytest.mark.parametrize('param1', [False])
@pytest.mark.parametrize('param2', ["123"])
def test_recommended_example(setup_fixture: TestEnvironment):  # noqa
    """
    "Recommended" test
    1. Can handle broken env
    2. Can clean up if test fails
    3. Easy to read
    4. Easy to maintain
    5. Easy to pass parameters
    6. Easy to reuse fixtures
    7. Can handle clean up exceptions
    8. Does not handle set up exceptions !
    7. More fixtures !
    8. PyCharm does not parse parameters !
    """
    print('\n=== Start the test ===\n')

    print('\n!!! The test itself !!!\n')
    assert True

    print('\n=== End the test ===\n')
