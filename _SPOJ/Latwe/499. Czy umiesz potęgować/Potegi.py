def foo(podstawa, wykladnik):
    # asd = (podstawa**3)%10

    asd = podstawa
    for i in range(2, wykladnik+1):
        asd *= podstawa

    asd %= 10
    return str(asd)
