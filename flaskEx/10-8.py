import pysolr

solr = pysolr.Solr("http://localhost:8983/solr/jpub_kr", timeout=30)
search_obj = solr.search("CGI")
for record in search_obj:
    # record에 대한 처리