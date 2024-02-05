import csv
import os


def function_ret_carac(obj_ler_arquivo):
    lista_nova = []
    for linha in obj_ler_arquivo:
        line_rem_carac = linha.rstrip()
        line_rem_subs = line_rem_carac.replace('"', '')
        line_divid = line_rem_subs.split(',')
        lista_nova.append(line_divid)
    del lista_nova[0]
    return lista_nova

### 1 parte####
# Recebe arquivo csv para leitura
tabelaAreas = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\Tabela Areas.csv"
arquivo_Area = open(tabelaAreas, 'r')
lista_tab_Area = []
lista_tab_Area = function_ret_carac(arquivo_Area)

for i in lista_tab_Area:
    del i[1]

lista_id=[]
for i in lista_tab_Area:
   lista_id.append(i[0])

lista_id_1=[]
for i in lista_id:
   if i not in lista_id_1:
       lista_id_1.append(i)

lista_Area_fil=[]
for i in lista_id_1:
    for j in lista_tab_Area:
        if i == j[0]:
           lista_Area_fil.append(j)
           break

### 3 parte####
# Recebe arquivo csv para leitura
tabelaNOS = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\PontosCSV_L-mod.csv"
arquivo_Nos = open(tabelaNOS, 'r')
lista_tab_Nos = []
lista_tab_Nos = function_ret_carac(arquivo_Nos)
# Remove coluna 0 e 1
for i in lista_tab_Nos:
    del i[0]
    del i[1]

### 2 parte####
# Recebe arquivo csv para leitura
tabelaEscoa = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\Pontos Escoamento.csv"
arquivo_Escoa = open(tabelaEscoa, 'r')
lista_tab_Escoa = []
lista_tab_Escoa = function_ret_carac(arquivo_Escoa)
lista_id_escoa=[]
for i in lista_tab_Escoa:
    lista_id_escoa.append(i[0])

lista_id_escoa_1=[]
for i in lista_id_escoa:
    if i not in lista_id_escoa_1:
        lista_id_escoa_1.append(i)

lista_tab_Escoa_1=[]
for i in lista_id_escoa_1:
   for j in lista_tab_Escoa:
       if i == j[0]:
           lista_tab_Escoa_1.append(j)
           break


#print(len(lista_tab_Escoa_1))
lista_no_esc=[]
for i in lista_tab_Escoa_1:
    for j in lista_tab_Nos:
        if i[1]==j[1] and i[2]==j[2]:
            var_no_esc=str(j[0])
    var_tot=str(i[0])+" "+str(var_no_esc)
    var_tot=var_tot.split()
    lista_no_esc.append(var_tot)

lista_tot_AN=[]
for i in lista_Area_fil:
   for j in lista_no_esc:
       if i[0]==j[0]:
           var0=str(j[0])+" "+str(j[1])+" "+str(i[1])
           var0=var0.split()
           lista_tot_AN.append(var0)

"""for i in lista_tot_AN:
    print(i)
"""
##############################
def function_ret(obj_ler_arquivo):
    lista_nova = []
    for linha in obj_ler_arquivo:
        line_rem_carac = linha.rstrip()
        line_rem_subs = line_rem_carac.replace('"', '')
        line_rem_subs = line_rem_carac.replace('\t', '  ')
        line_divid = line_rem_subs.split()
        lista_nova.append(line_divid)
    del lista_nova[0]
    return lista_nova
tabelaAreas1 = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\Gerar_arq_IC_Funcionam\Txts\Bacia_E_COEFs.txt"
arquivo_Area1 = open(tabelaAreas1, 'r',encoding="utf8")
lista_tab_Area_1 = []
lista_tab_Area_1 = function_ret(arquivo_Area1)

"""for i in lista_tab_Area_1:
    print(i)
"""
new_list_01=[]
for i in lista_tot_AN:
    for j in lista_tab_Area_1:
      if i[0]==j[0]:    
       var_a1=str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(j[1])+" "+str(j[2])+" "+str(j[3])
       var_a1=var_a1.split()        
       new_list_01.append(var_a1)
