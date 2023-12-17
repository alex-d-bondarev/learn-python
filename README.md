# learn-python
Learn python basics

## Build
### First time
1. Make sure that ```python3 --version``` is `3.10.*`.
2. Run ```poetry env use `python --version | grep -Eo '[0-9]+([.][0-9]+)+([.][0-9]+)?'` && poetry install```

### Update dependencies
Run ```poetry update```

### Find virtual env
RUn ```poetry show -v | grep "Using virtualenv"```
