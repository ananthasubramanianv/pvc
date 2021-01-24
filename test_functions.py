import pytest
import forms
import polvalcalc

class Apol:
  bonus = 1000
  uplift = 40
  mfee = 3
  bdate = 1990

class Bpol:
  bonus = 1000
  uplift = 25
  mfee = 5
  bdate = 1990

class Cpol:
  bonus = 1000
  uplift = 10
  mfee = 7
  bdate = 1990

A = Apol()
B = Bpol()
C = Cpol()

def test_polval():
    assert polvalcalc.polval('A12345').uplift == A.uplift
    assert polvalcalc.polval('B12345').uplift == B.uplift
    assert polvalcalc.polval('C12345').uplift == C.uplift
    assert polvalcalc.polval('A12345').bonus == A.bonus
    assert polvalcalc.polval('B12345').bonus == B.bonus
    assert polvalcalc.polval('C12345').bonus == C.bonus
    assert polvalcalc.polval('A12345').mfee == A.mfee
    assert polvalcalc.polval('B12345').mfee == B.mfee
    assert polvalcalc.polval('C12345').mfee == C.mfee
    assert polvalcalc.polval('A12345').bdate == A.bdate
    assert polvalcalc.polval('B12345').bdate == B.bdate
    assert polvalcalc.polval('C12345').bdate == C.bdate
    assert polvalcalc.polval('D12345') == 'invalid'

def test_bonuschk():
    assert polvalcalc.bonuschk('A12345', '1995-01-31', 'Y', A) == 'N'
    assert polvalcalc.bonuschk('A12345', '1995-01-31', 'N', A) == 'N'
    assert polvalcalc.bonuschk('A12345', '1989-01-31', 'Y', A) == 'Y'
    assert polvalcalc.bonuschk('A12345', '1989-01-31', 'N', A) == 'Y'
    assert polvalcalc.bonuschk('B12345', '1995-01-31', 'Y', A) == 'Y'
    assert polvalcalc.bonuschk('B12345', '1995-01-31', 'N', A) == 'N'
    assert polvalcalc.bonuschk('B12345', '1989-01-31', 'Y', A) == 'Y'
    assert polvalcalc.bonuschk('B12345', '1989-01-31', 'N', A) == 'N'
    assert polvalcalc.bonuschk('C12345', '1995-01-31', 'Y', A) == 'Y'
    assert polvalcalc.bonuschk('C12345', '1995-01-31', 'N', A) == 'N'
    assert polvalcalc.bonuschk('C12345', '1989-01-31', 'Y', A) == 'N'
    assert polvalcalc.bonuschk('C12345', '1989-01-31', 'N', A) == 'N'
    assert polvalcalc.bonuschk('D12345', '1989-01-31', 'N', A) == 'N'

def test_matvalcalc():
    assert polvalcalc.matvalcalc(10,A,'Y') == 1413.58
    assert polvalcalc.matvalcalc(10,A,'N') == 13.58
    assert polvalcalc.matvalcalc(10,B,'Y') == 1261.88
    assert polvalcalc.matvalcalc(10,B,'N') == 11.88
    assert polvalcalc.matvalcalc(10,C,'Y') == 1110.23
    assert polvalcalc.matvalcalc(10,C,'N') == 10.23








