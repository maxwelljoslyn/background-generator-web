from .__init__ import allowed_classes, classes, abilities
import textwrap


resetter = """hx-post="/validate" hx-target="#wholepage" hx-swap=outerHTML"""


def render_form(rolls, assignments, chosen_class):
    stringrolls = ", ".join([str(r) for r in rolls])
    if not stringrolls:
        stringrolls = "none"

    return textwrap.dedent(
        f"""
    <form id=wholepage action="" method="get" hx-include="#wholepage">

    Unassigned rolls: {stringrolls}.

    {render_abilities(rolls, assignments)}

    {render_classes(assignments, chosen_class)}

    <button formaction=deleteall type=button>Delete All</button>

    </form>
    """
    )


def render_classes(assignments, chosen_class):
    if not assignments:
        assignments = {}
    result = ["""<fieldset id="choose-class"><legend>Choose Class</legend>"""]
    ac = allowed_classes(assignments)
    for c in sorted(ac.keys()):
        result.append(render_class(c, ac[c], chosen_class, assignments))
    result.append("</fieldset>")
    return "".join(result)


def render_class(c, minimums, chosen_class, assignments):
    chosen = "checked" if c == chosen_class else ""
    result = []
    allowed = "" if all(minimums.values()) else "disabled"
    result.append(
        f"""<label><input type=radio id=choose-class-{c} name={c} value={c} {chosen} {allowed} {resetter}></input>{c}</label>"""
    )
    result.append("<p>Minimums:</p>")

    def render_minimum(abi, good):
        status = "color: green;" if good else "color: red;"
        return (
            f"<span style='{status}'>{abi} {classes[c]['ability minimums'][abi]}</span>"
        )

    mins = ", ".join([render_minimum(abi, good) for abi, good in minimums.items()])
    result.append(mins)
    return "<p>" + "".join(result) + "</p>"


def render_abilities(rolls, assignments):
    result = ["""<fieldset id="assign-scores"><legend>Assign Ability Scores</legend>"""]
    for a in sorted(list(abilities)):
        result.append(render_ability(a, rolls, assignments))
    result.append("</fieldset>")
    return "".join(result)


def render_ability(abi, rolls, assignments=None):
    if not assignments:
        assignments = {}
    if abi in assignments:
        return f"<span>{abi.title()} {assignments[abi]} <button type=button>Undo</button></span>"
    else:
        rolls.sort()
        result = [f"{abi.title()}"]
        for r in rolls:
            result.append(f"<label>{r}")
            foo = f"""<input type=radio id=choose-{abi}-{r} name={abi} value={r} {resetter}></input>"""
            result.append(foo)
            result.append("</label>")
        return "<p>" + "".join(result) + "</p>"
