#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
from http.cookies import SimpleCookie

new_blank = cgi.FieldStorage()

new_user = new_blank.getfirst("username")
new_pass = new_blank.getfirst("password")

stat_ok = new_user == username and new_pass == password

match = SimpleCookie(os.environ["HTTP_COOKIE"])
match_user = None
match_pass = None

cookie_ok = match_user == username and match_pass == password

if match.get("username"):
    match_user = match.get("username").value
if match.get("password"):
    match_pass = match.get("password").value

if cookie_ok:
    new_user = match_user
    new_pass = match_pass

print("Content-Type: text/html")

if stat_ok:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

if not new_user and not new_pass:
    print(login_page())
elif new_user == username and new_pass == password:
    print(secret_page(new_user, new_pass))
else:
    print(after_login_incorrect())



