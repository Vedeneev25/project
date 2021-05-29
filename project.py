
import openpyxl
import cv2
import pytesseract
img = cv2.imread('photo.png')
#text = pytesseract.image_to_string(img)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#config = r'--oem 3 --psm 6
#cv2.imshow('Result', img)
#cv2.waitKey(0)

#Открытие файла с себестоимотсью
wb_obj = openpyxl.load_workbook("cena.xlsx")
sheet_obj = wb_obj.active
#Открытие файла с фактической стоимостью
wb_obj1 = openpyxl.load_workbook("fact.xlsx")
sheet_obj1 = wb_obj1.active
# списки для определения категорий
napitki = ['cola','fanta','water1','water2','water3','coffee1','coffee2','coffee3','sprite', 'вода', 'кола', 'сок']
food = ['sandwich','cookie','laysbig','layssmall','чипсы','сэндвич','печенье']
coffee = ['капучино','латте','раф']
cola = [ 'cola' , 'coke' , 'cocacola','кола','кокакола','колаж/б0,5']
# спросим у пользователя значение наценки которое он считает критичным
krit = input("какое значение наценки в процентах для вас критично?").replace(' ', '')
kritlist=list(krit)
vvv=''
for i, letter in enumerate(kritlist):
    if letter in '0123456789':
        vvv = vvv + str(letter)
    else:
        i = i + 1
        
big = float(vvv)

i=1
j=1
n=(sheet_obj.max_row) 
b=(sheet_obj1.max_row)
n = n + 1
b = b + 1

srednap=0
ssrednap = 0
sch = 0

sredfood = 0
ssredfood = 0
schfood = 0

sred_coffee = 0
ssred_coffee = 0
sch_coffee = 0

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
        if d > big:
            print('наценка на товар ' + str(tovar.value) + ' равна ' + str(d) )
        if tovar.value in napitki:
            srednap = srednap + d
            sch = sch + 1
            i = 1
            j = j + 1
        elif tovar.value in food:
             sredfood = sredfood + d
             schfood = schfood + 1
             i = 1
             j = j + 1
        elif tovar.value in coffee:
             sred_coffee = sred_coffee + d
             sch_coffee = sch_coffee + 1
             i = 1
             j = j + 1
        else:
            i = 1
            j = j + 1
    else:
        i = i + 1
ssrednap = srednap / sch
ssredfood = sredfood / schfood
ssred_coffee = sred_coffee / sch_coffee
print('средняя наценка на напитки составляет ' + str(ssrednap))
print('средняя наценка на еду составляет ' + str(ssredfood))
print('средняя наценка на кофе составляет ' + str(ssred_coffee))








