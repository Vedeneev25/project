
import openpyxl
import cv2
import pytesseract
img = cv2.imread('photo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Result', img)
cv2.waitKey(0)

#Открытие файла с себестоимотсью
wb_obj = openpyxl.load_workbook("cena.xlsx")
sheet_obj = wb_obj.active
# словарь для определения категорий
napitki = ['cola','fanta','water1','water2','water3','coffee1','coffee2','coffee3','sprite']
food = ['sandwich','cookie','laysbig','layssmall']
cola = [ 'cola' , 'coke' , 'cocacola','кола','кокакола','колаж/б0,5']
#Открытие файла с фактической стоимостью
wb_obj1 = openpyxl.load_workbook("fact.xlsx")
sheet_obj1 = wb_obj1.active

i=1
j=1
n=(sheet_obj.max_row) 
b=(sheet_obj1.max_row)
n = n + 1
b = b + 1



# Определение наценки и выявление нарушений
while i < n and j<b:
    # товар с файла с сс
    tovar = sheet_obj.cell(row=j, column = 1)
    # товар с файла с фс
    tovar11 = sheet_obj1.cell(row=i, column = 1)
    
    cenaff = sheet_obj1.cell(row=i, column = 2)
    cenass = sheet_obj.cell(row=j, column = 2)
    if tovar11.value == tovar.value:
        k = cenaff.value
        l = cenass.value
        d = (k/l-1)*100
        if d > 55:
            print('себестоимотсь товара ' + str(tovar.value) + ' равна ' + str(cenass.value))
            print('цена продажи товара ' + str(tovar11.value) + ' равна ' + str(cenaff.value))      
            print('наценка на товар ' + str(tovar.value) + ' равна ' + str(d) )
            i = 1
            j = j + 1
        else:
            i = 1
            j = j + 1    
    else:
        i = i + 1
        
        









