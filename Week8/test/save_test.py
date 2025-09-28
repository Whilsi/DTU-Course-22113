import pytest,sys
sys.path.append('/home/wsl_ubuntu/DTU/22113/Week8/src')
from fasta import Fasta

@pytest.fixture()
def myFasta():
    return Fasta()

def test_1(tmp_path,myFasta):
    with pytest.raises(ValueError):
        filename = tmp_path / 'output.fsa'
        myFasta.load('testdata/test1.fsa')
        myFasta.save(filename)

def test_2(tmp_path,myFasta):
    filename = tmp_path / 'output.fsa'
    myFasta.load('testdata/test2.fsa')
    myFasta.save(filename)
    infile = open(filename,'r')
    txt = infile.readlines()
    infile.close()
    assert txt == ['>U2\n','ATG\n'],'One sequence'

def test_3(tmp_path,myFasta):
    filename = tmp_path / 'output.fsa'
    myFasta.load('testdata/test4.fsa')
    myFasta.save(filename)
    infile = open(filename,'r')
    txt = infile.readlines()
    infile.close()
    assert txt == ['>seq1\n','ATGC\n','>seq2\n','1234\n','>seq3\n','ABCD\n'],'Multiple sequences'

def test_4(tmp_path,myFasta):
    filename = tmp_path / 'output.fsa'
    myFasta.headers = ['>very long sequence header that is definately longer than 60 characters']
    myFasta.sequences = ['AGHDITGUCGSKFIUWNVISJFHVIWEMFKXVJFIJFLKJVIAKDUDNVIDNVUDYXBXGSVCGSIWBSHTCHWGSGXYCBEYXFXBAKDYNWIXYAKAKVMNDJSHCJWUDNDHSDHUWJNCUS']
    myFasta.save(filename)
    infile = open(filename,'r')
    txt = infile.readlines()
    infile.close()
    assert txt == ['>very long sequence header that is definately longer than 60 characters\n','AGHDITGUCGSKFIUWNVISJFHVIWEMFKXVJFIJFLKJVIAKDUDNVIDNVUDYXBXG\n','SVCGSIWBSHTCHWGSGXYCBEYXFXBAKDYNWIXYAKAKVMNDJSHCJWUDNDHSDHUW\n','JNCUS\n'],'Long sequence'

def test_5(tmp_path,myFasta):
    filename = tmp_path / 'output.fsa'
    with pytest.raises(AttributeError):
        myFasta.save(filename)