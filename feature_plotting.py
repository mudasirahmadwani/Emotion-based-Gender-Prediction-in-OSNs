import xlrd
import matplotlib.pyplot as plt

#file_location="D:\Desktop\Mudasir\Emotion Analysis (Fake vs real)\comsnet\\feature_set(fake).xlsx"

file_location="C:/Users/mudasirw/Desktop\RESEARCH @N T N U -JULY 2019/GENDER PREDICTION/New_Data-set/xlsemotion_attribues(1562 users with gender information)-experimental.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)
#arrayofvalues = sheet.col_values(11,0,720) # for real profiles
arrayofvalues = sheet.col_values(3,0)
print (arrayofvalues)

plt.boxplot(arrayofvalues)
plt.show()