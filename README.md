# pyFolia

pyFolia is a deterministic garden planning engine for small vegetable beds. It
uses local plant fixture data, USDA-style climate-zone filtering, a hex-grid
bed model, spacing validation, and a simple greedy optimiser.

The project no longer depends on live scraping, geocoding, or Python 2 runtime
behaviour.

## Install

```sh
uv pip install -e .
```

## CLI

Create a JSON plan:

```sh
pyfolia plan --bed-width-cm 120 --bed-length-cm 240 --zone 8a --plants carrot,tomato,basil,lettuce
```

Create a printable SVG plan:

```sh
pyfolia plan --bed-width-cm 120 --bed-length-cm 240 --zone 8a --plants carrot,tomato,basil,lettuce --output svg > plan.svg
```

## Development

Run the core checks:

```sh
uv run ruff check src tests
uv run flake8 src tests
uv run mypy src/pyfolia
uv run pytest
```
