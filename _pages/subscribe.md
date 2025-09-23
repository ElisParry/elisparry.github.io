---
layout: page
title: Newsletter subscription
permalink: /subscribe
comments: false
---

<p>Enter your email below to subscribe to my newsletter. I'll send an email to any newsletter subscribers whenever I post a new blog, sometimes with additional content too!</p>

<form id="subscribe-form" action="https://formspree.io/f/mblkpglk" method="POST">
  <input class="form-control mb-2" type="email" name="_replyto" placeholder="E-mail Address*" required>
  <input type="hidden" name="form_type" value="subscribe">
  <input class="btn btn-dark" type="submit" value="Subscribe">
</form>
<div id="subscribe-thankyou" style="display:none;">
  <p>Thank you for subscribing! You'll hear from me soon.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var form = document.getElementById('subscribe-form');
  var thankyou = document.getElementById('subscribe-thankyou');
  if(form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var data = new FormData(form);
      fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { 'Accept': 'application/json' }
      }).then(function(response) {
        if (response.ok) {
          form.style.display = 'none';
          thankyou.style.display = 'block';
        } else {
          alert('There was a problem. Please try again later.');
        }
      }).catch(function() {
        alert('There was a problem. Please try again later.');
      });
    });
  }
});
</script>