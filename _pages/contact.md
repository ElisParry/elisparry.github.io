---
layout: page
title: Contact.
permalink: /contact
comments: false
---
![Running](/assets/images/email_image.avif)

<form id="contact-form" action="https://formspree.io/f/mblkpglk" method="POST">    
<p class="mb-4">Please use the form or send me an email if you would like to get in touch. I'll try to reply as soon as possible!</p>
<div class="form-group row">
<div class="col-md-6">
<input class="form-control" type="text" name="name" placeholder="Name*" required>
</div>
<div class="col-md-6">
<input class="form-control" type="email" name="_replyto" placeholder="E-mail Address*" required>
</div>
</div>
<textarea rows="8" class="form-control mb-3" name="message" placeholder="Message*" required></textarea>    
<input class="btn btn-dark" type="submit" value="Send">
</form>
<div id="contact-thankyou" style="display:none;">
  <p>Thank you for contacting me. I will get back to you soon.</p>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var form = document.getElementById('contact-form');
  var thankyou = document.getElementById('contact-thankyou');
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