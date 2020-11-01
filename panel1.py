# ver:2019

import time
import random

class Panel1:
      def __init__(self):
        self.first_dialogues = [
                                "新発売になった、" ,
                                "このペプシジャパンコーラ" ,
                                "飲んでみたくないですか？" ,
                                "僕と勝負して勝ったら、",
                                "一本あげますよ。",
                                "じゃんけん！✊(真顔)"
                                ]

        self.win_log = [
                        "やるやん。" , 
                        "明日は俺にリベンジさせて。" , 
                        "では、どうぞ。"
                        ]

        self.lose_log_r = [
                          "俺の勝ち！",
                          "負けは次につながるチャンスです！",
                          "ネバーギブアップ！",
                          "ほな、いただきます！"
                          ]

        self.lose_log_s = [
                          "俺の勝ち！" , 
                          "たかがじゃんけん、そう思ってないですか？" , 
                          "それやったら明日も、俺が勝ちますよ" ,
                          "ほな、いただきます！"
                          ]

        self.lose_log_p = [
                          "俺の勝ち！",
                          "なんで負けたか、明日まで考えといてください。(ドヤ顔)",
                          "そしたら何かが見えてくるはずです",
                          "ほな、いただきます！"
                          ]

        self.ep_log = [
                      "一日一回勝負。" , 
                      "じゃあ、また明日。👋(ニッコリ)"
                      ]
        
        self.effect = " 🍺「ｼｭﾜｱｱｱ!!」"

        self.selecter = ["✊" , "✌️" , "✋" ]
        self.ksk_select = ["win" ,"lose" ,"lose" ,"lose" ,"lose" ,"lose" ,"lose" "lose" ,"lose" ,"lose"]
        self.user_hand = ""
        self.ksk_hand = ""

      def prologue(self):
        Panel1.log_contorolar(self.first_dialogues)
        time.sleep(1)
        print("あなたは何を出す？")

      def select_hands(self):
        print("{} -> {}でツイート  {} -> {} でツイート  {} -> {}でツイート".format(
          0 , self.selecter[0],
          1 , self.selecter[1],
          2 , self.selecter[2],
        ))
        self.user_hand = int(input(" >> "))

        if self.user_hand > 2:
          self.user_hand = random.randint(0 , 2)

      def ksk_select_hand(self):
        if self.user_hand == 0:
          Panel1.selct_controlar(self.ksk_select , "✌️" , "✋")

          self.ksk_hand = random.choice(self.ksk_select)

        elif self.user_hand == 1:
          Panel1.selct_controlar(self.ksk_select , "✋" , "✊")

          self.ksk_hand = random.choice(self.ksk_select)

        elif self.user_hand == 2:
          Panel1.selct_controlar(self.ksk_select , "✊" , "✌️")

          self.ksk_hand = random.choice(self.ksk_select)

      def judgement(self):
        if self.ksk_hand == self.ksk_select[0]:
          Panel1.youwin(self)

        else:
          Panel1.youlose(self)

      def youwin(self):
        time.sleep(2)
        print("HDKSK 「じゃんけんポン{}！(真顔)」".format(self.ksk_hand))
        time.sleep(3)
        print("YOU WIN(ﾋﾟｭｳｳｳｳｳｳ!!!)")
        time.sleep(3)
        Panel1.log_contorolar(self.win_log)
        Panel1.effect()

      def youlose(self):
        time.sleep(2)
        print("HDKSK 「じゃんけんポン{}！(真顔)」".format(self.ksk_hand))
        time.sleep(3)
        print("YOU LOSE(ﾌﾞｳｳｳｳｳｳ!!!)")
        time.sleep(3)

        if self.user_hand == 0:
          Panel1.log_contorolar(self.lose_log_r)

        elif self.user_hand == 1:
          Panel1.log_contorolar(self.lose_log_s)

        elif self.user_hand == 2:
          Panel1.log_contorolar(self.lose_log_p)

        Panel1.effect()
        Panel1.epilogue(self)

      def epilogue(self):
        Panel1.log_contorolar(self.ep_log)

      def selct_controlar(a , w , l):
        for i , _ in enumerate(a):
          a[i] = l
          a[0] = w

      def log_contorolar(logs):
        for log in logs:
          print("HDKSK 「{}」".format(log))
          time.sleep(2)

      def effect():
        print("    🍺「ｼｭﾜｱｱｱ!!」")
        time.sleep(4)


panel = Panel1()
panel.prologue()
panel.select_hands()
panel.ksk_select_hand()
panel.judgement()