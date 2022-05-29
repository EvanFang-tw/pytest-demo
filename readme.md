# Unit Test with Pytest

A really simple demo of how to use pytest.

Run unit test:
```sh
pytest
```

List markers:
```sh
pytest --markers
```

Markers are defined in `pytest.ini`.

Enable `--strict-markers` to reject any undefined marker.

Note that `@pytest.mark.skip` is a build in marker.

```ini
[pytest]
addopts = --strict-markers
markers =
    ignore: do not run this test
```

Run with marker:
```sh
# skip ignore tests
pytest -m "not ignore"

# run ignore tests only
pytest -m "ignore"
```

Generate html report with `pytest-html`:

```sh
pytest --html=reports/report.html
open reports/report.html
```