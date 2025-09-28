import pytest,sys
sys.path.append('/home/wsl_ubuntu/DTU/22113/Week8/src')
sys.path.append('testdata')
from fasta import Fasta

@pytest.fixture()
def myFasta():
    return Fasta()

def test_1(myFasta):
    with pytest.raises(FileNotFoundError):
        myFasta.load('NotAFile')

def test_2(myFasta):
    with pytest.raises(FileNotFoundError):
        myFasta.load(None)

def test_3(myFasta):
    myFasta.load('testdata/test1.fsa')
    assert myFasta.sequences == [] and myFasta.headers == ['>'], 'Simple file'

def test_4(myFasta):
    myFasta.load('testdata/test2.fsa')
    assert myFasta.sequences == ['ATG'] and myFasta.headers == ['>U2'], 'One header and one sequence'

def test_5(myFasta):
    myFasta.load('testdata/test3.fsa')
    assert myFasta.sequences == ['ATGCU'] and myFasta.headers == ['>test'], 'Sequence on multiple lines'

def test_6(myFasta):
    myFasta.load('testdata/test4.fsa')
    assert myFasta.sequences == ['ATGC','1234','ABCD'] and myFasta.headers == ['>seq1','>seq2','>seq3']