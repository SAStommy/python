# 111-1 師大科技系程式語言
>**這裡記錄我在111-1 師大科技系程式語言的課程的筆記,作業以及專題**


# 目錄  
>+ [**1. 課程介紹** ](https://github.com/SAStommy/python#課程介紹)
>+ [**2. 自我介紹**](https://github.com/SAStommy/python#自我介紹)
>+ [**3. 課程筆記區**](https://github.com/SAStommy/python#課程筆記區)
>+ [**4. 作業連結區**](https://github.com/SAStommy/python#作業連結區)
>+ [**5. 專題連結區**](https://github.com/SAStommy/python#專題連結區)
---

# 課程介紹
**授課老師 :**

蔡芸琤老師
  
**內容 :** 
1. 教授python的使用方法
2. 以作業和專題訓練實作能力
3. 教授python在資料分析中的應用並實作

# 自我介紹
**姓名**：杜洺鋒\
**學校**：國立臺灣師範大學\
**系級**：科技系二年級\
**E-mail**：mingfungto@gmail.com

# 課程筆記區
>+ [**Week 1**](https://github.com/SAStommy/python#Week-1)
>+ [**Week 2**](https://github.com/SAStommy/python#Week-2)
>+ [**Week 3**](https://github.com/SAStommy/python#Week-3)
>+ [**Week 4**](https://github.com/SAStommy/python#Week-4)
>+ [**Week 5**](https://github.com/SAStommy/python#Week-5)
>+ **Week 6**
>+ **Week 7**
>+ **Week 8**
>+ **Week 9**
>+ **Week 10**
>+ **Week 11**
>+ **Week 12**
>+ **Week 13**
>+ **Week 14**
>+ **Week 15**
>+ **Week 16**
---

# 作業連結區
>+ [**HW 1 : csv資料比對**](https://github.com/SAStommy/python/blob/main/hw01%E8%B3%87%E6%96%99%E5%B0%8D%E6%AF%94.ipynb)
>+ [**HW 2 : json處理**](https://github.com/SAStommy/python/blob/main/hw02%20json%E8%99%95%E7%90%86.ipynb)\
> **因為資料太大不方便在github顯示**\
> **付上顯示連結** : <https://nbviewer.org/github/SAStommy/python/blob/main/hw02%20json%E8%99%95%E7%90%86.ipynb>\
> **檔案連結** : <https://drive.google.com/file/d/19OO1c8tCbG9VG9dRvl7fRSTgzo0g7IcC/view?usp=sharing>
>+ [**HW 3 : 爬蟲**](https://github.com/SAStommy/python/blob/main/hw03%20%E7%88%AC%E8%9F%B2.ipynb)\
> **如果沒法顯示,請到連結** : <https://nbviewer.org/github/SAStommy/python/blob/main/hw03%20%E7%88%AC%E8%9F%B2.ipynb>\
> **產生的json檔** : [**sv.json**](https://github.com/SAStommy/python/blob/main/sv.json)\
> **產生的csv檔** : [**sv.csv**](https://github.com/SAStommy/python/blob/main/sv.csv)\
> **注:json檔請在打開後按[view raw]查看,因為文件太大**
>+ [**HW 4 : 文字探勘**](https://medium.com/@mingfungto/d8729f9128d2?source=friends_link&sk=acd0c89bcf9afa487e3efc7572c2137f)\
> [**程式碼**](https://github.com/SAStommy/python/blob/main/%E6%96%87%E5%AD%97%E6%8E%A2%E5%8B%98.ipynb)\
> **如果沒法顯示,請到連結** : <https://nbviewer.org/github/SAStommy/python/blob/main/%E6%96%87%E5%AD%97%E6%8E%A2%E5%8B%98.ipynb>
>+ [**HW 5 : 共現分析**](https://medium.com/@mingfungto/%E6%95%99%E5%AD%B8-%E6%96%87%E5%AD%97%E6%8E%A2%E5%A0%AA%E8%88%87%E5%85%B1%E7%8F%BE%E6%80%A7%E5%88%86%E6%9E%90-fd2eb4e6239d)\
> [**程式碼**](https://github.com/SAStommy/python/blob/main/hw05%20%E5%85%B1%E7%8F%BE%E6%80%A7%E5%88%86%E6%9E%90.ipynb)
---

# 專題連結區
>+ [**專題**](https://youtu.be/wUO0I5zkwqI)
---

# Week 1
+ 課程介紹

[回目錄](https://github.com/SAStommy/python#目錄)

# Week 2
+ 資料形態
  + int(整數)
  + float(小數)
  + bool(布林值) : 判定True or False
+ 初步暖身
  + [mini task 1](https://github.com/SAStommy/python/blob/main/mini%20task%201.ipynb)
+ 練習題
  + [1.行車糾紛](https://github.com/SAStommy/python/blob/main/week2%20%E7%B7%B4%E7%BF%92%E9%A1%8C%201-checkpoint.ipynb)
  + [2.償還債務](https://github.com/SAStommy/python/blob/main/week2%20%E7%B7%B4%E7%BF%92%E9%A1%8C%202.ipynb)
  + [3.行車糾紛判定](https://github.com/SAStommy/python/blob/main/week2%20%E7%B7%B4%E7%BF%92%E9%A1%8C%203.ipynb)
  
[回目錄](https://github.com/SAStommy/python#目錄)

# Week 3

+ **list(變數['a','b'.'c'])**
  + 變數[start:end] : 取從start剄end
  + 變數[:n] : 取前n名
  + 變數[:-n] : 取前n名,不取後n項
  + 變數[n:] : 取n項到最後
  + 變數[-n:] : 不取前n名,取後n項
  + 變數[:] : 取所有元素
  + 變數[start : end : step] : 每隔step從start到end
  
  [回目錄](https://github.com/SAStommy/python#目錄)

# Week 4

+ **dict**

[回目錄](https://github.com/SAStommy/python#目錄)

# Week 5
