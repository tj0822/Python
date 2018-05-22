<?xml version="1.0" encoding="utf-8"?>

<dataConfig>
    <dataSource driver="org.postgresql.Driver" url="jdbc:postgresql://localhost:5432/jpub_kr" user="jpub" password="jpub!!@#!#" />
    <document>
        <entity name="product" query="select * from product">
            <field column="product_id" name="product_id" />
            <field column="product_name" name="product_name" />
            <field column="product_seller" name="product_seller" />
            <field column="delivery_cp" name="delivery_cp" />
            <field column="product_soldout" name="product_soldout" />
            <field column="product_quantity" name="product_quantity" />
            <field column="product_eng_description" name="product_eng_description" />
            <field column="regdate" name="regdate" />
        </entity>
    </document>
</dataConfig>