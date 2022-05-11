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
