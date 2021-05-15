import os
import uuid
import sys
import json


def to_js_timestamp(ts):
    return int(ts * 1000)


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


class Chart:
    def __init__(self, type):
        self.purge()
        self.config = {}
        self.config["chart"] = {}
        self.config["chart"]["type"] = type

    def config(self, conf: dict):
        '''Accepts an dictionary containing chart configurations'''
        self.config = conf

    def set_series(self, series: list):
        '''Accepts an list of [{"name":"name", "data":[data]] , for axis charts or 
        an array of values for non-axis (pie/donut) charts '''
        self.config["series"] = series

    def set_chart(self, chart):
        self.config["chart"] = merge_two_dicts(self.config["chart"], chart)

    def set_labels(self, labels):
        self.config["labels"] = labels

    def set_xaxis(self, xaxis):
        self.config["xaxis"] = xaxis

    def set_yaxis(self, yaxis):
        self.config["yaxis"] = yaxis

    def set_theme(self, theme):
        self.config["theme"] = theme

    def set_theme(self, theme):
        self.config["theme"] = theme

    def set_data_labels(self, data_labels):
        self.config["dataLabels"] = data_labels

    def set_fill(self, fill):
        self.config["fill"] = fill

    def set_grid(self, grid):
        self.config["grid"] = grid

    def set_legend(self, legend):
        self.config["legend"] = legend

    def set_markers(self, markers):
        self.config["markers"] = markers

    def set_no_data(self, no_data):
        self.config["noData"] = no_data

    def set_plot_options(self, plot_options):
        self.config["plotOptions"] = plot_options

    def set_responsive(self, responsive):
        self.config["responsive"] = responsive

    def set_states(self, states):
        self.config["states"] = states

    def set_stroke(self, stroke):
        self.config["stroke"] = stroke

    def set_subtitle(self, subtitle):
        self.config["subtitle"] = subtitle

    def set_title(self, title):
        self.config["title"] = title

    def set_tooltip(self, tooltip):
        self.config["tooltip"] = tooltip

    def set_annotations(self, annotations):
        self.config["annotations"] = annotations

    def show(self):
        '''open html file in browser'''
        cv = str(json.dumps(self.config))
        with open("template.html", "r") as tempf:
            template = tempf.read()
            fout = template.replace("{options}", cv)

        self.filename = "html/"+str(uuid.uuid4())+".html"
        with open(self.filename, "w") as tempo:
            tempo.write(fout)
        if(sys.platform.startswith('win')):
            cmd = "start "+self.filename
        else:
            cmd = "open "+self.filename
        os.system(cmd)

    def purge(self):
        dir_name = "html/"
        test = os.listdir(dir_name)

        for item in test:
            if item.endswith(".html"):
                os.remove(os.path.join(dir_name, item))
