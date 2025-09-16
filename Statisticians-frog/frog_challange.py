def verjetnosti(m, n):
    """
    Izracuna verjetnost, da pride zaba na m-ti lokvan v n skokih.
    P = sum(1 / m, 1 / (m - 1), ..., 1 zmnožek n taksnih stevil, kjer gre vsota po
    vseh moznih kombincijah, s tem da je vsak naslednji imenovalec manjsi.)
    """

    if n == 1:
        return 1. / m
    else:
        v = 0
        for j in range(m - n + 1, 0, -1):
            v += verjetnosti(m - j, n - 1)
        return v / m


def povprecje_skokov(m):
    """
    Izracuna pricakovan oz. povprecno vrednost skokov zabe za m lokvanov, kjer je
    verjetnost za skok iz k-tega na enega izmed naslednjih lokvanov enaka 1 /  (m - k).
    """
    povp = 0
    for i in range(1, m + 1):
        povp += i * verjetnosti(m, i)
    return povp

