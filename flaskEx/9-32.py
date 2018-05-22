return send_file(resultIO, mimetype="application/zip", as_attachment=True,
                     attachment_filename=u"result.xlsx")

@app.route("/winning_list")
def winning_list():
    winning_query = WinningEntity.query().order(WinningEntity.winning_rank).fetch()

    return render_template("winning_list.html", winning_query = winning_query)

@app.template_filter('date_format')
def datetime_convert(dt):
    format_string = "%Y-%m-%d"
    
    return dt.strftime(format_string)