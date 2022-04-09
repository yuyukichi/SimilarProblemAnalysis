from array import array
import numpy as np

class User():
	def __init__(self,name,sex,age,work,qol):
		self.date = [name,sex,age,work,qol]

#ユーザーデータを定義するクラス
# name = 名前
# sex = 性別（男性 = 0 女性 = 1）
# age = 年齢 1~150
# work = 職業 (学生 = 0 社会人 = 1)
# qol = 主観的QOL尺度の得点
# 
# >主観的QOL尺度
# 1.はい 2.いいえ 3.どちらでもない を回答
#（１）毎日の生活が楽しいですか
#（２）まわりの人があなたの困っていることをどのように思っているか気になりますか
#（３）あなたは今の自分を好きですか
#（４）将来に希望がありますか
#（５）自分が困っていることに対するまわりの人の偏見を感じますか
#（６）毎日の生活に張り合いを感じていますか
#（７）あなたは生きる目標をもっていますか
#（８）急に自分の具合が悪くならないかと、いつも心配していますか
#（９）あなたはいまいきいきとしていると感じますか
# 得点計算法：質問（２）、（５）、（８）は（1,2,3）➜（0,2,1）それ以外の質問は（1,2,3）➜（2,0,1）と変換を行い、（１）〜（９）の値を合計する。
# 算出された値が高ければ高いほど、困りごとを受容し、前向きに捉えられている。

O = User("O",1,16,0,13)
T = User("T",1,14,0,9)
M = User("M",1,14,0,14)
Yuki = User("Yuki",0,17,0,9)
#未踏企画書に記載した比較に利用した値

def euclidean_distance_chack(user_date1,user_date2):
	a = np.array([user_date1[1],user_date1[2],user_date1[3],user_date1[4]])
	b = np.array([user_date2[1],user_date2[2],user_date2[3],user_date2[4]])
	distance  = np.linalg.norm(b-a)
	return distance
#ユークリッド距離を算出して出力する関数 類似性が高ければ高いほど0に近づく

def presented_similar_users(main_user,*users):
	dict = {};
	for i in users:
		dis = euclidean_distance_chack(main_user.date,i.date)
		dict.setdefault(i.date[0],dis)
	return min(dict, key=dict.get)
#ユークリッド距離を利用してmain_userともっとも類似度の高いユーザーを出力する関数
