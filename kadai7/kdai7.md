## 初めに

メインプログラムで取り込んだcsvファイルはリストの形式で保存しています。

## データの保存図

* Classroom

    - grade
    - class_id
    - teacher_name
	- teacher_fm
	* student_list
	    * student_id
	    * name
	    * math
	    * japanese
	    * fm

## データの取り出し方
1. 1組の名簿番号１番の名前を取り出す場合

    classroom11.student_list[0].name
		
1. ２組の学年を取り出す場合

    classroom12.grade
		
	
