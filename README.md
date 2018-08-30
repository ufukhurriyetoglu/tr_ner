# tr_ner

Veri Sözlükleri:

- name_list.txt : İsim sözlüğüdür.
- city_list.txt : Yer sözlüğüdür. 

Api terminal çağrısı:

api input json formatı:  {'text':'input'}
output: {[entity,label], [entity,label]} 

curl sorgusu
------------

* Çift tırnak öncesinde \ kullanmak gerekiyor. Metin içerisindeki tek tırnak için çözüm olarak bunu buldum. 

curl -X POST http://localhost:5000/api/v1/ner -d "{\"text\": \"Ali bugün İstanbul'un Ataşehir ilçesinde kurulan pazara gitti\"}" -H "Content-Type: application/json"

output:
--------

{
  "output": [
    [
      "Ali", 
      "ISIM"
    ], 
    [
      "\u0130stanbul", 
      "YER"
    ], 
    [
      "Ata\u015fehir", 
      "YER"
    ]
  ]
}
