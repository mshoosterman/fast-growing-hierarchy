from Ordinal_Number import Ordinal


def fast(ordinal: Ordinal, n: int) -> int:
    if ordinal.is_zero():
        return n+1
    if ordinal.is_successor():
        return _composition_helper(fast, n, ordinal.predecessor(), n)
    if ordinal.is_lim():
        return fast(ordinal.fun_seq(n), n)


def _composition_helper(f: function, n: int, ord_arg: Ordinal, int_arg: int) -> int:
    if n == 0:
        return f(ord_arg, int_arg)
    if n > 0:
        return _composition_helper(f, n-1, ord_arg, int_arg)
    else:
        raise Exception("n should be non-negative")
