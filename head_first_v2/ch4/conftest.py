def pytest_configure(config):
    """Fix vsearch_pep8.py warning"""
    config.addinivalue_line(
        'markers', 'pep8: workaround for https://bitbucket.org/pytest-dev/pytest-pep8/issues/23/'
    )