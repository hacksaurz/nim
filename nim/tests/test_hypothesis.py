from hypothesis import given, strategies as st

from nim.game import Bot


@given(state=st.lists(elements=st.integers()))
def test_non_zero_pile_indexes(state):
    assert Bot().nonzero_pile_indexes(state) == [i for i, n in enumerate(state)
                                                 if n >= 1]
