---
layout: page
title: Memo
permalink: /memo/
main_nav: true
---

{% assign memo_categories = "" | split: "" %}
{% for post in site.posts %}
  {% if post.path contains '_posts/memo' %}
    {% unless memo_categories contains post.categories[0] %}
      {% assign memo_categories = memo_categories | push: post.categories[0] %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% for category in memo_categories %}
  {% assign category_posts = site.categories[category] | where_exp: "post", "post.path contains '_posts/memo'" %}
  <h3 id="{{cat}}">
    <a href="{{ site.baseurl }}/category/{{ category }}/">{{ cat | capitalize }} ({{ site.categories[category].size }})</a>
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
