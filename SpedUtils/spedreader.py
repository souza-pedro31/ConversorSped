from copy import deepcopy

class SpedReader:
    """
    Inicia o leitor e faz a busca do caminho que contém o SPED.
    """
    def __init__(self, sped_path:str) -> None:
        self.__sped_path = sped_path
        return
    
    def record_reader(self, req_record: list[str]) -> list[list]:
        """
        Faz a leitura do arquivo SPED e retorna uma lista com as linhas contendo os registros
        passados como parâmetro.
        """
        self.__sped_infos = []
        self.__data = []
        with open(self.__sped_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
            for line in lines:
                try:
                    split_line = line.split('|')
                    del(split_line[0])
                    split_line.pop()
                    self.__data.append(split_line)
                    if self.__data[0][0] in req_record:
                        self.__sped_infos.append(deepcopy(self.__data))
                        self.__data.clear()
                    self.__data.clear()
                except IndexError:
                    break
        return self.__sped_infos

if __name__ == '__main__':
    pass