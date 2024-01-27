class SpedReader:
    def __init__(self, sped_path:str) -> None:
        self.__sped_path = sped_path
        return


    def record_reader(self) -> dict:
        self.__sped_file = open(self.__sped_path, 'r', encoding='latin-1', errors='ignore')
        self.__full_sped = {}
        self.__sped_erro = []
        
        for index, sped_line in enumerate(self.__sped_file):
            try:
                records = sped_line[1:5]
                self.__full_sped[f'{index}-{records}'] = {f'{sped_line[6:]}'}
            except Exception as erro:
                self.__sped_erro.append(('Erro:',erro,'on record:', sped_line))
                continue
        return self.__full_sped
    
    def find_records(self, full_sped: dict ,registration_requested: str) -> dict:
        self.__sped_infos = {}
        for key, value in full_sped.items():
            if key[-4:] == registration_requested:
                self.__sped_infos[key] = value        
        return self.__sped_infos
    

    @property
    def registry_errors(self) -> list[str]:
        return self.__sped_erro


    def generate_sped_file(self, sped_infos: dict) -> None:
        with open('sped_file','w') as file:
            file.write('')

        file = open('sped_file', 'a')
        for key, value in sped_infos.items():
            file.write(f'{key}:{value}\n')
        file.close()

if __name__ == '__main__':
    reader = SpedReader('/home/pedro-souza/Documentos/ConversorSped/PISCOFINS.txt')
    a = reader.record_reader()
    b = reader.find_records(a, '0000')