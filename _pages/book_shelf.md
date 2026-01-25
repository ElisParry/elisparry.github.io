---
layout: page
title: Book shelf
permalink: /book_shelf
comments: false
image: 
imageshadow: true
---

Here are some books that I've enjoyed reading related to some of the topics discussed in my blog. Hopefully it can be a useful resource to anyone who wants to learn more about these topics.
<style>
.books-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px; /* reduced from 32px */
  justify-items: start;     /* LEFT-align items in each grid cell */
  justify-content: start;   /* align the whole grid to the left within container */
  align-items: end; /* aligns bottoms of items */
  margin-top: 32px;
  max-width: 1100px; /* keep grid from stretching too wide */
  margin-left: auto;
  margin-right: auto;
}
@media (max-width: 700px) {
  .books-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px; /* reduced from 20px */
    justify-items: start;
    justify-content: start;
    align-items: end;
  }
}
.book-item {
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: flex-end; /* ensures image sits at bottom */
  align-items: flex-start;    /* keep content in each cell left-aligned */
}
.book-item img {
  width: 120px;
  border-radius: 8px;
  display: block;
}
.books-grid + h1,
  .books-grid + h2 {
    margin-top: 48px;
  }
@media (max-width: 700px) {
    .books-grid + h1,
    .books-grid + h2 {
      margin-top: 28px;
    }
  }
</style>

# Running

<div class="books-grid">
  <div class="book-item">
    <img src="/assets/images/Books/feet_in_clouds.jpg" alt="Feet in Clouds book">
  </div>
  <div class="book-item">
    <img src="/assets/images/Books/born_to_run.jpeg" alt="Born to Run book">
  </div>
  <div class="book-item">
    <img src="/assets/images/Books/ultramarathon_man.jpg" alt="Ultramarathon Man book">
  </div>
  <div class="book-item">
    <img src="/assets/images/Books/running_up_hill.jpg" alt="Running up That Hill">
  </div>
  <div class="book-item">
    <img src="/assets/images/Books/endurance_handbook.webp" alt="The Endurance Handbook">
  </div>
  <div class="book-item">
    <img src="/assets/images/Books/skyrunner.webp" alt="Skyrunner">
  </div>
</div>

# Life

<div class="books-grid">
  <div class="book-item">
    <img src="/assets/images/Books/can_the_mind_be_quiet.jpg" alt="Can The Mind Be Quiet?">
  </div>
</div>

# Climate

<div class="books-grid">
  <div class="book-item">
    <img src="/assets/images/Books/changes_everything.jpg" alt="This Changes Everything">
  </div>
</div>


Note: Book covers are displayed here for informational purposes only. I do not own the rights to these images. All rights remain with the respective authors and publishers.