import sys
import warnings

import pytest

import looseversion as lv

have_distutils = True
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from distutils import version as dv
    except ImportError:
        have_distutils = False


@pytest.mark.skipif(not have_distutils, reason="Needs distutils")
@pytest.mark.parametrize("v1, v2", [("0.0.0", "0.0.0"), ("0.0.0", "1.0.0")])
def test_LooseVersion_compat(v1, v2):
    vend1, vend2 = lv.LooseVersion(v1), lv.LooseVersion(v2)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        orig1, orig2 = dv.LooseVersion(v1), dv.LooseVersion(v2)

    assert vend1 == orig1
    assert orig1 == vend1
    assert vend2 == orig2
    assert orig2 == vend2
    assert (vend1 == orig2) == (v1 == v2)
    assert (vend1 < orig2) == (v1 < v2)
    assert (vend1 > orig2) == (v1 > v2)
    assert (vend1 <= orig2) == (v1 <= v2)
    assert (vend1 >= orig2) == (v1 >= v2)
    assert (orig1 == vend2) == (v1 == v2)
    assert (orig1 < vend2) == (v1 < v2)
    assert (orig1 > vend2) == (v1 > v2)
    assert (orig1 <= vend2) == (v1 <= v2)
    assert (orig1 >= vend2) == (v1 >= v2)


# Adapted from Cpython:Lib/distutils/tests/test_version.py
@pytest.mark.parametrize(
    "v1,v2,result",
    [
        ("1.5.1", "1.5.2b2", -1),
        ("161", "3.10a", 1),
        ("8.02", "8.02", 0),
        ("3.4j", "1996.07.12", -1),
        ("3.2.pl0", "3.1.1.6", 1),
        ("2g6", "11g", -1),
        ("0.960923", "2.2beta29", -1),
        ("1.13++", "5.5.kw", -1),
    ],
)
def test_cmp(v1, v2, result):
    loosev1 = lv.LooseVersion(v1)
    loosev2 = lv.LooseVersion(v2)
    assert loosev1._cmp(loosev2) == result
    assert loosev1._cmp(v2) == result
    assert loosev2._cmp(loosev1) == -result
    assert loosev2._cmp(v1) == -result
    assert loosev1._cmp(object()) == NotImplemented
    assert loosev2._cmp(object()) == NotImplemented


@pytest.mark.parametrize(
    "vstring,version",
    [
        ("1.5.1", [1, 5, 1]),
        ("1.5.2b2", [1, 5, 2, "b", 2]),
        ("161", [161]),
        ("3.10a", [3, 10, "a"]),
        ("1.13++", [1, 13, "++"]),
    ],
)
def test_split(vstring, version):
    # Regression test to ensure we don't accidentally break parsing (again)
    # This can be changed if the version representation changes
    v = lv.LooseVersion(vstring)
    assert v.vstring == vstring
    assert v.version == version


@pytest.mark.parametrize(
    "v1,v2,result",
    [
        ("0.3@v0.3", "0.3.1@v0.3.1", 1),
        ("0.3.1@v0.3.1", "0.3@v0.3", -1),
        ("13.0-beta3", "13.0.1", 1),
        ("13.0.1", "13.0-beta3", -1),
    ],
)
def test_py2_rules(v1, v2, result):
    """Python 2 did allow strings and numbers to be compared.
    Verify consistent, generally unintuitive behavior.
    """
    loosev1 = lv.LooseVersion(v1)
    loosev2 = lv.LooseVersion(v2)
    assert loosev1._cmp(loosev2) == result
    assert loosev1._cmp(v2) == result
    assert loosev2._cmp(loosev1) == -result
    assert loosev2._cmp(v1) == -result


if __name__ == "__main__":
    sys.exit(pytest.main([__file__] + sys.argv[1:]))
