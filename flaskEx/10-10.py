import pysolr
import datetime

solr = pysolr.Solr("http://localhost:8983/solr/jpub_kr", timeout=30)

document_ready = {'delivery_cp': 'KGB',
                  'id': 10,
                  'product_eng_description': 'This book will show you the New World.',
                  'product_name': 'Flask Web Programming',
                  'product_quantity': 1000,
                  'product_seller': 'JPUB',
                  'product_soldout': False,
                  'regdate': datetime.datetime.now()
                 }
solr.add([document_ready])