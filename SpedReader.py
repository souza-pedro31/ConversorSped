
class SpedReader:
    def __init__(self, sped_path:str) -> None:
        self.__sped_path = sped_path
        return


    def record_reader(self, registration_requested:str) -> list[str]:
        self.__sped_file = open(self.__sped_path, 'r', encoding='latin-1', errors='ignore')
        self.__sped_infos = []
        self.__sped_erro = []
        
        for sped_line in self.__sped_file:
            try:
                records = sped_line[1:5]
                if records == registration_requested:
                    self.__sped_infos.append(sped_line)
            except Exception as erro:
                self.__sped_erro.append(('Erro:',erro,'on record:', sped_line))
                continue
        return self.__sped_infos
    
    @property
    def registry_errors(self) -> list[str]:
        return self.__sped_erro

if __name__ == '__main__':
    reader = SpedReader('/home/pedro-souza/Documentos/ConversorSped/PISCOFINS.txt')
    a  = reader.record_reader('0000')

class teste(SpedReader):
    def __init__(self, sped_path: str) -> None:
        super().__init__(sped_path)

    def record_reader(self, registration_requested: str) -> list[str]:
        return super().record_reader(registration_requested)