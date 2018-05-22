<lib dir="${solr.install.dir:../../../..}/contrib/velocity/lib" regex=".*\.jar" />
<lib dir="${solr.install.dir:../../../..}/dist/" regex="solr-velocity-\d.*\.jar" />

<lib dir="../../../dist/" regex="solr-dataimporthandler-5.2.1.jar" />
<lib dir="../../../dist/" regex="postgresql-9.4-1201.jdbc4.jar" />

<!-- an exact 'path' can be used instead of a 'dir' to specify a 
   specific jar file.  This will cause a serious error to be logged 
   if it can't be loaded.
-->