---
layout: page
title: Youtube
permalink: /posts/
main_nav: true
---

{% assign youtube_categories = "" | split: "" %}
{% for post in site.posts %}
  {% if post.path contains '_posts/Youtube' %}
    {% unless youtube_categories contains post.categories[0] %}
      {% assign youtube_categories = youtube_categories | push: post.categories[0] %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% for category in youtube_categories %}
  {% assign category_posts = site.categories[category] | where_exp: "post", "post.path contains '_posts/Youtube'" %}
  <h3 id="{{category}}">
    <a href="{{ site.baseurl }}/category/{{ category }}/">{{ category }} ({{ site.categories[category].size }})</a>
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
