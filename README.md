# learn-python
Learn python basics

## Build

### First time

1. Make sure [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed
2. Run `uv sync`

### Update dependencies

Run `uv sync`

### Update transitive dependencies

Run `uv lock --upgrade-package <transitive_package_name>`

## Change code

Run ruff from time to time from project root or from specific folder
```shell
ruff check
ruff format
```
