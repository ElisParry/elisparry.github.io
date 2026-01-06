---
layout: page
title: Contact.
permalink: /contact
comments: false
---

<img src="/assets/images/email_image.avif" alt="Running" style="border-radius: 12pt;">


<form id="contact-form" action="https://formspree.io/f/mblkpglk" method="POST" novalidate target="_self">
  <p class="mb-4">Please use the form or send me an email if you would like to get in touch. I'll try to reply as soon as possible!</p>
  <div class="form-group row">
    <div class="col-md-6">
      <input class="form-control" type="text" name="name" placeholder="Name*" required style="border:none;border-bottom:2px solid #333;border-radius:0;background:transparent;box-shadow:none;max-width:100%;margin-bottom:8px;">
    </div>
    <div class="col-md-6">
      <input class="form-control" type="email" name="_replyto" placeholder="E-mail Address*" required style="border:none;border-bottom:2px solid #333;border-radius:0;background:transparent;box-shadow:none;max-width:100%;margin-bottom:8px;">
    </div>
  </div>
  <textarea rows="8" class="form-control mb-3" name="message" placeholder="Message*" required style ="border-radius:12px;"></textarea>
  <input class="btn btn-dark" type="submit" value="Send" style="border-radius:12px;">
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
      return false; // Extra insurance for mobile browsers
    }, false);
  }
});
</script>

<style>
/* two-column layout: text left, image right, vertically centered */
.two-col {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 12px;
}
.two-col .text {
  flex: 1;
  min-width: 0;
}
.cv-pic {
  width: 220px;
  max-width: 35%;
  border-radius: 12px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.12);
  display: block;
}
@media (max-width: 700px) {
  .two-col { flex-direction: column; align-items: center; text-align: center; }
  .cv-pic { max-width: 60%; margin-top: 12px; }
}
</style>

