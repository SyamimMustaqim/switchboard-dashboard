import django_tables2 as tables
from graph.models import DataTerminal

class SwitchTable(tables.Table):
    class Meta:
        model = DataTerminal

class AlertTable(tables.Table):
    id = tables.Column(verbose_name='No')
    switch_lable = tables.Column(verbose_name='Switch Lable')
    alert_type = tables.Column(verbose_name='Alert Type')
    unix_timestamp = tables.Column(verbose_name='Timestamp')

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'id',
            'switch_lable',
            'alert_type',
            'unix_timestamp'
            )

class ReportTable(tables.Table):
    switch_lable = tables.Column(verbose_name='Switch Lable')
    terminal_1 = tables.Column(verbose_name='Terminal 1 (P1)')
    terminal_2 = tables.Column(verbose_name='Terminal 2 (P2)')
    terminal_3 = tables.Column(verbose_name='Terminal 3 (P3)')
    terminal_4 = tables.Column(verbose_name='Terminal 4 (P4)')
    terminal_5 = tables.Column(verbose_name='Terminal 5 (P5)')
    unix_timestamp = tables.Column(verbose_name='Timestamp')

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'switch_lable',
            'terminal_1',
            'terminal_2',
            'terminal_3',
            'terminal_4',
            'terminal_5',
            'unix_timestamp'
            )