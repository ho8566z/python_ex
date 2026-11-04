import os
import json

if __name__ == "__main__":
    import sys

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    sys.path.append(project_root)

from db import dbManager
from db import config

RESOURCE_PATH = f"{os.getcwd()}\\resources"
PATH_MEMBER = f"{RESOURCE_PATH}\\member.json"
PATH_BANK = f"{RESOURCE_PATH}\\bank.json"
PATH_MEMO = f"{RESOURCE_PATH}\\memo.json"
PATH_TODO = f"{RESOURCE_PATH}\\todo.json"


def saveAtFile(path, data):
    """딕셔너리·리스트 데이터를 UTF-8 JSON 파일(들여쓰기 4칸, 한글 유지)로 저장한다."""
    with open(f"{path}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def dbSaveAllAtFile():
    """dbManager 의 회원·계좌·메모·할일 데이터를 각각의 JSON 파일에 저장한다."""
    saveAtFile(PATH_MEMBER, dbManager.members)
    saveAtFile(PATH_BANK, dbManager.bankAccounts)
    saveAtFile(PATH_MEMO, dbManager.memos)
    saveAtFile(PATH_TODO, dbManager.todoLists)


def loadFromFile(path, hook=None):
    """JSON 파일을 읽어 파이썬 객체로 반환한다. hook 이 있으면 object_hook 으로 사용한다."""
    with open(f"{path}", encoding="utf-8") as file:
        data = json.load(file, object_hook=hook)
        return data


def restoreBankLog(dct):
    # json에 데이터를 저장할 때 튜플->리스트가 되므로 로드할 때 리스트를 튜플로 바꿔줌
    if config.BANK_LOG in dct:
        for idx, item in enumerate(dct[config.BANK_LOG]):
            dct[config.BANK_LOG][idx] = tuple(item)

    return dct


def dbLoadAllFromFile():
    """JSON 파일에서 회원·계좌·메모·할일 데이터를 읽어 dbManager 에 채운다."""
    dbManager.members = loadFromFile(PATH_MEMBER)
    dbManager.bankAccounts = loadFromFile(PATH_BANK, restoreBankLog)
    dbManager.memos = loadFromFile(PATH_MEMO)
    dbManager.todoLists = loadFromFile(PATH_TODO)


# if __name__ == "__main__":

#     def printInfo(dct):
#         print(dct)

#     def printAll():
#         printInfo(dbManager.members)
#         printInfo(dbManager.bankAccounts)
#         printInfo(dbManager.memos)
#         printInfo(dbManager.todoLists)

#     dbLoadAllFromFile()
#     printAll()

#     print("=" * 200)

#     dbManager.members = None
#     dbManager.bankAccounts = None
#     dbManager.memos = None
#     dbManager.todoLists = None

#     # dbSaveAllAtFile()
#     printAll()
