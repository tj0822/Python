import pysolr

solr = pysolr.Solr("http://localhost:8983/solr/jpub_kr", timeout=30)
search_obj = solr.search("CGI")
first_index_document = search_obj[0]

first_index_document["product_name"] = "Short Coding"
solr.add([first_index_document])