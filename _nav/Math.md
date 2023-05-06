---
layout: page
title: Math
permalink: /math/
main_nav: true
---

{% assign target_categories = "algebra,analysis" | split: "," %}

{% for category_name in target_categories %}
  {% assign category_posts = site.categories[category_name] %}
  <h3 id="{{category_name}}">
    <a href="{{ site.baseurl }}/category/{{ category_name }}/">{{ category_name }} ({{ site.categories[category_name].size }})</a>
  </h3>
  <ul class="posts-list">
  {% for post in category_posts limit:4 %}
    <li>
      <strong>
        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </strong>
      <span class="post-date">- {{ post.date | date_to_long_string }}</span>
    </li>
  {% endfor %}
  </ul>
  {% if forloop.last == false %}<hr>{% endif %}
{% endfor %}
<br>
