html = """
<html>
   <head>
      <meta charset="utf-8">
   </head>

   <body>
       <font color=red> @out</font>
       <table borker = 2>
            <tr>
                <td> 이름</td> <td> @name </td>
            </tr>
            <tr>
                <td> e-mail</td> <td> @email </td>
            </tr>
              
   </body>
</html>
"""

html = html.replace("@out",  "제목출력")
html = html.replace("@name",  "이순신")
html = html.replace("@email",  "lee@gmail.com")


print(html)