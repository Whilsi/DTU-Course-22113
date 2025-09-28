import pytest,sys
sys.path.append('/home/wsl_ubuntu/DTU/22113/Week8/src')
from fasta import Fasta

@pytest.fixture()
def myFasta():
    return Fasta()

@pytest.fixture()
def loadedFasta(myFasta):
    myFasta.headers = ['>header1','>header2','>header3','>header4','>header5','>header6']
    myFasta.sequences = ['seq1','seq2','seq3','seq4','seq5','seq6']
    return myFasta


def test_1(myFasta):
    with pytest.raises(AttributeError):
        myFasta.delete()

def test_2(loadedFasta):
    loadedFasta.delete()
    with pytest.raises(AttributeError):
        loadedFasta.headers

def test_3(loadedFasta):
    with pytest.raises(IndexError):
        loadedFasta.delete(6)

def test_4(loadedFasta):
    loadedFasta.delete(0)
    assert loadedFasta.headers == ['>header2','>header3','>header4','>header5','>header6'] and loadedFasta.sequences == ['seq2','seq3','seq4','seq5','seq6']

def test_5(loadedFasta):
    loadedFasta.delete(1)
    assert loadedFasta.headers == ['>header1','>header3','>header4','>header5','>header6'] and loadedFasta.sequences == ['seq1','seq3','seq4','seq5','seq6']

def test_6(loadedFasta):
    loadedFasta.delete(-1)
    assert loadedFasta.headers == ['>header1','>header2','>header3','>header4','>header5'] and loadedFasta.sequences == ['seq1','seq2','seq3','seq4','seq5']

def test_7(loadedFasta):
    loadedFasta.delete(1,4)
    assert loadedFasta.headers == ['>header1','>header5','>header6'] and loadedFasta.sequences == ['seq1','seq5','seq6']

def test_8(loadedFasta):
    loadedFasta.delete(0,-1)
    assert loadedFasta.headers == ['>header6'] and loadedFasta.sequences == ['seq6']

