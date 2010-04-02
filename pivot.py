# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'.')
import xml, traceback, os, re, codecs
from xml.dom import minidom
from datetime import datetime
from deepzoom import *

testentry = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.0/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.0/"
    xmlns:atom="http://www.w3.org/2005/Atom"
>
<items>
<item>
<title>Talking with Kingsley Idehen about mastering your own search index</title>
<link>http://blog.jonudell.net/2009/09/09/talking-with-kingsley-idehen-about-mastering-your-own-search-index/</link>
<pubDate>Wed, 09 Sep 2009 14:21:49 +0000</pubDate>
<dc:creator><![CDATA[Jon Udell]]></dc:creator>

		<category><![CDATA[Uncategorized]]></category>

		<category domain="category" nicename="uncategorized"><![CDATA[Uncategorized]]></category>

		<category domain="tag"><![CDATA[goodrelations]]></category>

		<category domain="tag" nicename="goodrelations"><![CDATA[goodrelations]]></category>

		<category domain="tag"><![CDATA[kingsleyidehen]]></category>

		<category domain="tag" nicename="kingsleyidehen"><![CDATA[kingsleyidehen]]></category>

		<category domain="tag"><![CDATA[rdfa]]></category>

		<category domain="tag" nicename="rdfa"><![CDATA[rdfa]]></category>

		<category domain="tag"><![CDATA[seo]]></category>

		<category domain="tag" nicename="seo"><![CDATA[seo]]></category>

<guid isPermaLink="false">http://blog.jonudell.net/?p=1868</guid>
<description></description>
<content:encoded><![CDATA[<p>
Kingsley Idehen's vision of a web of linked data long predates the <a href="http://robots.infoworld.com/article/03/05/23/21FEinnovidehen_1.html">recognition</a> I accorded him in 2003. He's seen the big picture for a very long time, and has been driving toward it consistently. Over the years we've had <a href="http://jonudell.net/udell/2006-04-27-a-conversation-with-kingsley-idehen-about-open-source-virtuoso.html">conversations</a> in which I've always wound up saying: "Yes, OK, but how will we get people to create this web of linked data that we want to navigate and query?"
</p>
<p>
To navigate and query a web of linked data you need, obviously, mechanisms by which to do the navigation and the querying. That's never been the problem. Technologists love to figure such things out. But we've spectacularly failed to help people create that web of linked data in the first place. I don't know if the approach Kingsley Idehen sketches in this week's podcast will succeed. But it feels right, and I love his tagline: "Be the master of your own index." 
</p>
]]></content:encoded>
<excerpt:encoded><![CDATA[]]></excerpt:encoded>
<wp:post_id>1868</wp:post_id>
<wp:post_date>2009-09-09 09:21:49</wp:post_date>
<wp:post_date_gmt>2009-09-09 14:21:49</wp:post_date_gmt>
<wp:comment_status>open</wp:comment_status>
<wp:ping_status>open</wp:ping_status>
<wp:post_name>talking-with-kingsley-idehen-about-mastering-your-own-search-index</wp:post_name>
<wp:status>publish</wp:status>
<wp:post_parent>0</wp:post_parent>
<wp:menu_order>0</wp:menu_order>
<wp:post_type>post</wp:post_type>
<wp:post_password></wp:post_password>
<wp:is_sticky>0</wp:is_sticky>
<wp:postmeta>
<wp:meta_key>_edit_last</wp:meta_key>
<wp:meta_value><![CDATA[108410]]></wp:meta_value>
</wp:postmeta>
<wp:postmeta>
<wp:meta_key>_edit_lock</wp:meta_key>
<wp:meta_value><![CDATA[1269619136]]></wp:meta_value>
</wp:postmeta>
<wp:comment>
<wp:comment_id>132539</wp:comment_id>
<wp:comment_author><![CDATA[Manchester Solicitors]]></wp:comment_author>
<wp:comment_author_email>Hazarika@gmail.com</wp:comment_author_email>
<wp:comment_author_url>http://www.manchestersolicitors.org.uk</wp:comment_author_url>
<wp:comment_author_IP>94.197.54.134</wp:comment_author_IP>
<wp:comment_date>2010-03-16 03:48:27</wp:comment_date>
<wp:comment_date_gmt>2010-03-16 08:48:27</wp:comment_date_gmt>
<wp:comment_content><![CDATA[Hi vey nice interesting blog im from irland i found this on yahoo i found this blog very interesting good luck with it i will return to this blog soon]]></wp:comment_content>
<wp:comment_approved>spam</wp:comment_approved>
<wp:comment_type></wp:comment_type>
<wp:comment_parent>0</wp:comment_parent>
<wp:comment_user_id>0</wp:comment_user_id>
</wp:comment>
<wp:comment>
<wp:comment_id>130198</wp:comment_id>
<wp:comment_author><![CDATA[Healthcare Semantic Architectures &raquo; RDFa Links for Reference and Quick Intros]]></wp:comment_author>
<wp:comment_author_email></wp:comment_author_email>
<wp:comment_author_url>http://www.semanticarch.com/wordpress/?p=119</wp:comment_author_url>
<wp:comment_author_IP>69.89.31.189</wp:comment_author_IP>
<wp:comment_date>2009-09-18 16:24:32</wp:comment_date>
<wp:comment_date_gmt>2009-09-18 21:24:32</wp:comment_date_gmt>
<wp:comment_content><![CDATA[[...] Talking with Kingsley Idehen about mastering your own search index (jonudell.net)      Categories: Ontology, RDF, RDFa, Semantic Web Tags:         Comments (0) Trackbacks (0) Leave a comment Trackback [...] ]]></wp:comment_content>
<wp:comment_approved>1</wp:comment_approved>
<wp:comment_type>pingback</wp:comment_type>
<wp:comment_parent>0</wp:comment_parent>
<wp:comment_user_id>0</wp:comment_user_id>
</wp:comment>
	</item>
