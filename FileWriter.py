class writer :

    def __init__(self, separator = "\n" , filename = 'File.txt', mode = 'a' ):
        self.separator = separator
        self.filename = filename
        self.mode = mode
        
    def writes(self, string):
        with open( self.filename, mode = self.mode ) as file :
            file.write(string)
            file.write(self.separator)
        
