---
title: Projects
permalink: /projects/
---

<p class="page-eyebrow">Projects</p>

<p>Selected projects outside my publication work. Research that led to a paper is listed under
<a href="{{ '/publications/' | relative_url }}">Publications</a>.</p>

{%- for project in site.data.projects %}
{% include project.html project=project %}
{%- endfor %}
