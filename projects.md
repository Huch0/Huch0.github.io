---
title: Projects
permalink: /projects/
---

{%- assign pj = site.data.projects -%}

<p class="page-eyebrow">Projects</p>

<p>Things I've built outside my research. Work that led to a paper is listed under
<a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>

{%- for project in pj.featured %}
{% include project.html project=project %}
{%- endfor %}

<h2>Mentoring</h2>
{%- for project in pj.mentoring %}
{% include project.html project=project %}
{%- endfor %}

<h2>Class Projects</h2>
{%- for grp in pj.class_projects %}
<div class="subfield">
  <div class="subfield__label">{{ grp.subfield }}</div>
  {%- for it in grp.items %}
  <div class="cproj">
    <div class="cproj__head">
      <span class="cproj__name">{{ it.name }}</span>
      {%- if it.course %}<span class="cproj__course">{{ it.course }}</span>{% endif %}
    </div>
    {%- if it.description %}<div class="cproj__desc">{{ it.description }}</div>{% endif %}
    {%- if it.links and it.links.size > 0 %}
    <div class="linkrow">
      {%- for l in it.links %}
        {%- if l.url contains "://" %}<a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.type }}</a>
        {%- else %}<a href="{{ l.url | relative_url }}">{{ l.type }}</a>{% endif %}
      {%- endfor %}
    </div>
    {%- endif %}
  </div>
  {%- endfor %}
</div>
{%- endfor %}
