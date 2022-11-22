import random
import datetime

def syutudai(question):
    quest = random.choice(questions)
    p_quest = quest["q"]
    print(f"問題:{p_quest}")
    answer = input("答えるんだ:")
    return answer,quest

def kaito(answer,quest):
    if(answer in quest["a"]):
        print(f"正解!!!")
    else:
        print(f"出直してこい")

if __name__ == "__main__":
    questions = [{"q":"サザエさんの旦那の名前は？","a":["マスオ","ますお"]},{"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},{"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}]
    start = datetime.datetime.now()
    ans,qus = syutudai(questions)
    end = datetime.datetime.now()
    kaito(ans,qus)
    print(f"回答時間:{(end-start).seconds}秒")
    