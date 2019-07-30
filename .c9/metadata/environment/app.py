{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\napp.config[\"MONGO_DBNAME\"] = 'task_manager'\napp.config[\"MONGO_URI\"] = 'mongodb+srv://ananya:password5@myfirstcluster-nesmd.mongodb.net/task_manager?retryWrites=true&w=majority'\n\nmongo = PyMongo(app)\n\n@app.route('/')\n@app.route('/get_tasks')\ndef hello():\n    return render_template(\"tasks.html\", tasks=mongo.db.tasks.find())\n\n@app.route('/add_task')\ndef add_task():\n    return render_template('addtask.html')\n\nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)","undoManager":{"mark":95,"position":100,"stack":[[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["a"],"id":88},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["p"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["p"]}],[{"start":{"row":12,"column":15},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":90}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"],"id":91},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."],"id":92},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["o"],"id":93},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["r"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["."]},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":["p"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":["p"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"remove","lines":["a"]},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["@"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"],"id":94},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"]}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"],"id":95},{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["p"],"id":96}],[{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"],"id":97},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["()"],"id":98}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":13},"action":"insert","lines":["''"],"id":99}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["/"],"id":100},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["g"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["e"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["_"],"id":101},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["t"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["a"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["s"]},{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"remove","lines":["s"],"id":102}],[{"start":{"row":13,"column":20},"end":{"row":13,"column":21},"action":"insert","lines":["k"],"id":103},{"start":{"row":13,"column":21},"end":{"row":13,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":[","],"id":104}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":[" "],"id":105},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["r"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["n"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["d"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["e"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":[" "],"id":106}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":[" "],"id":107}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["_"],"id":108},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":["t"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["e"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["m"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["p"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["a"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["t"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["e"],"id":109},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["t"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":["a"]}],[{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["l"],"id":110},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["a"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["t"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":42},"action":"insert","lines":["()"],"id":111}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":42},"action":"remove","lines":["()"],"id":112}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"insert","lines":[","],"id":113}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[" "],"id":114}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":["r"],"id":115},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["e"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["d"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["i"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["r"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["e"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["c"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[","],"id":116}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":[" "],"id":117},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["e"],"id":118},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["q"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["u"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["e"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["s"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"insert","lines":["t"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"insert","lines":[","]}],[{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"insert","lines":[" "],"id":119},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"insert","lines":["u"]},{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"insert","lines":["r"]},{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"insert","lines":["l"]},{"start":{"row":1,"column":64},"end":{"row":1,"column":65},"action":"insert","lines":["_"]},{"start":{"row":1,"column":65},"end":{"row":1,"column":66},"action":"insert","lines":["f"]},{"start":{"row":1,"column":66},"end":{"row":1,"column":67},"action":"insert","lines":["o"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":33},"action":"remove","lines":["Hello World ...again'"],"id":120},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["'"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["r"],"id":121},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["d"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["e"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["_"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["t"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["e"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["m"]}],[{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["p"],"id":122},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["a"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["k"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["k"],"id":123},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["a"]}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["l"],"id":124},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["a"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["t"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":28},"action":"insert","lines":["()"],"id":125}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":29},"action":"insert","lines":["\"\""],"id":126}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["t"],"id":127},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["a"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["s"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["k"]},{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":15,"column":33},"end":{"row":15,"column":34},"action":"insert","lines":["."],"id":128},{"start":{"row":15,"column":34},"end":{"row":15,"column":35},"action":"insert","lines":["h"]},{"start":{"row":15,"column":35},"end":{"row":15,"column":36},"action":"insert","lines":["t"]},{"start":{"row":15,"column":36},"end":{"row":15,"column":37},"action":"insert","lines":["m"]},{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":39},"end":{"row":15,"column":40},"action":"insert","lines":[","],"id":129}],[{"start":{"row":15,"column":40},"end":{"row":15,"column":41},"action":"insert","lines":[" "],"id":130}],[{"start":{"row":15,"column":41},"end":{"row":15,"column":42},"action":"insert","lines":["t"],"id":131},{"start":{"row":15,"column":42},"end":{"row":15,"column":43},"action":"insert","lines":["a"]},{"start":{"row":15,"column":43},"end":{"row":15,"column":44},"action":"insert","lines":["s"]},{"start":{"row":15,"column":44},"end":{"row":15,"column":45},"action":"insert","lines":["k"]},{"start":{"row":15,"column":45},"end":{"row":15,"column":46},"action":"insert","lines":["s"]},{"start":{"row":15,"column":46},"end":{"row":15,"column":47},"action":"insert","lines":["="]},{"start":{"row":15,"column":47},"end":{"row":15,"column":48},"action":"insert","lines":["m"]},{"start":{"row":15,"column":48},"end":{"row":15,"column":49},"action":"insert","lines":["o"]},{"start":{"row":15,"column":49},"end":{"row":15,"column":50},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":50},"end":{"row":15,"column":51},"action":"insert","lines":["g"],"id":132},{"start":{"row":15,"column":51},"end":{"row":15,"column":52},"action":"insert","lines":["o"]}],[{"start":{"row":15,"column":52},"end":{"row":15,"column":53},"action":"insert","lines":["."],"id":133},{"start":{"row":15,"column":53},"end":{"row":15,"column":54},"action":"insert","lines":["d"]},{"start":{"row":15,"column":54},"end":{"row":15,"column":55},"action":"insert","lines":["b"]},{"start":{"row":15,"column":55},"end":{"row":15,"column":56},"action":"insert","lines":["."]},{"start":{"row":15,"column":56},"end":{"row":15,"column":57},"action":"insert","lines":["t"]},{"start":{"row":15,"column":57},"end":{"row":15,"column":58},"action":"insert","lines":["a"]},{"start":{"row":15,"column":58},"end":{"row":15,"column":59},"action":"insert","lines":["s"]},{"start":{"row":15,"column":59},"end":{"row":15,"column":60},"action":"insert","lines":["k"]}],[{"start":{"row":15,"column":60},"end":{"row":15,"column":61},"action":"insert","lines":["s"],"id":134}],[{"start":{"row":15,"column":61},"end":{"row":15,"column":62},"action":"insert","lines":["."],"id":135},{"start":{"row":15,"column":62},"end":{"row":15,"column":63},"action":"insert","lines":["f"]},{"start":{"row":15,"column":63},"end":{"row":15,"column":64},"action":"insert","lines":["i"]},{"start":{"row":15,"column":64},"end":{"row":15,"column":65},"action":"insert","lines":["n"]},{"start":{"row":15,"column":65},"end":{"row":15,"column":66},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":66},"end":{"row":15,"column":68},"action":"insert","lines":["()"],"id":136}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":47},"action":"remove","lines":["ananya"],"id":137},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["r"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["o"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["o"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"remove","lines":["t"],"id":138},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"remove","lines":["o"]},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"remove","lines":["o"]},{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"remove","lines":["r"]}],[{"start":{"row":8,"column":41},"end":{"row":8,"column":42},"action":"insert","lines":["a"],"id":139},{"start":{"row":8,"column":42},"end":{"row":8,"column":43},"action":"insert","lines":["n"]},{"start":{"row":8,"column":43},"end":{"row":8,"column":44},"action":"insert","lines":["a"]},{"start":{"row":8,"column":44},"end":{"row":8,"column":45},"action":"insert","lines":["n"]},{"start":{"row":8,"column":45},"end":{"row":8,"column":46},"action":"insert","lines":["y"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"remove","lines":["2"],"id":140},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["7"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":137},"action":"remove","lines":["mongodb+srv://ananya:17codzitswall05@myfirstcluster-nesmd.mongodb.net/task_manager?retryWrites=true&w=majority"],"id":141}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":124},"action":"insert","lines":["mongodb+srv://ananya:<password>@myfirstcluster-nesmd.mongodb.net/test?retryWrites=true&w=majority"],"id":142}],[{"start":{"row":8,"column":49},"end":{"row":8,"column":57},"action":"remove","lines":["password"],"id":143},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["1"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["7"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["c"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["o"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["d"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["z"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["i"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["t"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["w"],"id":144},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["a"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["l"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["l"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["0"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["5"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["<"],"id":145}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":[">"],"id":146}],[{"start":{"row":8,"column":97},"end":{"row":8,"column":101},"action":"remove","lines":["test"],"id":147},{"start":{"row":8,"column":97},"end":{"row":8,"column":98},"action":"insert","lines":["t"]},{"start":{"row":8,"column":98},"end":{"row":8,"column":99},"action":"insert","lines":["a"]},{"start":{"row":8,"column":99},"end":{"row":8,"column":100},"action":"insert","lines":["s"]},{"start":{"row":8,"column":100},"end":{"row":8,"column":101},"action":"insert","lines":["k"]},{"start":{"row":8,"column":101},"end":{"row":8,"column":102},"action":"insert","lines":["_"]},{"start":{"row":8,"column":102},"end":{"row":8,"column":103},"action":"insert","lines":["m"]},{"start":{"row":8,"column":103},"end":{"row":8,"column":104},"action":"insert","lines":["a"]},{"start":{"row":8,"column":104},"end":{"row":8,"column":105},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":105},"end":{"row":8,"column":106},"action":"insert","lines":["a"],"id":148},{"start":{"row":8,"column":106},"end":{"row":8,"column":107},"action":"insert","lines":["g"]},{"start":{"row":8,"column":107},"end":{"row":8,"column":108},"action":"insert","lines":["e"]},{"start":{"row":8,"column":108},"end":{"row":8,"column":109},"action":"insert","lines":["r"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":63},"action":"remove","lines":["17codzitswall05"],"id":149},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["<"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["P"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["A"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["S"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["S"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["W"]}],[{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["O"],"id":150},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["R"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["D"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":[">"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":58},"action":"remove","lines":["<PASSWORD>"],"id":151},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["1"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["7"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["c"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["o"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["d"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["z"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["i"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["t"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["s"]},{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["w"]}],[{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["a"],"id":152},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["l"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["l"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["0"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["5"]},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["!"]}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":["!"],"id":153}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":["@"],"id":154},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"remove","lines":["a"],"id":155},{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"remove","lines":["@"]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":156},{"start":{"row":17,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["@"]},{"start":{"row":17,"column":1},"end":{"row":17,"column":2},"action":"insert","lines":["a"]},{"start":{"row":17,"column":2},"end":{"row":17,"column":3},"action":"insert","lines":["p"]},{"start":{"row":17,"column":3},"end":{"row":17,"column":4},"action":"insert","lines":["p"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["."]}],[{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"],"id":157},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["o"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["u"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["t"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["("],"id":158},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":[")"]}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":[")"],"id":159}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["\""],"id":160}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["\""],"id":161}],[{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["'"],"id":162},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["'"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":[")"]}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["/"],"id":163},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["a"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["d"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["d"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["_"]}],[{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["t"],"id":164},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["a"]},{"start":{"row":17,"column":19},"end":{"row":17,"column":20},"action":"insert","lines":["s"]},{"start":{"row":17,"column":20},"end":{"row":17,"column":21},"action":"insert","lines":["k"]}],[{"start":{"row":17,"column":23},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":165},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["d"]},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["e"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":[" "],"id":166},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["a"]},{"start":{"row":18,"column":5},"end":{"row":18,"column":6},"action":"insert","lines":["d"]},{"start":{"row":18,"column":6},"end":{"row":18,"column":7},"action":"insert","lines":["d"]}],[{"start":{"row":18,"column":4},"end":{"row":18,"column":7},"action":"remove","lines":["add"],"id":167},{"start":{"row":18,"column":4},"end":{"row":18,"column":12},"action":"insert","lines":["add_task"]}],[{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["("],"id":168},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":[")"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":[":"]}],[{"start":{"row":18,"column":15},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":169}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "],"id":170}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["r"],"id":171},{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"]},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["u"]},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["t"],"id":172},{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["u"]}],[{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["t"],"id":173},{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["u"]},{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["r"]},{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":[" "],"id":174}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":[" "],"id":175}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":[" "],"id":176},{"start":{"row":19,"column":11},"end":{"row":19,"column":12},"action":"insert","lines":["r"]},{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["e"]},{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["n"]},{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["d"]},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["e"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["_"],"id":177},{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":["t"]},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["e"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["m"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["p"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["l"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["a"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["t"]},{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["("],"id":178},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":[")"]}],[{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["'"],"id":179},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["a"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["d"]},{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":["d"]},{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":["t"]},{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"insert","lines":["a"]},{"start":{"row":19,"column":33},"end":{"row":19,"column":34},"action":"insert","lines":["s"]},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"insert","lines":["k"]}],[{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["."],"id":180},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["h"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["t"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["m"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["l"]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["'"]}],[{"start":{"row":17,"column":0},"end":{"row":19,"column":42},"action":"remove","lines":["@app.route('/add_task')","def add_task():","    return render_template('addtask.html')"],"id":181},{"start":{"row":17,"column":0},"end":{"row":19,"column":42},"action":"insert","lines":["@app.route('/add_task')","def add_task():","    return render_template('addtask.html')"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":63},"action":"remove","lines":["17codzitswall05"],"id":185},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["P"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["A"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["S"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["S"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["W"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["O"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["R"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["D"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":56},"action":"remove","lines":["PASSWORD"],"id":186},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["1"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["7"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["c"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["o"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["d"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["z"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["i"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["t"]},{"start":{"row":8,"column":56},"end":{"row":8,"column":57},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":57},"end":{"row":8,"column":58},"action":"insert","lines":["w"],"id":187},{"start":{"row":8,"column":58},"end":{"row":8,"column":59},"action":"insert","lines":["a"]},{"start":{"row":8,"column":59},"end":{"row":8,"column":60},"action":"insert","lines":["l"]},{"start":{"row":8,"column":60},"end":{"row":8,"column":61},"action":"insert","lines":["l"]},{"start":{"row":8,"column":61},"end":{"row":8,"column":62},"action":"insert","lines":["0"]},{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":["5"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":62},"action":"remove","lines":["17codzitswall0"],"id":188},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["p"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["p"],"id":189}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["p"],"id":190},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["a"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["d"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["d"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["w"]}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"remove","lines":["w"],"id":191},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"remove","lines":["d"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"remove","lines":["d"]}],[{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["s"],"id":192},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["s"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["w"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["o"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["r"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["d"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":56},"end":{"row":8,"column":56},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564502581500}