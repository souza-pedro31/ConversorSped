from SpedUtils.spedreader import SpedReader
from SpedUtils.spedgendocs import SpedCsv

class SpedContribuicoes(SpedReader, SpedCsv):
    """
    Inicia o leitor e gerador de arquivos SPED Contribuições. Já contém os blocos.
    """
    def __init__(self, sped_path: str) -> None:
        super().__init__(sped_path)
    
    def record_reader(self, req_record) -> None:
        return super().record_reader(req_record)
    
    @property
    def block_zero(self) -> list:
        """
        Retorna os registros do bloco zero
        """
        __block_records = ['0000', '0001', '0035', '0100', '0110', '0111', '0120',
                                '0140', '0145', '0150', '0190', '0200', '0205', '0206',
                                '0208', '0400', '0450', '0500', '0600', '0990']        
        return __block_records
    
    @property
    def block_A(self) -> list:
        """
        Retorna os registros do bloco A
        """
        __block_records = ['A001', 'A010', 'A100', 'A110', 'A111', 'A120', 'A170',
                                'A990']        
        return __block_records
        
    @property 
    def block_C(self) -> list:
        """
        Retorna os registros do bloco C
        """        
        __block_records = ['C001', 'C010', 'C100', 'C110', 'C111', 'C120', 'C170',
                                'C175', 'C180', 'C181', 'C185', 'C188', 'C190', 'C191',
                                'C195', 'C198', 'C199', 'C380', 'C385', 'C395','C396',
                                'C400', 'C405', 'C481', 'C485', 'C489', 'C490', 'C491',
                                'C495', 'C499','C500', 'C501', 'C505', 'C509', 'C600',
                                'C601', 'C605', 'C609', 'C800', 'C810', 'C820', 'C830',
                                'C860', 'C870', 'C880', 'C890', 'C990']        
        return __block_records
    
    @property
    def block_D(self) -> dict:
        """
        Retorna os registros do bloco D
        """        
        __block_records = ['D001', 'D010', 'D100', 'D101', 'D105', 'D111', 'D200',
                                'D201', 'D205', 'D209', 'D300', 'D309', 'D350', 'D359',
                                'D500', 'D501', 'D505', 'D509', 'D600', 'D601', 'D605',
                                'D609', 'D990']        
        return __block_records


if __name__ == '__main__':  
    pass
