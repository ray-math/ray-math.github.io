---
layout: page
title: Math
permalink: /math/
main_nav: true
---

{% assign math_categories = "" | split: "" %}
{% for post in site.posts %}
  {% if post.path contains '_posts/math' %}
    {% unless math_categories contains post.categories[0] %}
      {% assign math_categories = math_categories | push: post.categories[0] %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% for category in math_categories %}
  {% assign category_posts = site.categories[category] | where_exp: "post", "post.path contains '_posts/math'" %}
  <h3 id="{{category}}">
    <a href="{{ site.baseurl }}/category/{{ category }}/">{{ category | capitalize }} ({{ site.categories[category].size }})</a>
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
