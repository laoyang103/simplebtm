import time
from django.shortcuts import render
from django.db import connection,transaction
from ipm.models import bus_tags

# Create your views here.
def home(request):
    taglist = bus_tags.objects.all()
    return render(request, 'home.html', {'taglist': taglist})

def list(request):
    cursor = connection.cursor() 
    cursor.execute('show tables like \'btm_log_0%\'') 
    results = cursor.fetchall()
    for r in results: pass

    btmlist = []
    cursor.execute('select *from ' + str(r[0]) + ' order by begintime desc limit 20') 
    results = cursor.fetchall()
    for r in results: 
        row = {}
        for i in range(len(r)):
            if 1 == i: row['begintime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(r[i] + 28800))
            if 1 == i: row['endtime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(r[i] + 28800))
            if 3 == i: row['server_ip'] = r[i]
            if 4 == i: row['client_ip'] = r[i]
            if 5 == i: row['delay'] = r[i]
            if 6 == i: row['group'] = r[i]
            if i > 6: row['bus_tag_' + str(i - 7)] = r[i]
        btmlist.append(row)
        
    return render(request, 'list.html', {'btmlist': btmlist})

def search(request):
    cursor = connection.cursor() 
    cursor.execute('show tables like \'btm_log_0%\'') 
    results = cursor.fetchall()
    for r in results: pass

    btmlist = []
    group = request.GET.get('group')
    cursor.execute('select *from ' + str(r[0]) + ' where `group` = ' + group + ' order by begintime desc limit 20') 
    results = cursor.fetchall()
    for r in results: 
        row = {}
        for i in range(len(r)):
            if 1 == i: row['begintime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(r[i] + 28800))
            if 1 == i: row['endtime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(r[i] + 28800))
            if 3 == i: row['server_ip'] = r[i]
            if 4 == i: row['client_ip'] = r[i]
            if 5 == i: row['delay'] = r[i]
            if 6 == i: row['group'] = r[i]
            if i > 6: row['bus_tag_' + str(i - 7)] = r[i]
        btmlist.append(row)
        
    return render(request, 'list.html', {'btmlist': btmlist})

def found_tags(request):
    found_taglist = {}
    try: 
        with open('/tmp/btm_found_tags') as f:
            for line in f.readlines():
                if line.startswith('#'): 
                    found_taglist[line] = []
                    found_taglist['curr'] = line
                    continue
                csvlist = line.strip('\n').split(',')
                found_taglist[found_taglist['curr']].append(csvlist)
        found_taglist.pop('curr')
    except: pass
    return render(request, 'found_tags.html', {'found_taglist': found_taglist})
