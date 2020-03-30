import flask
import json
app = flask.Flask(__name__)


@app.route("/")
def index():
    user = flask.request.values.get("user") if "user" in flask.request.values else ""
    pwd = flask.request.values.get("pwd") if "pwd" in flask.request.values else ""
    if user == "xyz" and pwd =="123":
       # return flask.redirect("/user")
       return flask.render_template("phone.html")
    else:
       # return flask.render_template("phone.html")
       return flask.render_template("user.html")

@app.route("/phones")
def getPhones():
    mark = flask.request.values.get("mark")
    phones = []
    if mark == "华为":
        phones.append({"model":"p9","mark":"华为","price":3900})
        phones.append({"model":"p10","mark":"华为","price":4898})
    elif mark == "苹果":
        phones.append({"model":"I9","mark":"苹果","price":8000})
        phones.append({"model":"I10","mark":"苹果","price":4898})
    elif mark == "三星":
        phones.append({"model":"p9","mark":"三星","price":3990})

    s = json.dumps({"phones":phones})
    return s

@app.route("/show")
def show():
    return "server message"

@app.route("/user", methods=['GET','POST'])
def user():
    st = "<table border='1'>"
    st += "<tr><td>品牌</td><td>型号</td><td>价格</td></tr>"
    st += "<tr><td>1</td><td>xxx</td><td>123</td></tr>"
    st += "<tr><td>2</td><td>sss</td><td>534</td></tr>"
    st += "</table>"
    st += "<a href='/'>退出</a>"
    return st

@app.route("/down")
def download():
    with open("END_ALL _SPIDER/images/1.jpg","rb") as f:
        data = f.read()
    return data

if __name__ == "__main__":
    app.run()
