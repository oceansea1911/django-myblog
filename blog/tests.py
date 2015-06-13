from views import * 

# Create your tests here.
id = 1
comments = getComment(id)
for comment in comments:
	if comment:
		for element in comment:
				print element.content
