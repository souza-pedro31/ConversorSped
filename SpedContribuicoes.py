from SpedUtils.SpedReader import SpedReader
from SpedUtils.SpedGenDocs import SpedPlan

class SpedContribuicoes(SpedReader):
    def __init__(self, sped_path:str) -> None:
        super().__init__(sped_path)
        self.__block_records = []
        return
    

    def record_reader(self) -> list[str]:
        return super().record_reader()


    def block_zero(self) -> dict:
        self.__block_records = ['0000', '0001', '0035', '0100', '0110', '0111', '0120',
                                '0140', '0145', '0150', '0190', '0200', '0205', '0206',
                                '0208', '0400', '0450', '0500', '0600', '0990']        
        record_info, size_sped_info = super().record_reader(self.__block_records)
        a = size_sped_info//1000 if size_sped_info//1000 > 1 else 1
        print(f'{a} gravações necessárias!')
        return record_info, size_sped_info
    
    def block_A(self) -> dict:
        self.__block_records = ['A001', 'A010', 'A100', 'A110', 'A111', 'A120', 'A170',
                                'A990']        
        record_info, size_sped_info = super().record_reader(self.__block_records)
        a = size_sped_info//1000 if size_sped_info//1000 > 1 else 1
        print(f'{a} gravações necessárias!')
        return record_info, size_sped_info
        

    def block_C(self) -> dict:
        self.__block_records = ['C001', 'C010', 'C100', 'C110', 'C111', 'C120', 'C170',
                                'C175', 'C180', 'C181', 'C185', 'C188', 'C190', 'C191',
                                'C195', 'C198', 'C199', 'C380', 'C385', 'C395','C396',
                                'C400', 'C405', 'C481', 'C485', 'C489', 'C490', 'C491',
                                'C495', 'C499','C500', 'C501', 'C505', 'C509', 'C600',
                                'C601', 'C605', 'C609', 'C800', 'C810', 'C820', 'C830',
                                'C860', 'C870', 'C880', 'C890', 'C990']        
        record_info, size_sped_info = super().record_reader(self.__block_records)
        a = size_sped_info//1000 if size_sped_info//1000 > 1 else 1
        print(f'{a} gravações necessárias!')
        return record_info, size_sped_info

    
    def block_D(self) -> dict:
        self.__block_records = ['D001', 'D010', 'D100', 'D101', 'D105', 'D111', 'D200',
                                'D201', 'D205', 'D209', 'D300', 'D309', 'D350', 'D359',
                                'D500', 'D501', 'D505', 'D509', 'D600', 'D601', 'D605',
                                'D609', 'D990']        
        record_info, size_sped_info = super().record_reader(self.__block_records)
        a = size_sped_info//1000 if size_sped_info//1000 > 1 else 1
        print(f'{a} gravações necessárias!')
        return record_info, size_sped_info      

    @property
    def get_block_records(self):
        return self.__block_records


if __name__ == '__main__':  
    s = SpedContribuicoes('/home/pedro-souza/Documentos/ConversorSped/PISCOFINS.txt')
    b, z = s.block_C()
    sp = SpedPlan()
    sp.generate_sped_log(b)
    c = s.get_block_records
    sp.generate_sped_plan(c, '/home/pedro-souza/Documentos/ConversorSped/SpedLog.txt', z)
    