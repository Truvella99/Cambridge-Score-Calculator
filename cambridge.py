min_points = {"reading":24,"uoe":18,"listening":18,"writing":24,"speaking":36}
max_points = {"reading":42,"uoe":28,"listening":30,"writing":40,"speaking":60}
max_time = {"reading_uoe":75,"listening":40,"writing":80}
reading_use_of_english_weights = {1:1,2:1,3:1,4:2,5:2,6:2,7:1}

def stampa(score,min,max,time=0,max_time=0):
    text = str(score) + " punti, su un massimo di " + str(max) + " punti" + " e un minimo di " + str(min) + " punti"
    if(score<min):
        text+= "\tInsufficiente"
    else:
        text+= "\tB2"
    if(time!=0 and max_time!=0):
        text+= " Completato in " + str(time) + " minuti su un massimo di " + str(max_time) + " minuti"
    return text

reading,use_of_english,listening,writing,speaking = 0,0,0,0,0
points = [reading,use_of_english,listening,writing,speaking]
time_reading_uoe,time_listening,time_writing = 0,0,0
time = [time_reading_uoe,time_listening,time_writing]

for part,weight in reading_use_of_english_weights.items():
    if part==1 or part==5 or part==6 or part==7:
        points[0]+= weight * int(input("Inserire il Punteggio Reading & Use of English parte " + str(part) + ":\n"))
    else:
        points[1] += weight * int(input("Inserire il Punteggio Reading & Use of English parte " + str(part) + ":\n"))

time[0] = int(input("Inserire il tempo (in minuti) impiegato per la parte di Reading & Use of English:\n"))

for i in range(1,5):
    points[2]+= int(input("Inserire il Punteggio Listening parte " + str(i) + ":\n"))

time[1] = int(input("Inserire il tempo (in minuti) impiegato per la parte di Listening:\n"))

for i in range(1,3):
    points[3]+= int(input("Inserire il Punteggio Writing parte " + str(i) + ":\n"))

time[2] = int(input("Inserire il tempo (in minuti) impiegato per la parte di Writing:\n"))

points[4]+= int(input("Inserire il Punteggio Speaking:\n"))

print("\nPunteggio Finale:\n")
print("Reading:\t\t" + stampa(points[0],min_points.get("reading"),max_points.get("reading")))
print("Use of English: " + stampa(points[1],min_points.get("uoe"),max_points.get("uoe")))
print("Reading & Use of English:\t" + stampa(points[0]+points[1],min_points.get("reading")+min_points.get("uoe"),max_points.get("reading")+max_points.get("uoe"),time[0],max_time.get("reading_uoe")))
print("Listening:\t\t" + stampa(points[2],min_points.get("listening"),max_points.get("listening"),time[1],max_time.get("listening")))
print("Writing:\t\t" + stampa(points[3],min_points.get("writing"),max_points.get("writing"),time[2],max_time.get("writing")))
print("Speaking:\t\t" + stampa(points[4],min_points.get("speaking"),max_points.get("speaking")))

print("\nCalcolo Percentuali...")

percentage = []
i,total,avg = 0,0,0

for max in max_points.values():
    percentage.append((points[i]/max)*100)
    i+=1

for element in percentage:
    total+=element

avg = int(total / len(percentage))

print("Percentuale da Convertire in Cambridge English Score (contando tutto, >=160 per il B2): " + str(avg) + " %")
print("https://kseacademy.com/cambridge/how-calculate-score-cambridge-exam/#how-to-calculate-the-score-for-b2-first-fce")