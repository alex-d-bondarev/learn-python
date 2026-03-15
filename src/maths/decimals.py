from decimal import Decimal, getcontext


def test_default():
    assert 1.1 + 2.2 != 3.3
    assert abs(1.1 + 2.2 - 3.3) > 0


def test_decimals():
    assert Decimal(str(1.1)) + Decimal(str(2.2)) == Decimal(str(3.3))
    assert Decimal("1.1") + Decimal("2.2") == Decimal("3.3")


def test_format():
    assert format(Decimal('2.6759'), ".2f") == "2.68"
    assert f"{Decimal('2.675'):.2f}" == "2.68"


def test_rounding():
    assert round(Decimal('2.6759')) == 3
    assert round(Decimal('2.6759'), 1) == Decimal('2.7')
    assert round(Decimal('2.6759'), 2) == Decimal('2.68')


def test_precision():
    getcontext().prec = 4
    assert Decimal('2.6759') + Decimal('1.11101') == Decimal('3.787')
    getcontext().prec = 8
    assert Decimal('2.6759') + Decimal('1.11101') == Decimal('3.78691')
    last_3 = Decimal(10) ** -3
    assert (Decimal('2.6759') + Decimal('1.11101')).quantize(last_3) == Decimal('3.787')
