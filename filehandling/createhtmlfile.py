#Creating HTML file in Python

createfile=open('ourHtmlFile.html','w')


createfile.write("<!DOCTYPE html>"
                "\n<html>"
		        "\n<head>"
		        "\n<title>Pyhton Course</title>"
		        "\n</head>"
		        "\n<body>"
		        "\n<h2>This is Our HTML File!</h2>"
		        "\n</body>"
		        "\n</html>"
		        )
createfile.close()