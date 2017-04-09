#!/usr/bin/python
 
import cgi, cgitb
import watsonconnect

form = cgi.FieldStorage() 
comment = form.getvalue('comment')
#if len(comment) < 100:
#    pass
    #print("Enter atleast 100 words")
watresult= watsonconnect.watsoncon(comment)
fresult="You: \n"
for (key,value) in watresult:
    if key == "values":
        for trait in value:
            if trait["name"] == "Conservation" and trait["raw_score"] > (trait["percentile"] * 0.7):
                fresult= fresult + "Emphasize self-restriction, order, and resistance to change.\n"
            elif trait["name"] == "Openness to change" and trait["raw_score"] > (trait["percentile"] * 0.7):
                fresult= fresult + "Emphasize independent action, thought, and feeling, as well as a readiness for new experiences.\n"
            elif trait["name"] == "Hedonism" and trait["raw_score"] > (trait["percentile"] * 0.7):
                fresult= fresult + "Seek pleasure and sensuous gratification for themselves.\n"
            elif trait["name"] == "Self-enhancement" and trait["raw_score"] > (trait["percentile"] * 0.7):
                fresult= fresult + "Seek personal success for themselves.\n"
            elif trait["name"] == "Self-transcendence" and trait["raw_score"] > (trait["percentile"] * 0.7):
                fresult= fresult + "Show concern for the welfare and interests of others.\n"
            else:
                pass

#print("Set-Cookie:result=%s;\r\n"%(result))

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>PersonalityHunter</title>")
print("</head>")
print("<body>")
print("<h5>%s</h5>"%(fresult))
print("</body>")
print("</html>")

