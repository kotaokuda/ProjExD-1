import random
import time
num_alpa = 0 # 対象文字数
remove_alpha = 0 #欠損文字数
max_rec = 10 #最大繰り返し回数
now_chg = 0 #繰り返し回数
start = time.time() #開始時間を計測
def syutudai(): #問題を出題
    global num_alpa , remove_alpha
    az = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num_alpa = random.randint(5,20)
    remove_alpha = random.randint(1,num_alpa-3)
    ques_alphas = [az.pop(random.randint(0,25-i)) for i in range(num_alpa)] #対象文字リストを作成
    all_alphas = ques_alphas.copy() #対象文字リストをコピー
    rem_alphas = [ques_alphas.pop(random.randint(0,num_alpa-i-1)) for i in range(remove_alpha)] #欠損文字リストを作成、ques_alphasを表示文字リストに変更
    
    print("対象文字")
    for alpha in all_alphas:
        print(alpha,end=" ")
    print()
    
    # print("欠損文字") #デバッグ用欠損文字表示
    # for rem in rem_alphas:
    #     print(rem,end=" ")
    # print()
    
    print("表示文字")
    for i in range(len(ques_alphas)):
        view = random.choice(ques_alphas)
        ques_alphas.remove(view)
        print(view,end=" ")
    print("\n")
    
    kaito(remove_alpha,rem_alphas) #回答用関数を呼び出し、欠損文字数と、欠損文字リストを引数に指定

def kaito(rem,rems): #問題に解答
    InputRem = input("欠損文字はいくつあるでしょうか？:")
    try: #だが、例外処理をする 
        if(int(InputRem)==rem): #入力数が欠損文字数があっているかをチェック
            print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
            for i in range(rem):
                InputAlpha = input(f"{i+1}つ目の文字を入力してください:").upper()
                if InputAlpha in rems: #欠損文字リストに入力文字があるかをチェック
                    rems.remove(InputAlpha) #答えた文字を欠損文字リストから削除
                else:
                    replay() #再チャレンジ関数を呼び出し
                    return None #間違えた場合ここまでで、この関数での処理を終える
            end =time.time()
            print(f"正解です。タイムは{int(end-start)}秒でした。")
        else:
            replay() #再チャレンジ関数を呼び出し
    except ValueError: 
        print("数字を入力してください")
        kaito(rem,rems) #回答用関数を呼び出し、もう一度入力できる
    

def replay(): #再チャレンジ
    global now_chg
    if(now_chg < max_rec): #再チャレンジ可能かを確認
        print("不正解です。またチャレンジしてください")
        print("-"*40)
        now_chg += 1 
        syutudai() #問題を出題する関数を呼び出す
    else:
        print("不正解です。そして、もう解くことはできません")

if(__name__ =="__main__"):
    syutudai()