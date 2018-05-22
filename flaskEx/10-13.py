import pysolr

solr = pysolr.Solr("http://localhost:8983/solr/jpub_kr", timeout=30)
solr.delete(q="id:10")