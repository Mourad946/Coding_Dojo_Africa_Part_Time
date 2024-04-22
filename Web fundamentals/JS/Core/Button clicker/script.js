let likes = [0, 0];

function likeDefinition(index) {
  likes[index - 1]++;
  document.getElementById('like-count-' + index).innerText = likes[index - 1];
  alert('New like added to definition ' + index + '!');
}

function addDefinition() {
  // Add functionality to add a new definition
}
