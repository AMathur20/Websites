<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>

<xsl:template match="/">
  <html>
  <body>
  <h2>My Playlist</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
      	<th align="left">Track #</th>
        <th align="left">Title</th>
        <th align="left">Artist</th>
        <th align="left">Album</th>
      </tr>
      <xsl:for-each select="catalog/cd">
      <xsl:if test="artist='U2'">
      <tr>
      	<td> <xsl:value-of select="track"/> </td>
        <td> <xsl:value-of select="title"/> </td>
        <td> <xsl:value-of select="artist"/> </td>
        <td> <xsl:value-of select="album"/></td>
      </tr>
      </xsl:if>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
