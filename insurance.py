import csv

#Importar las columnas a listas individuales para mejor analisis
age=[]
sex=[]
bmi=[]
children=[]
smoker=[]
regions=[]
charges=[]


def extract_insurance(lista, documento, columna):
    with open(documento, newline="") as insurance_data:
       data=csv.DictReader(insurance_data)
       for row in data:
           lista.append(row[columna])
       return lista

#llenar los columnas con los datos 
extract_insurance(age, "insurance.csv", "age")
extract_insurance(sex, "insurance.csv", "sex")
extract_insurance(bmi, "insurance.csv", "bmi")
extract_insurance(children, "insurance.csv", "children")
extract_insurance(smoker, "insurance.csv", "smoker")
extract_insurance(regions, "insurance.csv", "region")
extract_insurance(charges, "insurance.csv", "charges")

#Extraer informacion del dataset

rows=0

for row in age:
    rows+=1

print(f"There are {rows} rows  in this dataset")

#Numero de hombres y mujeres
hombres=0
mujeres=0

for row in sex:
    if row=="male":
        hombres+=1
    elif row=="female":
        mujeres+=1
porcent_men=round((hombres*100)/rows,2)
porcent_women=round((mujeres*100)/rows,2)
print(f"there are a total of {hombres} men and a total of {mujeres} women in this dataset")
print(f"this represent a total of {porcent_men} % and {porcent_women} % respectively")
#total de la poblacion que es fumadora

fumadores=0
no_fumadores=0

for row in smoker:
    if row=="yes":
        fumadores+=1
    elif row=="no":
        no_fumadores+=1

porcent_smokers=round((fumadores*100)/rows,2)
porcent_no_smokers=round((no_fumadores*100)/rows,2)
print(f"the total of fumadores represent the {porcent_smokers} % of the population")

#encontrar relacion de fumadores por genero

fumadores_genero=list(zip(smoker,sex))
fumadores_mujeres=0
fumadores_hombres=0


for i in fumadores_genero:
    if i[0]=="yes" and i[1]=="female":
        fumadores_mujeres+=1
    elif i[0]=="yes" and i[1]=="male":
        fumadores_hombres+=1

porcentaje_fumadores_hombre=round((fumadores_hombres*100)/hombres,2)
porcentaje_fumadores_mujeres=round((fumadores_mujeres*100)/mujeres,2)
print(f"The total of population of men and women who smoke are {porcentaje_fumadores_hombre} % {porcentaje_fumadores_mujeres} % respectively")

total_costs=[]
for cost in charges:
    total_costs.append(float(cost))
max_cost=round(max(total_costs),2)
print(max_cost)

    

#Tratar de calcular el costo promedio de fumadores y no fumadores
cargos_y_fumadores=list(zip(smoker, charges))
cargo_por_fumadores=[]
cargo_no_fumadores=[]

for i in cargos_y_fumadores:
    if i[0]=="yes":
        cargo_por_fumadores.append(float(i[1]))
    else:
        cargo_no_fumadores.append(float(i[1]))


#esta funcion es muy util la debi haber definido antes 
def calcular_promedio(list):
    return round(sum(list)/len(list),2)



promedio_fumadores=calcular_promedio(cargo_por_fumadores)
promedio_nofumadores=calcular_promedio(cargo_no_fumadores)
print(f"el cargo promedio de un seguro a personas que fuman es de {promedio_fumadores}, mientras que el costo promedio si uno no es fumador es de {promedio_nofumadores}")

#Determinar edad promedio 
edades_int=[]
for i in age:
    edades_int.append(int(i))

edad_promedio=calcular_promedio(edades_int)

print(f"la edad promedio de los pacientes es de {edad_promedio} años")


#Econtrar de donde viene la mayoria de personas 
for i in set(regions):
    numero_region=regions.count(i)
    print(i, numero_region)

costes_por_region=list(zip(regions, charges))
Promedio_sw=[]
promedio_nw=[]
promedio_se=[]
promedio_ne=[]

for i in costes_por_region:
    if i[0]=="southwest":
        Promedio_sw.append(float(i[1]))
    elif i[0]=="northwest":
        promedio_nw.append(float(i[1]))
    elif i[0]=="southeast":
        promedio_se.append(float(i[1]))
    else:
        promedio_ne.append(float(i[1]))


total_promedio_sw=calcular_promedio(Promedio_sw)
total_promedio_nw=calcular_promedio(promedio_nw)
total_promedio_se=calcular_promedio(promedio_se)
total_promedio_ne=calcular_promedio(promedio_ne)

