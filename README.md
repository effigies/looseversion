# looseversion - Version numbering for anarchists and software realists

A backwards/forwards-compatible fork of `distutils.version.LooseVersion`,
for times when PEP-440 isn't what you need.

The goal of this package is to be a drop-in replacement for the original `LooseVersion`.
It implements an identical interface and comparison logic to `LooseVersion`.
The only major change is that a `looseversion.LooseVersion` is comparable to a
`distutils.version.LooseVersion`, which means tools should not need to worry whether
all dependencies that use LooseVersion have migrated.

If you are simply comparing versions of Python packages, consider moving to
[packaging.version.Version](https://packaging.pypa.io/en/latest/version.html#packaging.version.Version),
which follows [PEP-440](https://peps.python.org/pep-0440).
`LooseVersion` is better suited to interacting with heterogeneous version schemes that
do not follow PEP-440.

## Installation

### From PyPI

```
pip install looseversion
```

### From source

```
git clone https://github.com/effigies/looseversion.git
pip install looseversion/
```

## Usage

```Python
>>> from looseversion import LooseVersion
>>> LooseVersion("1.0.0") < LooseVersion("2.0.0")
True
>>> LooseVersion("1.0.0") < "2"
True
```
