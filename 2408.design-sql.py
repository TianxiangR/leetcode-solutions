from typing import *

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
      self.tables: dict[str, dict[int, List[str]]] = dict()
      self.start_indices: dict[str, int] = dict()
      
      for name in names:
        self.tables[name] = dict()
        self.start_indices[name] = 0
        

    def insertRow(self, name: str, row: List[str]) -> None:
        next_index = self.start_indices[name] + 1
        self.tables[name][next_index] = row
        self.start_indices[name] = next_index
        

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId - 1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)