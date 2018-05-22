import pysolr

solr = pysolr.Solr("http://localhost:8983/solr/jpub_kr", timeout=30)
search_obj = solr.search("CGI")
if len(search_obj):
    for record in search_obj:
        # record에 대한 처리
else:
    print("검색 엔진이 반환한 결과가 비어있습니다.")