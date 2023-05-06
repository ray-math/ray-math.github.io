---
layout: page
title: Memo
permalink: /memo/
main_nav: true
---

{% assign target_categories = "essay,money,study" | split: "," %}

{% for category in target_categories %}
  {% assign category_posts = site.categories[category] %}
  {% if category_posts.size > 0 %}
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
  {% endif %}
{% endfor %}
<br>
