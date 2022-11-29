from urllib import request
from django.views.generic import TemplateView
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django_tables2 import RequestConfig

from django.shortcuts import render
from datetime import datetime

from graph.models import DataTerminal
from .tables import ReportTable, AlertTable


class MainPageView(TemplateView):
    template_name = 'mainpage.html'

class GraphView(TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs1 = DataTerminal.objects.all().filter(switch_lable='S1')
        qs2 = DataTerminal.objects.all().filter(switch_lable='S2')
        qs3 = DataTerminal.objects.all().filter(switch_lable='S3')
        timestamp1 = []
        timestamp2 = []
        timestamp3 = []
        ping_s1 = []
        ping_s2 = []
        ping_s3 = []

        for data in qs1:
            timestamp1.append(datetime.utcfromtimestamp(data.unix_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
            if data.terminal_1 == data.terminal_2 == data.terminal_3 == data.terminal_4 == data.terminal_5 == 0:
                ping_s1.append(0)
            else:
                ping_s1.append(1)

        for data in qs2:
            timestamp2.append(datetime.utcfromtimestamp(data.unix_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
            if data.terminal_1 == data.terminal_2 == data.terminal_3 == data.terminal_4 == data.terminal_5 == 0:
                ping_s2.append(0)
            else:
                ping_s2.append(1)

        for data in qs3:
            timestamp3.append(datetime.utcfromtimestamp(data.unix_timestamp).strftime('%Y-%m-%d %H:%M:%S'))
            if data.terminal_1 == data.terminal_2 == data.terminal_3 == data.terminal_4 == data.terminal_5 == 0:
                ping_s3.append(0)
            else:
                ping_s3.append(1)

            

        context['timestamp1'] = timestamp1
        context['timestamp2'] = timestamp2
        context['timestamp3'] = timestamp3
        context['ping_s1'] = ping_s1
        context['ping_s2'] = ping_s2
        context['ping_s3'] = ping_s3
        return context

def data_table():
    table = DataTerminal.objects.all()

    return table

def table_display(request):
    list_data = []
    table = data_table()

    for data in table.values():
        list_data.append(data)

    for data in list_data:
        data['unix_timestamp'] = datetime.utcfromtimestamp(data['unix_timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    
    new_table = ReportTable(list_data)
    # table.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request).configure(new_table)
    return render(request, "tables.html", {
        "table": new_table
    })

def report_table(request):
    list_data = []
    table = data_table()

    no_id = 1
    filter_data = table.values().filter(terminal_1 = 0, terminal_2 = 0, terminal_3 = 0, terminal_4 = 0,terminal_5 = 0)

    for data in filter_data:
        data['unix_timestamp'] = datetime.utcfromtimestamp(data['unix_timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        data['id'] = no_id
        data.update({"alert_type":"Ping Lost"})
        no_id += 1
        list_data.append(data)
    
    table = AlertTable(list_data)
    RequestConfig(request).configure(table)
    return render(request, "alert_report.html", {
        "table": table
    })    