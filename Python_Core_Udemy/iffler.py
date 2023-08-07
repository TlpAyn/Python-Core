test_score= input("lutfen sonucu giriniz:  ")

if not test_score.isdigit():
    print("lutfen rakamsal bilgi giriniz")
elif int(test_score) <=100:
    test_score=int(test_score)
    if test_score >=85:
        result="pekiyi"
    elif test_score >=75:
        result="orta"
    else:
        result="kaldi"



print(result)



