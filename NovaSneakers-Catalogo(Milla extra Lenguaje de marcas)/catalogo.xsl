<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<head>
    <meta charset="utf-8"/>
    <title>Catálogo NovaSneakers</title>
    <link rel="stylesheet" href="estilos.css"/>
</head>
<body>
    <h2>Catálogo de Zapatillas</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Precio (€)</th>
            <th>Talla</th>
            <th>Stock</th>
        </tr>
        <xsl:for-each select="catalogo/producto">
            <tr>
                <td><xsl:value-of select="@id"/></td>
                <td><xsl:value-of select="marca"/></td>
                <td><xsl:value-of select="modelo"/></td>
                <td><xsl:value-of select="precio"/></td>
                <td><xsl:value-of select="talla"/></td>
                <td><xsl:value-of select="stock"/></td>
            </tr>
        </xsl:for-each>
    </table>
</body>
</html>
</xsl:template>

</xsl:stylesheet>
