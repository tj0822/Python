task = db.Task()
task.title = request.form['title']
task.text = request.form['text']
task.save()