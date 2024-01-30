import openpyxl 
from copy import deepcopy

class SpedPlan:
    def __init__(self) -> None:
        self.__wb = openpyxl.Workbook()
        self.__ws = self.__wb.active
        self.__ws.title = 'Resumo'
        return


    def generate_sped_log(self, block_infos:dict) -> None:
        file = open('SpedLog.txt','a')
        file.truncate(0)
        for key, values in block_infos.items():
            file.write(f'{key[-4:]}:{values}\n')
        file.close()
        return
    

    def generate_sped_plan(self, block_records: list, path_sped_log: str, size_sped_info: int) -> None:
        file = open(path_sped_log, 'r')

        data_plan = []
        prohibited_caracters = ['\n', r"\\n'"]
        counter = 0
        plan_rows = []
        a = 0

        if size_sped_info < 1000:
            counter = 1001 - size_sped_info

        for record in block_records:
                self.__wb.create_sheet(record)
        self.__wb.save('relatório sped.xlsx')

        for f in file:
            data_plan.append([f[0:4]])
            if counter < 1000:
                start_key, end_key = f.index('{'), f.index('}')
                info = f[start_key+1:end_key]
                format_info = info.split('|')

                for f_i in format_info:
                    if len(f_i) > 0 and f_i not in prohibited_caracters:
                        data_plan[0].append(f_i)
                plan_rows.append(deepcopy(data_plan))
                data_plan.clear()
                counter += 1
            else:
                for pr in plan_rows:
                    ws_name = self.__wb[pr[0][0]].title
                    ws = self.__wb[pr[0][0]]
                    if pr[0][0] == ws_name:
                        ws.append(pr[0])
                counter = 0
                a += 1
                print(f'Gravação de número {a}')
                self.__wb.save('relatório sped.xlsx')
        return

if __name__ == '__main__':
    sp = SpedPlan()
    block_infos = dict()
    block_infos['0-0000'] = 'blableblibloblu'
    block_infos['0-0001'] = 'blublobliblebla'
    sp.generate_sped_plan(block_infos)