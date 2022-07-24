from datetime import datetime
from flask import Flask, render_template, abort, jsonify, request, redirect, url_for

from model import db, save_db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        bookmarks=db
    )


@app.route("/bookmark/<int:index>")
def bookmark_view(index):
    try:
        bookmark = db[index]
        return render_template("bookmark.html",
                               bookmark=bookmark,
                               index=index,
                               max_index=len(db)-1)
    except IndexError:
        abort(404)


@app.route('/add_bookmark', methods=["GET", "POST"])
def add_bookmark():
    if request.method == "POST":
        bookmark = {"bookmarktitle": request.form['bookmarktitle'],
                    "bookmarkurl": request.form['bookmarkurl'],
                    "category": request.form['category'],
                    "subcategory": request.form['subcategory'],
                    "bookmarkdesc": request.form['bookmarkdesc']}
        db.append(bookmark)
        save_db()
        return redirect(url_for('bookmark_view', index=len(db)-1))
    else:
        return render_template("add_bookmark.html")


# @app.route('/edit_bookmark/<int:index>', methods=["GET", "POST"])
# def edit_bookmark(index):
#     try:
#         if request.method == "POST":
#             bookmark=db[index]
#              = {"bookmarktitle": request.form['bookmarktitle'],
#                         "bookmarkurl": request.form['bookmarkurl'],
#                         "category": request.form['category'],
#                         "subcategory": request.form['subcategory'],
#                         "bookmarkdesc": request.form['bookmarkdesc']}
#             db.append
#             save_db()
#             return render_template("bookmark_view.html", bookmark=db[index])
#         else:
#             return render_template("edit_bookmark.html", bookmark=db[index])
#     except IndexError:
#         abort(404)


@app.route('/remove_bookmark/<int:index>', methods=["GET", "POST"])
def remove_bookmark(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_bookmark.html", bookmark=db[index])
    except IndexError:
        abort(404)


@app.route("/api/bookmark/")
def api_bookmark_list():
    return jsonify(db)


@app.route('/api/bookmark/<int:index>')
def api_bookmark_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)






# @app.route("/date")
# def date():
#     return "This page was served at " + str(datetime.now())
#
#
# counter = 0
#
#
# @app.route("/count_views")
# def count_views():
#     global counter
#     counter += 1
#     return "this page was served " + str(counter) + " times"