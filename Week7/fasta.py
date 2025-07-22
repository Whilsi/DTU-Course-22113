class Fasta:
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
    
    def content(self) -> list[list[str]]:
        if hasattr(self,'headers') and hasattr(self,'sequences'):
            return self.headers,self.sequences
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
                for i in range(start,end+1):
                    self.headers.pop(start)
                    self.sequences.pop(start)
            except:
                print('The interval is out of range')
                
        
myfasta = Fasta()
myfasta.load("dna7.fsa")
# myfasta.delete(0,-1)
print(myfasta.content())
myfasta.save("newfile.fsa")