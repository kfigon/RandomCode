__author__ = 'kamil'


def foo(wiekMatki,zaXLat,bedzieStartszeTyleRazy):
    dziecko = (wiekMatki+zaXLat)/(bedzieStartszeTyleRazy-1)
    dlugoscCiazy = (dziecko - zaXLat)*12

    # szczegolny przypadek
    if(dlugoscCiazy==0):
        return 1

    return round(dlugoscCiazy)