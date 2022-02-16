from understory import web, sql
import re
from understory.web import tx
from sqlite3 import OperationalError
from pathlib import Path
import json
from . import characters

classes = characters.classes
races = characters.races
abilities = characters.abilities

app = web.application(__name__)

try:
    db = sql.db("money.db")
except OperationalError:
    pass

tables = {
    "rolls": "score INTEGER",
    "assigned_scores": "ability TEXT, score INTEGER",
    "chosen_class": "class TEXT",
}

for table, schema in tables.items():
    try:
        db.create(table, schema)
    except OperationalError:
        pass


def get_assignments():
    with tx.db.transaction as cur:
        aa = cur.select("assigned_scores", what="*")
        print(aa)
        print(dict(aa))
        return dict(aa) if aa else {}


def get_chosen_class():
    with tx.db.transaction as cur:
        cc = cur.select("chosen_class", what="*")
        return cc if cc else None


def rolls_exist():
    with tx.db.transaction as cur:
        try:
            rolls = cur.select("rolls", what="*")
        except OperationalError:
            # shitty hack
            return []
        if rolls:
            return [r["score"] for r in rolls]
        else:
            return []


def check_minimums(abis, minimums):
    # todo this belongs in characters
    # todo put characters.abilities into a list so they have defined order
    result = {}
    for abi, mini in minimums.items():
        score = abis.get(abi, 0)
        result[abi] = True if (score and score >= mini) else False
    return result


def started():
    r = rolls_exist()
    a = get_assignments()
    if r:
        return True
    elif not r and len(a) > 0:
        return True
    else:
        return False


def allowed_classes(abis):
    """Which classes are playable given this set of abilities?
    Results of check_minimums are returned so met/unmet minimums can be surfaced to end user."""
    # todo this belongs in characters
    return {c: check_minimums(abis, classes[c]["ability minimums"]) for c in classes}


@app.wrap
def wrap(handler, app):
    """Wrap the response with data for all requests."""
    tx.host.db = sql.db("money.db")
    yield
    # HX-Request means request was triggered by HTMX
    # HTMX expects an HTML fragment, not fully rendered page
    if (
        tx.response.headers.content_type == "text/html"
        and "HX-Request" not in tx.request.headers
    ):
        tx.response.body = app.view.template(tx.response.body)


@app.control("create")
class Create:
    def get(self):
        if not started():
            raise web.SeeOther("start")
        else:
            rolls = rolls_exist()
            assignments = get_assignments()
            chosen_class = get_chosen_class()
            return app.view.create(rolls, assignments, chosen_class)


@app.control("")
class Home:
    def get(self):
        if started():
            raise web.SeeOther("create")
        else:
            raise web.SeeOther("start")


@app.control("start")
class Start:
    def get(self):
        if started():
            raise web.SeeOther("create")
        else:
            return app.view.start()

    def post(self):
        scores = [tx.request.body[f"score-{i}"] for i in range(1, 7)]
        print(scores)
        print("debug: inserting scores")
        for s in scores:
            tx.db.insert("rolls", score=s)
        raise web.SeeOther("create")


@app.control("validate")
class Validate:
    def post(self):
        from .render import render_form

        print(tx.request.headers)
        pattern = r".*\-(\w*)\-(\d+)$"
        foo = re.match(pattern, tx.request.headers["HX-trigger"])
        if foo:
            ability = foo.groups()[0]
            print(ability)
            score = foo.groups()[1]
            print(score)
            with tx.db.transaction as cur:
                cur.insert("assigned_scores", ability=ability, score=score)
                # todo how to uniquely delete? web.sql doesn't yet support LIMIT on deletes
                cur.delete("rolls", where="score = ?", vals=(score,))
            return render_form(rolls_exist(), get_assignments(), get_chosen_class())
        elif tx.request.headers["HX-trigger-name"] in classes:
            c = tx.request.headers["HX-trigger-name"]
            with tx.db.transaction as cur:
                cur.delete("chosen_class", where="class = *")
                cur.insert("chosen_class", where="class = ?", vals=(c,))
            return render_form(rolls_exist(), get_assignments(), get_chosen_class())
        else:
            return render_form(rolls_exist(), get_assignments(), get_chosen_class())


@app.control("delete-all")
class DeleteAll:
    def post(self):
        tx.db.delete("rolls")
        tx.db.delete("chosen_class")
        tx.db.delete("assigned_scores")
