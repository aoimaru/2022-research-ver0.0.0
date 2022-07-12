import numpy as np
import matplotlib.pyplot as plt
 
def draw_barchart(x, y):
       """ 棒グラフを表示する関数
       引数：
       x -- x軸の値
       y -- y軸の値
       """
       # グラフの装飾
       plt.title("Sales by Product (m$)",
              fontsize = 12) # タイトル
       plt.xlabel("Product", fontsize = 12) # x軸ラベル
       plt.ylabel("Sales", fontsize = 12) # y軸ラベル
       plt.grid(True) # 目盛線の表示
       plt.tick_params(labelsize=12) # 目盛線のラベルサイズ
 
       # グラフの描画
       plt.bar(x, y, tick_label=x,
              align="center", color = "c") # 棒グラフの描画
 
def draw_piechart(x, y, c):
       """ 円グラフを表示する関数
       引数：
       x -- x軸の値
       y -- y軸の値
       c -- 指定色
       """
       # グラフの装飾
       plt.title("Sales by Product",
              fontsize = 12) # タイトル
       plt.rcParams['font.size'] = 12.0 # ラベルのフォント
 
       # グラフの描画
       plt.pie(y, labels=x, counterclock=True,
              autopct="%1.1f%%", colors=c) # 円グラフの描画
 
# データ準備
product_nm = np.array(["Co", "Dr", "Ra",
              "TV", "Ws"]) # 製品名の格納
sales = np.array([124, 60, 70, 133, 12]) # 売上の格納
pie_colors = ["r", "c", "b", "m", "y"] # 製品毎の色指定
 
# グラフの描画
plt.figure(figsize=(12, 8)) # (1)描画領域を指定
plt.subplots_adjust(wspace=0.6, hspace=0.6) # (2)間隔指定
 
plt.subplot(2, 3, 1) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)
 
plt.subplot(2, 3, 2) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)

plt.subplot(2, 3, 3) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)
 
plt.subplot(2, 3, 4) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)

plt.subplot(2, 3, 5) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)

plt.subplot(2, 3, 6) # (3)グラフ描画位置の指定
draw_barchart(product_nm, sales)

plt.savefig("hello.png")
