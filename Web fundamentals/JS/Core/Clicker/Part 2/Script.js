<script>
// Select the "likes-count" element and the "like-button" element
const likesCountElement = document.querySelector('#likes-count');
const likeButtonElement = document.querySelector('#like-button');

// Define a function to increase the number of likes by 1
function increaseLikes() {
  // Get the current number of likes
  const currentLikes = parseInt(likesCountElement.textContent);

  // Increment the number of likes
  likesCountElement.textContent = currentLikes + 1;
}

// Add an event listener to the "like-button" element to call the increaseLikes function when clicked
likeButtonElement.addEventListener('click', increaseLikes);
</script>