#!/usr/bin/env python3
# coding=utf-8
import bottle

app = bottle.Bottle()

userTable = {
    "aiifabbf": "12345",
}

@app.get("/")
def index():
    return bottle.static_file("index.html", root=".")

@app.post("/")
def signIn():
    user = bottle.request.forms.get("session[username_or_email]")
    passwd = bottle.request.forms.get("session[password]")
    if userTable.get(user, "guest") == passwd:
        bottle.redirect("/home" % user)
    redirect("/")

@app.get("/<path:path>")
def getFile(path):
    return bottle.static_file(path, root=".")

@app.get("/<user>")
def getUserPage(user):
    return

@app.get("/home")
def getHomePage():
    return bottle.static_file("home.html", root=".")

if __name__ == "__main__":
    app.run(host="", port=80, reloader=True)