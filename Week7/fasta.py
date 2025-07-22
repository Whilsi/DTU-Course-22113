class Fasta:
    alphabets = {'DNA' : 'ATCG', 'RNA' : 'AUCG', 'Protein' : 'ILVFMCAGPTSYWQNHEDKR'}

    def load(self,filename:str):
        with open(filename) as infile:
            self.lines = infile.readlines()
            self.headers = []
            self.sequences = []
            sequence_str = ''
            for line in self.lines:
                if line.startswith('>'):
                    if sequence_str != '':
                        self.sequences.append(''.join(sequence_str.split()))
                        sequence_str = ''
                    self.headers.append(line.strip())
                else:
                    sequence_str += line
            if sequence_str != '':
                self.sequences.append(''.join(sequence_str.split()))

    def save(self,filename:str):
        with open(filename,'w') as outfile:
            headers,sequences = self.content()
            for i in range(len(headers)):
                outfile.write(headers[i]+'\n')
                for j in range(0,len(sequences[i]),60):
                    outfile.write(sequences[i][j:j+60]+'\n')
    
    def content(self,start:int = None, end:int = None) -> list[list[str]]:
        if hasattr(self,'headers') and hasattr(self,'sequences'):
            if start == None:
                return self.headers,self.sequences
            elif end == None:
                return self.headers[start],self.sequences[start]
            else:
                return self.headers[start:end],self.sequences[start:end]
        else:
            raise NameError('The file has not been loaded yet.')
        
    def delete(self,start:int = None,end:int = None ):
        if start == None:
            del self.headers
            del self.sequences
        elif end == None:
            try:
                self.headers.pop(start)
                self.sequences.pop(start)
            except:
                print('The index is out of range')
        else:
            try:
                start = len(self.headers[:start])
                end = len(self.headers[:end])
                for i in range(start,end):
                    self.headers.pop(start)
                    self.sequences.pop(start)
            except:
                print('The interval is out of range')
    
    def insert(self,header:str,sequence:str,position:int = None):
        if position == None:
            self.headers.append(header)
            self.sequences.append(sequence)
        else:
            self.headers.insert(position,header)
            self.sequences.insert(position,sequence)

    def verify(self, alphabet, start:int = None, end:int = None):
        if alphabet in Fasta.alphabets:
            if start == None:
                for sequence in self.sequences:
                    for letter in sequence:
                        if letter not in Fasta.alphabets[alphabet]:
                            return False
            elif end == None:
                for letter in self.sequences[start]:
                    if letter not in Fasta.alphabets[alphabet]:
                        return False
            else:
                for sequence in self.sequences[start:end]:
                    for letter in sequence:
                        if letter not in Fasta.alphabets[alphabet]:
                            return False
            return True
        else:
            print('Alphabet not defined in class')

    def discard(self, alphabet, start:int = None, end:int = None):
        if alphabet in Fasta.alphabets:
            start = len(self.headers[:start])
            end = len(self.headers[:end])
            headers = []
            sequences = []
            for i in range(len(self.headers)):
                if self.verify(alphabet,i):
                    headers.append(self.headers[i])
                    sequences.append(self.sequences[i])
                elif start != None and end == None and i != start:
                    headers.append(self.headers[i])
                    sequences.append(self.sequences[i])
                elif start != None and end != None and i not in range(start,end):
                    headers.append(self.headers[i])
                    sequences.append(self.sequences[i])
            self.headers = headers
            self.sequences = sequences


                
        
myfasta = Fasta()
myfasta.load("dna7.fsa")
print(myfasta.verify('DNA',-1))
# myfasta.discard('DNA',-1)
# print(myfasta.content(0,-2))
# myfasta.delete(-2,-1)
myfasta.save("newfile.fsa")