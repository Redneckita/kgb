from kgb import settings as settings

REPLACE_STRINGS = [
    ("^1","")
    ,("^2","")
    ,("^3","")
    ,("^4","")
    ,("^5","")
    ,("^6","")
    ,("^7","")
    ,("<","&lt;")
    ,(">","&gt;")
    ,("syntax is ","")
]

level = -1
html = ''
for command, command_prop in sorted(settings.COMMANDS.items(), key=lambda (k, v): v['min_level']):

    if level != command_prop['min_level']:
        level = command_prop['min_level']
        html += "</table><hr /><table><tr><td colspan=\"4\"><b>Commands level %s</b></td></tr>" % (command_prop['min_level'])
        html += "<tr><td><b>Command</b></td><td><b>Command abbreviation</b></td><td><b>Syntax</b></td><td><b>Description</b></td></tr>"

    for s, r in REPLACE_STRINGS:
        command_prop['syntax'] = command_prop['syntax'].replace(s,r)
    html += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (command_prop['command'], command_prop['command_slug'], command_prop['syntax'], command_prop['description'])

html += "</table>"

print html