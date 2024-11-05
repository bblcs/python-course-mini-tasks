def solve(n):
    count = 0
    while n != 0:
        count += n & 1
        n >>= 1
        if n == -1:
            # adding the sign bit
            count += 1
            break
    return count


def test_solve():
    assert solve(0) == 0, "test case 0 failed"

    assert solve(1) == 1, "test case 1 failed"
    assert solve(2) == 1, "test case 2 failed"
    assert solve(10) == 2, "test case 3 failed"
    assert solve(100) == 3, "test case 4 failed"
    assert solve(127) == 7, "test case 5 failed"

    assert solve(-1) == 2, "test case 6 failed"
    assert solve(-128) == 1, "test case 7 failed"
    assert solve(-10) == 3, "test case 8 failed"
    assert solve(-1000) == 3, "test case 9 failed"
    assert solve(-123) == 3, "test case 10 failed"

    print("all tests passed")


test_solve()
