import openpyxl 

class SpedPlan:
    def __init__(self) -> None:
        self.__wb = openpyxl.Workbook()
        self.__ws = self.__wb.active
        self.__ws.title = 'Resumo'
        return


    def generate_sped_plan(self, sped_block:list[str], block_infos:dict) -> None:
        data_plan = []
        for record in sped_block:
            self.__wb.create_sheet(record)

        for key, value in block_infos.items():
            for info in value:
                format_info = info.split('|')
                for f_i in format_info:
                    if len(f_i) > 0 and f_i != '\n':
                        data_plan.append(f_i)

                ws_name = self.__wb[key[-4:]].title
                ws = self.__wb[key[-4:]]
                if key[-4:] == ws_name:
                    ws.append(data_plan)
                    data_plan.clear()
                    
        self.__wb.save('relatório sped.xlsx')


if __name__ == '__main__':
    sp = SpedPlan()
    block_infos = dict()
    block_infos['0-0000'] = 'blableblibloblu'
    block_infos['0-0001'] = 'blublobliblebla'
    sp.generate_sped_plan(block_infos)