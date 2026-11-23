"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

import pytest

from lippu import (
    AIKUINEN_HINTA,
    ELAKELAINEN_HINTA,
    LAPSI_HINTA,
    kokonaishinta,
    lippuhinta,
)


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika)
    # Assert: tarkistetaan tulos
    assert hinta == 15.0


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.test
@pytest.mark.parametrize(
    "ika, odotettu",
    [
        (6, 0.0),
        (7, LAPSI_HINTA),
        (17, LAPSI_HINTA),
        (18, AIKUINEN_HINTA),
        (64, AIKUINEN_HINTA),
        (65, ELAKELAINEN_HINTA),
        (120, ELAKELAINEN_HINTA),
    ],



    
)
def test_lippuhinta_raja_arvot(ika, odotettu):
    assert lippuhinta(ika) == odotettu


# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
# Vinkki: with pytest.raises(ValueError):

@pytest.mark.parametrize("virheellinen_ika", [-1, 121])
def test_lippuhinta_virheellinen_ika(virheellinen_ika):
    with pytest.raises(ValueError):
        lippuhinta(virheellinen_ika)


def test_kokonaishinta_tyhja():
    assert kokonaishinta([]) == 0.0


def test_kokonaishinta_ei_ryhmaalennusta():
    iat = [30] * 9
    assert kokonaishinta(iat) == 9 * AIKUINEN_HINTA


def test_kokonaishinta_ryhmaalennus():
    iat = [30] * 10
    # Tarkista tehtävänannosta ryhmäalennuksen tarkka prosentti (esim. 10 % -> * 0.9)
    assert kokonaishinta(iat) == 10 * AIKUINEN_HINTA * 0.9

def test_opiskelijalippu():
    assert lippuhinta(20, opiskelija=True) == 10.0

def lippuhinta(ika: int, opiskelija: bool = False) -> float:
    if ika < 0 or ika > 120:
        raise ValueError("Virheellinen ikä")
    
    if ika < 7:
        return 0.0
    if opiskelija:
        return 10.0
    if ika <= 17:
        return 8.0
    if ika >= 65:
        return 10.0
    
    return 15.0




    #hei testi 2 kun git ei lisännyt

# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).
def test_kokonaishinta_tyhja():
    assert kokonaishinta([]) == 0.0


def test_kokonaishinta_ei_ryhmaalennusta():
    iat = [30] * 9
    assert kokonaishinta(iat) == 9 * AIKUINEN_HINTA


def test_kokonaishinta_ryhma_alennus():
    iat = [30] * 10
    assert kokonaishinta(iat) == 10 * AIKUINEN_HINTA * 0.9


