# loop-integration-fixture

A **disposable** Python fixture for the
[software-factory-loop](https://github.com/manjula25/software-factory-loop)
integration test.

Not a real library, and **not** the practice fixture (`loop-fixtures-py`):
this repository exists to be reset, rewritten and merged into by an automated
test, and its history is expendable.

The seed carries one latent defect that the contract suite does not cover,
with an open issue describing the symptom.

## Install and test

```bash
pip install -e ".[test]"
pytest
```

Fully offline: no network, no services.
