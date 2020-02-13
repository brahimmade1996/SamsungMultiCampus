html = """
<html>
   <head>
      <meta charset="utf-8">
   </head>
"""


print(html)
a = 135
for i in str(a) :
   print(f"<img src=../images/{i}.png width=40 >")




html = """
   <body>
       <font color=red> 한글 </font>
   </body>
"""
print(html)


print("</html>")