#########################
"""for i in new_list_01:
    print(i)
"""
var_escreve_file = '\n[SUBCATCHMENTS]\n'
for i in new_list_01:
    var_escreve_file += f's_{i[0]}\t1\t{i[1]}\t{i[2]}\t{i[3]}\t500\t0.5\t0\n'

var_escreve_file += '\n[SUBAREAS]\n'
for i in new_list_01:
    var_escreve_file += f's_{i[0]}\t{i[4]}\t{i[5]}\t0.05\t0.05\t25\tOUTLET\n'

var_escreve_file += '\n[INFILTRATION]\n'
for i in new_list_01:
    var_escreve_file += f's_{i[0]}\t3.5\t0.5\t0.25\n'

### 3 parte####
# Recebe arquivo csv para leitura
tabelaNOS = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\PontosCSV_L-mod.csv"
arquivo_Nos = open(tabelaNOS, 'r')
lista_nos = []
lista_nos = function_ret_carac(arquivo_Nos)

for i in lista_nos:
    del i[0]

var_escreve_file += '\n[JUNCTIONS]\n'
for i in lista_nos:
    var_escreve_file += f'{i[0]}\t{i[1]}\t1.25\t0\t0\t0\n'



### 5 parte####
# Recebe arquivo csv para leitura
tabelaTrechos = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\TrechoCSV-mod.csv"
arquivo_Trechos = open(tabelaTrechos, 'r')
lista_trechos = []
lista_trechos = function_ret_carac(arquivo_Trechos)

for i in lista_trechos:
    del i[0]

'''for i in lista_trechos:
   print(i)'''

var_nosX=str(0)
var_nosY=str(0)

lista_trechos_1=[]
for i in lista_trechos:
    for j in lista_nos:
        if i[1]==j[2] and i[2]==j[3]:
              var_nosX=str(j[0])
              #var_nosX=var_nosX.split()
        if i[3]==j[2] and i[4]==j[3]:
              var_nosY=str(j[0])
    var_nosZ=str(i[0])+" "+var_nosX+" "+var_nosY+" "+str(i[5])
    var_nosZ=var_nosZ.split()
    lista_trechos_1.append(var_nosZ)

"""for i in lista_trechos_1:
   print(i)
"""
var_escreve_file += '\n[CONDUITS]\n'
for i in lista_trechos_1:
    var_escreve_file += f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t0.01\t0\t0\t0\t0\n'

var_escreve_file += '\n[XSECTIONS]\n'
for i in lista_trechos_1:
    var_escreve_file += f'{i[0]}\tRECT_OPEN\t1\t10\t0\t0\t1\n'

var_escreve_file += '\n[COORDINATES]\n'
for i in lista_nos:
    var_escreve_file += f'{i[0]}\t{i[2]}\t{i[3]}\n'    

pontosDesenho = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\desenho_subBacia.csv"
manipulador3 = open(pontosDesenho, 'r')
desenho_subBacia = []
for l in manipulador3:
    l_strip = l.strip()
    l_limpo = l_strip.replace('"', '')
    l_dividido = l_limpo.split(',')
    desenho_subBacia.append(l_dividido)
del desenho_subBacia[0]

nomes_das_subBacias = []
for i in desenho_subBacia:
    if (not (i[0] in nomes_das_subBacias)):
        nomes_das_subBacias.append(i[0])

ordem_para_desenho = []
temp = []
cont = 0
for n in nomes_das_subBacias:
    for i in desenho_subBacia:
        if (i[0] == n):
            temp.append(i[:])

    while (len(temp) > 0):
        for i in temp:
            if (i[1] == str(cont)):  # a segunda coluna contem a ordem correta para fazer o desenho
                ordem_para_desenho.append(i[:])
                del temp[(temp.index(i))]
                # print(temp)
        cont += 1
    temp.clear()
    cont = 0
var_escreve_file += '\n[Polygons]\n'
for i in ordem_para_desenho:
    var_escreve_file += f's_{i[0]}\t{i[2]}\t{i[3]}\n'

diretorio_aq_swmm = r"C:\Users\leona\OneDrive\Área de Trabalho\IC_UFSJ\ANEW_PROJ\Bacias_ren_210623_swmm.txt"
arquivo_SWMM = open(diretorio_aq_swmm, 'w')
arquivo_SWMM.write(var_escreve_file)
arquivo_SWMM.close()