# django-class-based-todo #

## 專案介紹 ##

本專案使用5個Django Class-based Views類別導向的檢視函式(ListView、CreateView、UpdateView、DeleteView及DetailView)，來開發具有CRUD功能的待辦清單(To Do List)，藉此與函式導向的檢視函式寫法比較，來瞭解其中的不同及使用方式，可以搭配[[Django教學14]解析5個常用的Django Class-based Views使用方式](https://www.learncodewithmike.com/2020/04/django-class-based-views.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /todo (例：http://127.0.0.1:8000/todo/) 後，即可看到首頁畫面。

![Alt text](https://1.bp.blogspot.com/-T30MCv-NYjI/XqV6n0D3NoI/AAAAAAAACB0/xQqmYPFEYnYvON7bTBr7Y6tz4izdy3myQCPcBGAsYHg/s1600/django_class_based_views.PNG "Optional title")