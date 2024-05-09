# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
# rəqəmlər yoxdursa -1 cavabı qaytarın. 

# Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.

class Solution:
    def index(self, list, hedef):
        indexes = [(a, b)
        for a in range(len(list))
        for b in range(a+1, len(list))
        if list[a] + list[b] == hedef]
        return indexes if indexes else -1

find_index = Solution()
myList = [1, 2, 3, 4, 5]
target = 8
print(f'hedef ededlerin indeksleri {find_index.index(myList, target)} -dur')