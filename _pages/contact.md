---
layout: post
title: "Contact"
permalink: /contact/
comments: false
pagination: false
---

<div class="contact-page">
  <p class="contact-intro">Please use the form to get in touch. I'll try to reply as soon as possible.</p>

  <form id="contact-form" class="contact-form" action="https://formspree.io/f/mblkpglk" method="POST">
    <div class="contact-form-fields">
      <label>
        <span>Name</span>
        <input type="text" name="name" required>
      </label>
      <label>
        <span>Email address</span>
        <input type="email" name="_replyto" required>
      </label>
    </div>

    <label>
      <span>Message</span>
      <textarea name="message" rows="8" required></textarea>
    </label>

    <button type="submit">Send</button>
  </form>

  <p id="contact-thankyou" class="contact-thankyou" hidden>Thank you for contacting me. I will get back to you soon.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var form = document.getElementById('contact-form');
  var thankyou = document.getElementById('contact-thankyou');

  if (!form) return;

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    }).then(function(response) {
      if (!response.ok) throw new Error('Contact form submission failed');
      form.hidden = true;
      thankyou.hidden = false;
    }).catch(function() {
      alert('There was a problem. Please try again later.');
    });
  });
});
</script>
