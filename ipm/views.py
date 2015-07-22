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
            if 1 == i: row['begintime'] = r[i]
            if 2 == i: row['endtime'] = r[i]
            if 3 == i: row['server_ip'] = r[i]
            if 4 == i: row['client_ip'] = r[i]
            if 5 == i: row['delay'] = r[i]
            if i > 5: row['bus_tag_' + str(i - 6)] = r[i]
        btmlist.append(row)
        
    return render(request, 'list.html', {'btmlist': btmlist})

def found_tags(request):
    found_taglist = None
    with open('/data/btm_found_tags') as f:
        found_taglist = f.readlines()
    print found_taglist
    return render(request, 'found_tags.html', {'found_taglist': found_taglist})
