@app.route("/tenplusfifty_five")
def tenplusfifty_five():
    task = add_together.delay(10, 55)
    task_result = task.wait()
    return str(task_result)