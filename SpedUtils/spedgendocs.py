from copy import deepcopy
import csv
from SpedUtils.spedreader import SpedReader
from pathlib import Path

class SpedCsv:
    """
    Inicia o gerador de relatórios SPED em CSV.
    """
    def __init__(self) -> None:
        return

    def generate_sped_csv(self, sped: SpedReader, file_name: str = 'relatório') -> None:
        """
        Recebe a lista de informações geradas pelo módulo SpedReader, um nome (opcional) para o relatório e
        gera um documento CSV.
        """
        file_name += '.csv'
        path = Path(__file__).parent.parent / file_name

        with open(path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for item in sped:
                writer.writerow(item[0])
        return
        

if __name__ == '__main__':
    pass
