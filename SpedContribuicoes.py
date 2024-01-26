from SpedReader import *

class SpedContribuicoes(SpedReader):
    def __init__(self, sped_path:str) -> None:
        super().__init__(sped_path)
        return
    
    def record_reader(self, registration_requested:str) -> list[str]:
        return super().record_reader(registration_requested)


    def block_zero(self) -> None:
        zero_block_records = ['0000', '0001', '0035', '0100', '0110', '0111', '0120',
                            '0140', '0145', '0150', '0190', '0200', '0205', '0206',
                            '0208', '0400', '0450', '0500', '0600', '0990']        
        zero_block_infos = {}

        for records in zero_block_records:
            record_info = SpedContribuicoes.record_reader(self, records)
            for index, record in enumerate(record_info):
                zero_block_infos = {f'{index} {records}':f'{record}'}
                print(zero_block_infos)
        return zero_block_infos



if __name__ == '__main__':  
    s = SpedContribuicoes('/home/pedro-souza/Documentos/ConversorSped/PISCOFINS.txt')
    a = s.block_zero()
    print(a)