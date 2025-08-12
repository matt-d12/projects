import recipes from './recipes.mjs';

const recipesSection = document.querySelector('#recipes');
const searchForm = document.querySelector('#search');

// Random number generator
function random(num) {
  return Math.floor(Math.random() * num);
}

// Pick a random entry from an array
function getRandomListEntry(list) {
  return list[random(list.length)];
}

// Generate HTML for tags
function tagsTemplate(tags) {
  return `<ul class="recipe__tags">
    ${tags.map(tag => `<li>${tag}</li>`).join('')}
  </ul>`;
}

// Generate star rating HTML with aria info
function ratingTemplate(rating) {
  let html = `<span class="rating" role="img" aria-label="Rating: ${rating} out of 5 stars">`;
  for (let i = 1; i <= 5; i++) {
    html += i <= rating
      ? `<span aria-hidden="true" class="icon-star">⭐</span>`
      : `<span aria-hidden="true" class="icon-star-empty">☆</span>`;
  }
  html += `</span>`;
  return html;
}

// Build recipe card HTML
function recipeTemplate(recipe) {
  return `<figure class="recipe">
    <img src="${recipe.image}" alt="image of ${recipe.name}" />
    <figcaption>
      ${tagsTemplate(recipe.tags)}
      <h2><a href="${recipe.url || '#'}">${recipe.name}</a></h2>
      <p class="recipe__ratings">${ratingTemplate(recipe.rating)}</p>
      <p class="recipe__description">${recipe.description}</p>
    </figcaption>
  </figure>`;
}

// Render one or more recipes to the page
function renderRecipes(recipeList) {
  recipesSection.innerHTML = recipeList.map(recipe => recipeTemplate(recipe)).join('');
}

// Search filter logic
function filterRecipes(query) {
  const filtered = recipes.filter(recipe =>
    recipe.name.toLowerCase().includes(query) ||
    recipe.description.toLowerCase().includes(query) ||
    recipe.tags.find(tag => tag.toLowerCase().includes(query)) ||
    recipe.recipeIngredient.find(ing => ing.toLowerCase().includes(query))
  );

  return filtered.sort((a, b) => a.name.localeCompare(b.name));
}

// Handle search form submit
function searchHandler(e) {
  e.preventDefault();
  const query = searchForm.querySelector('input').value.toLowerCase();
  const results = filterRecipes(query);
  renderRecipes(results);
}

// Initialization function to display one random recipe on load
function init() {
  const randomRecipe = getRandomListEntry(recipes);
  renderRecipes([randomRecipe]);
}

// Event listeners
searchForm.addEventListener('submit', searchHandler);

// Load the page with one random recipe
init();
