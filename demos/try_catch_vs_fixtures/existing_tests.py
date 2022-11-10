import pytest

from demos.try_catch_vs_fixtures.test_environment_mock import (  # noqa
    ENV_OK, ENV_FAIL, TestEnvironment)


def test_example_1():
    """
    Basic test:
    1. Cannot handle broken env !
    2. Cannot clean up if test fails !
    """
    print('\n=== Start the test ===\n')
    env = ENV_OK
    # env = ENV_FAIL

    env.create_account()
    env.create_short_code()
    env.create_interested_party()

    print('\n!!! The test itself !!!\n')
    assert True

    env.delete_interested_party()
    env.delete_short_code()
    env.delete_account()

    print('\n=== End the test ===\n')


def test_example_2():
    """
    "Improved" test
    1. Can handle broken env
    2. Can clean up if test fails
    3. Hard to read and maintain !
    """
    print('\n=== Start the test ===\n')
    env = ENV_OK
    # env = ENV_FAIL

    try:
        clean_up_ip(env)
        clean_up_sh(env)
        clean_up_acc(env)

        env.create_account()
        env.create_short_code()
        env.create_interested_party()

        print('\n!!! The test itself !!!\n')
        assert True

    finally:
        env.delete_interested_party()
        env.delete_short_code()
        env.delete_account()

    print('\n=== End the test ===\n')


def clean_up_acc(env):
    try:
        env.delete_account()
    except Exception:
        pass


def clean_up_sh(env):
    try:
        env.delete_short_code()
    except Exception:
        pass


def clean_up_ip(env):
    try:
        env.delete_interested_party()
    except Exception:
        pass


@pytest.mark.parametrize('setup_fixture', [
    {"param1": False, "param2": "123"}
], indirect=True)
def test_example_3(setup_fixture: TestEnvironment):
    """
    "Improved 2.0" test
    1. Can handle broken env
    2. Can clean up if test fails
    3. "Easier" to read
    4. Hard to maintain !
    5. Hard to pass parameters !
    6. Hard to reuse a fixture
    7. Does not handle clean up exceptions !
    8. Does not handle set up exceptions !
    """
    print('\n=== Start the test ===\n')

    print('\n!!! The test itself !!!\n')
    assert True

    print('\n=== End the test ===\n')


@pytest.fixture(scope="function")
def setup_fixture(request) -> TestEnvironment:
    print(f'Fixture received params: '
          f'param1={request.param["param1"]}, '
          f'param2={request.param["param2"]}\n')
    env = ENV_OK
    # env = ENV_FAIL

    clean_up_ip(env)
    clean_up_sh(env)
    clean_up_acc(env)

    env.create_account()
    env.create_short_code()
    # raise Exception('surprise')
    env.create_interested_party()

    yield env

    env.delete_interested_party()
    env.delete_short_code()
    # raise Exception('surprise')
    env.delete_account()
