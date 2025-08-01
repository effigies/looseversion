# Changelog

## Releases

### Upcoming (To be determined)

- 2025.07.31
  - Test on Python 3.14
  - Update license metadata, per PEP 639
- 2025.01.02
  - Test on Python 3.13, updating CI infrastructure.

### 1.3.0 (5 Jul 2023)

- 2023.07.05
  - Restore Python 3 semantics for `LooseVersion`, creating `LooseVersion2`
    to restore Python 2 semantics.

### 1.2.0 (25 May 2023)

- 2023.05.25
  - Test on Python 3.12
  - Enable installation on Python 2+
  - Ensure consistent semantics between Python 2 and 3

### 1.1.2 (22 Feb 2023)

- 2023.02.22
  - Revert unintended change in internal version representation

### 1.1.1 (19 Feb 2023)

- 2023.02.19
  - Restructure package so stubs get installed and detected

### 1.1.0 (19 Feb 2023)

- 2023.02.19
  - Add type annotations and stubs.

### 1.0.3 (5 Jan 2023)

Re-release to ensure tests are bundled in sdist.

- 2022.12.11
  - Convert to flit package

### 1.0.2 (14 Oct 2022)

- 2022.10.14
  - Fix package metadata to correctly identify module
- 2022.07.24
  - Test on Python 3.11
- 2022.05.24
  - Add `__main__` section to tests to enable `python tests.py`

### 1.0.1 (16 May 2022)

- 2022.05.16
  - Add tests.py in sdist
- 2022.05.11
  - Set up GitHub actions for build/test/upload

### 1.0.0 (11 May 2022)

- 2022.05.11
  - Import from CPython (last modified 662db125cddbca1db68116c547c290eb3943d98e)
  - Remove Version base class and StrictVersion
  - Style with black
  - Add non-importing check for distutils.version.LooseVersion to maintain
    compatibility
