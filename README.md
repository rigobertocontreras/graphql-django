

To learn more check out the following [examples](examples/):


## Contributing


After cloning this repo, ensure dependencies are installed by running:

```sh
pip install -e ".[test]"
```

After developing, the full test suite can be evaluated by running:

```sh
py.test --cov-report html graphql_django --cov=graphql_django
```