<item>
<title>A conversation with Allen Wirfs-Brock about the history of Smalltalk and the future of dynamic languages</title>
<link>http://blog.jonudell.net/2007/05/21/a-conversation-with-allen-wirfs-brock-about-the-history-of-smalltalk-and-the-future-of-dynamic-languages/</link>
<pubDate>Mon, 21 May 2007 15:46:57 +0000</pubDate>
<dc:creator><![CDATA[Jon Udell]]></dc:creator>
<content:encoded><![CDATA[ More than 25 years ago, Allen Wirfs-Brock created one of the early implementations of Smalltalk. He was working at Tektronix at the time, as was Ward Cunningham who became the first user of Tektronix Smalltalk. Allen later served as chief scientist of Digitalk-ParcPlace and CTO of Instantiations, then joined Microsoft four years ago. His original charter was to work on future strategies for Visual Studio, but recently -- in light of growing interest in dynamic languages at Microsot -- he's returning to his roots.

In the <a href="http://channel9.msdn.com/media/ju_wirfs-brock.mp3">latest installment</a> of my <a href="http://channel9.msdn.com/shows/Microsoft_Conversations_with_Jon_Udell">Microsoft Conversations</a> series we review the history of Smalltalk, and trace the evolution of the techniques that it (and Lisp) pioneered, from the early implementations to such modern descendants as Python and Ruby.

I'm always looking for ways to explain why dynamic programming techniques are so important, and a great explanation emerged from this conversation. A Smalltalk system is, among other things, a population of continuously evolving objects that communicate by passing messages. That same description applies to another kind of system: the Internet. I suggested -- and Allen agreed -- that this congruence is driving renewed appreciation for dynamic languages.]]></content:encoded>
<excerpt:encoded><![CDATA[]]></excerpt:encoded>
<wp:post_id>142</wp:post_id>
<wp:post_date>2007-05-21 10:46:57</wp:post_date>
<wp:post_date_gmt>2007-05-21 15:46:57</wp:post_date_gmt>
<wp:comment_status>open</wp:comment_status>
<wp:ping_status>open</wp:ping_status>
<wp:post_name>a-conversation-with-allen-wirfs-brock-about-the-history-of-smalltalk-and-the-future-of-dynamic-languages</wp:post_name>
<wp:status>publish</wp:status>
<wp:post_parent>0</wp:post_parent>
<wp:menu_order>0</wp:menu_order>
<wp:post_type>post</wp:post_type>
<wp:post_password></wp:post_password>
<wp:is_sticky>0</wp:is_sticky>
<wp:postmeta>
<wp:meta_key>enclosure</wp:meta_key>
<wp:meta_value><![CDATA[http://channel9.msdn.com/media/ju_wirfs-brock.mp3
16136443
audio/mpeg
]]></wp:meta_value>
</wp:postmeta>
<wp:comment>
<wp:comment_id>19858</wp:comment_id>
<wp:comment_author><![CDATA[nate_combs]]></wp:comment_author>
<wp:comment_author_email>ncombs@roaringshrimp.com</wp:comment_author_email>
<wp:comment_author_url>http://scratchpad.roaringshrimp.com/</wp:comment_author_url>
<wp:comment_author_IP>68.160.59.29</wp:comment_author_IP>
<wp:comment_date>2007-05-23 21:35:59</wp:comment_date>
<wp:comment_date_gmt>2007-05-24 02:35:59</wp:comment_date_gmt>
<wp:comment_content><![CDATA[&gt;Alan Kay in his excellent keynote speech at OOPSLA 1997 (video available here http://video.google.com/videoplay?docid=-2950949730059754521).

This link doesn't appear to be valid anymore.

I found a list of other presentations at:

http://www.quartopiano.com/Quartopiano/Croquet%20Project.html]]></wp:comment_content>
<wp:comment_approved>1</wp:comment_approved>
<wp:comment_type></wp:comment_type>
<wp:comment_parent>0</wp:comment_parent>
<wp:comment_user_id>0</wp:comment_user_id>
</wp:comment>
</item>
</items></rss>
"""

testentry = unicode(testentry, errors='ignore')

def _log(msg):
  print msg
  f = open('log.txt','a')
  f.write('%s\n' % msg)
  f.close()

def _trace_log():
  f = open('log.txt','a')
  traceback.print_exc(3,f)
  f.close()

class PivotItem():
  
  def __init__(self,index):
    self.index = index
    self.title = None
    self.id = None
    self.link = None
    self.date = None
    self.tags = None
    self.comments = None
    self.blurb = None

  def __repr__(self):
    return '<PivotItem>: %s, %s' % (self.title, self.date)

  def MakeJPEG(self):
   
    cmd = 'iecapt --url=%s --delay=1000 --out=tmp.jpg' % ( self.link )
    _log(cmd)
    os.system(cmd)

    cmd = 'convert -quality 100 -crop 530x500+30+180 -border 1x1 -bordercolor Black tmp.jpg %s.jpg' % self.id
    _log(cmd)
    os.system(cmd)
    
  def MakeDZI(self):

    destination = ('%s.xml' % self.id)
    source = ('%s.jpg' % self.id)
    creator = ImageCreator(tile_size=256,
                           tile_format='jpg',
                           image_quality=0.95,
                           resize_filter='antialias')
    creator.create(source, destination)

  def AsXml(self):

    item_xml = self._item_template()

    tag_elements = ''
    if len(self.tags) > 0:
      for tag in self.tags:
        tag_element = self._tag_template() % tag
        tag_elements += tag_element
      tag_elements = """<Facet Name="tag">
%s
</Facet>""" % tag_elements

    dict = {
      '__TITLE__': self.title,
      '__ID__': str(self.index),
      '__TITLE__': self.title,
      '__HREF__': self.link,
      '__DATE__': self.date,
      '__COMMENTS__': str(self.comments),
      '__DESCR__': self.blurb,
      '__TAGS__': tag_elements
      }

    for key in dict.keys():
      item_xml = item_xml.replace(key,dict[key])

    return item_xml
    
  def _tag_template(self):
    return """<String Value="%s" />"""

  def _item_template(self):
    return """<Item Id="__ID__" Img="#__ID__" Name="__TITLE__" Href="__HREF__">
<Description>__DESCR__</Description>
<Facets>
  <Facet Name="date">
    <DateTime Value="__DATE__" />
  </Facet>
__TAGS__
<!--
  <Facet Name="yearmonth">
    <String Value="__YEARMONTH__" />
  </Facet>
-->
  <Facet Name="comments">
    <Number Value="__COMMENTS__" />
  </Facet>
</Facets>
</Item>
"""


class PivotItemCollection():

  def __init__(self,wp='wp.xml',testing=False,do_images=True):

    self.wp = wp
    self.testing = testing
    self.do_images = do_images

    self.xml = None
    self.pivot_items_xml = ''
    self.images = []
    self.dzc_output = 'dzc_output'

    self.blurb_max_len = 500

    if self.testing:
      doc = minidom.parseString(testentry)
    else:
      f = codecs.open(self.wp, 'r', 'utf-8')
      xml = f.read()
      f.close()
      if xml.find('xmlns:atom="http://www.w3.org/2005/Atom"') == -1:
        xml = xml.replace('xmlns:wp="http://wordpress.org/export/1.0/"', 'xmlns:wp="http://wordpress.org/export/1.0/" xmlns:atom="http://www.w3.org/2005/Atom"')
        f = codecs.open(self.wp, 'w', 'utf-8')
        f.write(xml)
        f.close()
      doc = minidom.parse(self.wp)

    self.items = doc.getElementsByTagName('item')

  def _extractBlurb(self,content,max):
    end = min(len(content),max)
    return content[0:max] + '...'
    
  def ProcessItems(self):

    i = 0

    for item in self.items:

      _log('item %d' % i)

      try:

        title = item.getElementsByTagName('title')[0].firstChild.nodeValue
        title = title.replace('"','')
        _log('title: ' + title)

        link = item.getElementsByTagName('link')[0].firstChild.nodeValue
        _log('link: ' + link)

        if link.find('attachment_id') > -1:
          _log('skipping attachment: ' + link)
          continue

        if link.find('page_id') > -1:
          _log('skipping page: ' + link)
          continue

        id = item.getElementsByTagNameNS('http://wordpress.org/export/1.0/','post_id')[0].firstChild.nodeValue
        _log('id: ' + id)

        date = item.getElementsByTagNameNS('http://wordpress.org/export/1.0/','post_date')[0].firstChild.nodeValue[0:10] + 'T00:00:00-00:00'
        if date.startswith('0'):
          continue

        categories = item.getElementsByTagName('category')
        categories = [c for c in categories if len(c.attributes.keys()) > 0 ]
        categories = [c for c in categories if c.getAttribute('domain') == 'tag']
        nicenames = [c for c in categories if c.getAttribute('nicename') != '']
        tags = [n.getAttribute('nicename') for n in nicenames]

        comments = item.getElementsByTagNameNS('http://wordpress.org/export/1.0/','comment')
        comments = len(comments)

        content = item.getElementsByTagNameNS('http://purl.org/rss/1.0/modules/content/','encoded')[0]
        content = '<item>' + content.firstChild.nodeValue + '</item>'

        blurb = ''

        try:          
          content = minidom.parseString(content)
          paras = content.getElementsByTagName('p')
          if len(paras) > 0:
            blurb = content.getElementsByTagName('p')[0].toxml()
          else:
            _log('no paras found, using initial text')
            content = content.getElementsByTagName('item')[0].toxml()
            blurb = self._extractBlurb(content,self.blurb_max_len)
        except:
          _log('unparseable content:encoded, using initial text')
          blurb = self._extractBlurb(content,self.blurb_max_len)
  
        blurb = re.sub('<(.|\n)*?>', '', blurb)
        blurb = re.sub('&amp;', '&', blurb);
        blurb = re.sub('&quot;', '"', blurb);
     
        _log('blurb: ' + blurb)

        blurb = '<![CDATA[%s]]>' % blurb

        pivot_item = PivotItem(i)
        pivot_item.title = title
        pivot_item.link = link
        pivot_item.id = id
        pivot_item.date = date
        pivot_item.tags = tags
        pivot_item.comments = str(comments)
        pivot_item.blurb = blurb

        self.images.append('%s.xml' % id)
  
        self.pivot_items_xml += pivot_item.AsXml()

        if self.do_images: 
          pivot_item.MakeJPEG()
          pivot_item.MakeDZI()

        i += 1
        _log('-----------------------------')

      except:
        _log('error in ProcessItems at item %d ' % i)
        _trace_log()
  

  def MakeDZC(self):
    creator = CollectionCreator()
    _log('MakeDZC: %s, %s' % ( ','.join(self.images), self.dzc_output))
    creator.create(self.images, self.dzc_output)

  def AsXml(self):
    cxml = self._cxml_template()
    cxml = cxml.replace('__ITEMS__', self.pivot_items_xml)
    return cxml

  def _cxml_template(self):
     return """<?xml version="1.0" encoding="utf-8"?>
<Collection xmlns:p="http://schemas.microsoft.com/livelabs/pivot/collection/2009" SchemaVersion="1.0" Name="jon's blog" xmlns="http://schemas.microsoft.com/collection/metadata/2009">
  <FacetCategories>
    <FacetCategory Name="date" Type="DateTime" Format="d" p:IsFilterVisible="true" p:IsWordWheelVisible="false" p:IsMetaDataVisible="true" />
    <FacetCategory Name="tag" Type="String" p:IsFilterVisible="true" p:IsWordWheelVisible="true" p:IsMetaDataVisible="true" />
<!--    <FacetCategory Name="yearmonth" Type="String" p:IsFilterVisible="true" p:IsWordWheelVisible="true" p:IsMetaDataVisible="true" />-->
    <FacetCategory Name="comments" Type="Number" p:IsFilterVisible="true" p:IsWordWheelVisible="false" p:IsMetaDataVisible="true" />
  </FacetCategories>
<!--  <Items ImgBase="dzc_output.xml" HrefBase=""> -->
   <Items ImgBase="dzc_output.xml">
__ITEMS__
  </Items>
</Collection>"""


def main():
  testing = False
  do_images = True
  pivot_items = PivotItemCollection(testing=testing,do_images=do_images)
  pivot_items.items = pivot_items.items
  pivot_items.ProcessItems()
  f = codecs.open('pivot.cxml','w','utf-8')
  f.write(pivot_items.AsXml())
  f.close()
  if do_images:
    pivot_items.MakeDZC()

if __name__ == "__main__":
    main()

