---
layout: page
title: Project joyrun.
permalink: /joyrun
comments: false
image: 
imageshadow: true
---

<div style="text-align:center;">
  <img src="{{ site.baseurl }}/assets/images/joyrun_logo_new.png" alt="JoyRun Logo" style="max-width:420px; width:100%; height:auto; margin:auto;">
</div>

<p>This is a new project that I am working on bringing to life. It's called joyrun. It's a project to help others (re)find joy in their running.

Please get in touch if you are interested in hearing more about the project and/or working with me during its early stages.</p>

<!-- Explore tiles: uses same blog-grid classes as homepage -->
## Explore

<div class="blog-grid-container" style="margin-top:18px;">

  <div class="blog-grid-item">
    <div class="card h-100">
      <div class="maxthumb">
        <a href="{{ site.baseurl }}/ideas">
          {% if site.lazyimages == "enabled" %}
            <img class="img-thumb lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{{ site.baseurl }}/assets/images/ideas.png" alt="Ideas">
          {% else %}
              <img class="img-thumb" style="width:100%;height:auto;" src="{{ site.baseurl }}/assets/images/ideas.png" alt="Ideas">
          {% endif %}
        </a>
      </div>
      <div class="card-body">
        <h4 class="card-text">{{ "Ideas to help you re-find joy in your running." | strip_html | truncatewords:30 }}</h4>
      </div>
      <div class="card-footer bg-white">
        <div class="wrapfooter">
          <div class="clearfix"></div>
        </div>
      </div>
    </div>
  </div>

  <div class="blog-grid-item">
    <div class="card h-100">
      <div class="maxthumb">
        <a href="{{ site.baseurl }}/recipes">
          {% if site.lazyimages == "enabled" %}
            <img class="img-thumb lazyimg" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAACCAQAAAA3fa6RAAAADklEQVR42mNkAANGCAUAACMAA2w/AMgAAAAASUVORK5CYII=" data-src="{{ site.baseurl }}/assets/images/recipes.png" alt="Recipes">
          {% else %}
              <img class="img-thumb" style="width:100%;height:auto;" src="{{ site.baseurl }}/assets/images/recipes.png" alt="Recipes">
          {% endif %}
        </a>
      </div>
      <div class="card-body">
        <h4 class="card-text">{{ "No-junk fuel for the long run - both during your runs and the rest of your life." | strip_html | truncatewords:30 }}</h4>
      </div>
      <div class="card-footer bg-white">
        <div class="wrapfooter">
          <div class="clearfix"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Add more tiles here using the same blog-grid-item/card structure -->
</div>

