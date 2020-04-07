def update():
    import json
    from Data import get
    from sendMsg import send
    import mysql.connector

    mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '1234',
            database = 'corona'
        )
    cur = mydb.cursor()
    data = get()
    f = json.load(open('data2.txt', 'r'))

    for (item2, item) in zip(f, data):
        if((item[2] != item2[2]) or (item[3] != item2[3])):
            update = item[0]

            print(update)
            s = f'select phone from Countries where country = {update}'
            try:
                cur.execute(s)
                results = cur.fetchall()
                for result in results:
                    msg = f'*{item[1]}*\n\t\t\t\tConfirmed: {item[2]}\n\t\t\t\tDeaths: {item[3]}'
                    print(result[0], msg)
                    send(result[0], msg)
                    with open("info.log", "a") as myfile:
                        myfile.write("\n" + result[0])
                        myfile.write("\n" + msg)
            except(Exception):
                pass
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

# update()


import time
starttime=time.time()
while True:
    update()
    print("tick")
    interval = 20
    time.sleep(interval - ((time.time() - starttime) % interval))