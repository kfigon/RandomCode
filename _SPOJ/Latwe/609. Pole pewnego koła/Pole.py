PI = 3.141592654
import math
def foo(promien, odlegloscMiedzySrodkami):
    odlegloscDoOkregu = odlegloscMiedzySrodkami/2
    # juz do kwadratu
    promienOkregu = promien**2 - odlegloscDoOkregu**2
    return PI * promienOkregu