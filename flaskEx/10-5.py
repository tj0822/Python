  <!-- Legacy config for the admin interface -->
  <admin>
    <defaultQuery>*:*</defaultQuery>
  </admin>

  <!-- Dataimport Handler Define -->
  <requestHandler name="/dataimport" class="org.apache.solr.handler.dataimport.DataImportHandler">
    <lst name="defaults">
      <str name="config">./db-data-config.xml</str>
    </lst>
  </requestHandler>

</config>