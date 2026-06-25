---
title: About
permalink: /
---

{%- assign cv = site.data.cv -%}

<p class="page-eyebrow">About</p>

{{ cv.bio | markdownify }}

<ul class="taglist">
  {%- for ri in cv.research_interests %}
  <li class="tag">{{ ri }}</li>
  {%- endfor %}
</ul>

<h2>Education</h2>
{%- for e in cv.education %}
  {%- if e.todo %}
<p class="todo">TODO — {{ e.note }}</p>
  {%- else %}
<div class="entry">
  <div class="entry__head">
    <span class="entry__title">{{ e.degree }}</span>
    <span class="entry__date">{{ e.dates }}</span>
  </div>
  <div class="entry__sub">{{ e.institution }}{% if e.location %} · {{ e.location }}{% endif %}</div>
  {%- if e.note %}<div class="entry__note">{{ e.note }}</div>{% endif %}
  {%- if e.gpa %}<div class="entry__note">{{ e.gpa }}</div>{% endif %}
  {%- if e.honors %}<div class="entry__note"><strong>{{ e.honors }}</strong></div>{% endif %}
</div>
  {%- endif %}
{%- endfor %}

<h2>Experience</h2>
{%- for x in cv.experience %}
<div class="entry">
  <div class="entry__head">
    <span class="entry__title">{{ x.title }}</span>
    <span class="entry__date">{{ x.dates }}</span>
  </div>
  <div class="entry__sub">{{ x.organization }}{% if x.location %} · {{ x.location }}{% endif %}</div>
  {%- if x.note %}<div class="entry__note">{{ x.note }}</div>{% endif %}
</div>
{%- endfor %}

<h2>Publications</h2>
{%- for pub in site.data.publications %}
{% include publication.html pub=pub compact=true %}
{%- endfor %}
<p style="margin-top:1rem;"><a href="{{ '/publications/' | relative_url }}">All publications &rarr;</a></p>

<h2>Patents</h2>
{%- for pt in cv.patents %}
<div class="entry">
  <div class="entry__title">{{ pt.title_en }}</div>
  <div class="entry__sub" lang="ko">{{ pt.title_kr }}</div>
  <div class="entry__sub">Inventors:
    {%- for inv in pt.inventors %} {% if inv.me %}<strong>{{ inv.name }}</strong>{% else %}{{ inv.name }}{% endif %}{% unless forloop.last %},{% endunless %}{% endfor %}
  </div>
  <div class="entry__note">{{ pt.status }}{% if pt.assignee %} · Assignee: {{ pt.assignee }}{% endif %}</div>
  <div class="entry__note">
    {%- for f in pt.filings %}{{ f.kind }}: {{ f.number }} ({{ f.date }}){% unless forloop.last %} · {% endunless %}{% endfor %}
  </div>
</div>
{%- endfor %}

<h2>Awards &amp; Honors</h2>
{%- for a in cv.awards %}
  {%- if a.todo %}
<p class="todo">TODO — {{ a.note }}</p>
  {%- else %}
<div class="entry">
  <div class="entry__head">
    <span class="entry__title">{{ a.title }}</span>
    <span class="entry__date">{{ a.date }}</span>
  </div>
  {%- if a.note %}<div class="entry__sub">{{ a.note }}</div>{% endif %}
</div>
  {%- endif %}
{%- endfor %}
