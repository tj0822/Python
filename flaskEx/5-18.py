def _jinja2_filter_date(date, format):
    if isinstance(date, datetime.date):
        return date.strftime(format)
    else:
        return date