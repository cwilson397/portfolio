import recipes from './recipes.mjs';

document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search");
    const clearButton = document.getElementById("clear-search");
    const recipeList = document.getElementById("recipe-list");

    // Function to display recipes
    const displayRecipes = (recipesArray) => {
        recipeList.innerHTML = ''; // Clear previous content
        recipesArray.forEach(recipe => {
            const recipeElement = document.createElement('div');
            recipeElement.classList.add('recipe-item'); // Add a class for styling

            recipeElement.innerHTML = `
                <img src="${recipe.image}" alt="${recipe.name}">
                <div class="recipe-info">
                    <h3>${recipe.name}</h3>
                    <p>${recipe.description}</p>
                    <div class="tags">
                        ${recipe.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                    </div>
                    <div class="rating" role="img" aria-label="Rating: ${recipe.rating} out of 5 stars">
                        ${'⭐'.repeat(recipe.rating)}${'☆'.repeat(5 - recipe.rating)}
                    </div>
                </div>
            `;
            recipeList.appendChild(recipeElement);
        });
    };

    // Display all recipes initially
    displayRecipes(recipes);

    // Clear the search input when the clear button is clicked
    clearButton.addEventListener("click", () => {
        searchInput.value = "";
        displayRecipes(recipes); // Show all recipes when search is cleared
    });

    // Filter recipes based on search input
    searchInput.addEventListener("input", () => {
        const searchTerm = searchInput.value.toLowerCase();
        const filteredRecipes = recipes.filter(recipe =>
            recipe.name.toLowerCase().includes(searchTerm) || 
            recipe.description.toLowerCase().includes(searchTerm)
        );
        displayRecipes(filteredRecipes);
    });
});
