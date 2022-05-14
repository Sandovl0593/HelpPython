"""Un ejemplo del uso del paquete 'calendar': 
-- Muestra configuraciones y personalizaciones del calendario, ademas
de realizar calculos de fechas en tiempo real."""
import calendar as cd
from datetime import datetime

def dayNoMondaySunday(year, month):
    "Determina los dias de la fecha sin lunes ni viernes"
    root = cd.Calendar()
    diasFalt = list(root.itermonthdays(year, month))
    alterc = False
    day= 0
    for _ in range(9):
        if alterc:
            day += 2;  diasFalt.pop(day)
        else:
            day += 3;  diasFalt.pop(day)
        alterc = not alterc
    print(diasFalt)

def lastdayFebr(year):
    "Determina el ultima dia de semana de febrero"
    root = cd.monthcalendar(year, 2)
    lastsem = root[-1]
    dia = [lastsem[i] for i in range(len(lastsem)-1, 0, -1) if lastsem[i] != 0][0]
    sem = list(cd.day_name)[lastsem.index(dia)]
    print(f"Day {sem} {dia}")

def NowDay():
    "Fecha actual"
    return list(map(int, str(datetime.today())[:10].split("-")))

def ListCalendar(mess):
    rooq = cd.Calendar()
    root = list(rooq.itermonthdates(int(NowDay()[0]), mess))
    return [str(rt).replace("datetime.date(", "").replace(")", "") for rt in root]

def dayCountBirth(mes, dia):
    "Determina los dias faltantes a la fecha de cumpleaños"
    f_actual = NowDay() # dia actual
    names = list(cd.month_name)
    distr = {}
    for mess in range(int(f_actual[1]), mes+1):
        f = ListCalendar(mess)
        newroot = []
        for fecha in f:
            fch = fecha.split("-")
            newroot.append([int(f) for f in fch[1:]])
        distr[names[mess]] = newroot

    count_days, count_mes = 0, 0
    confirm = False;  inicio = False
    for k, mm in distr.items():
        fccc = list(cd.month_name).index(k)
        for fr in mm:
            if fr[1] == f_actual[2] and fr[0] == f_actual[1]:
                inicio = True
            if inicio:
                if fr[1] == dia and fr[0] == mes:
                    confirm = True 
                    break
                elif fr[0] < fccc or fr[0] > fccc:
                    continue
                else:
                    count_days += 1
        if confirm:
            break
        count_mes += 1
        count_days = 0

    s = "s" if count_days > 1 else ""
    print(f"Te faltan {count_mes} meses y {count_days} dia{s} para cumplir un anio mas")
