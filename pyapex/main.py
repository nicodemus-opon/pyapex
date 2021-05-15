import os
import uuid
import sys
import json
config = {
    "chart": {
        "type": "line"
    },
    "series": [{
        "name": "sales",
        "data": [98, 40, 45, 50, 49, 60, 70, 91, 125]
    }],
    "xaxis": {
        "categories": [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    }
}
cv = str(json.dumps(config))
with open("template.html", "r") as tempf:
    template = tempf.read()
    fout = template.replace("{options}", cv)

filename = "html/"+str(uuid.uuid4())+".html"
with open(filename, "w") as tempo:
    tempo.write(fout)

if(sys.platform.startswith('win')):
    cmd = "start "+filename
else:
    cmd = "open "+filename
os.system(cmd)

def set_xxx(self, xxx):
        self.config["xxx"] = xxx