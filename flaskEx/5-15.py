def _jinja2_filter_date(date):
    if isinstance(date, datetime.date):
        return date.strftime("%Y-%m-%d")
    else:
        return date