---
title: Publications
permalink: /publications/
---

<p class="page-eyebrow">Publications</p>

{%- comment -%} Group by year, newest first. {%- endcomment -%}
{%- assign pubs = site.data.publications | sort: "year" | reverse -%}
{%- assign years = pubs | map: "year" | uniq -%}

{%- for y in years %}
<section class="year-group">
  <div class="year-group__label">{{ y }}</div>
  {%- for pub in pubs %}
    {%- if pub.year == y %}
{% include publication.html pub=pub %}
    {%- endif %}
  {%- endfor %}
</section>
{%- endfor %}
