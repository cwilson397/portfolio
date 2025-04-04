import { blogPosts } from './data.mjs';

document.addEventListener('DOMContentLoaded', () => {
    const blogContainer = document.querySelector('.blog-container');
    
    // Clear the container to ensure no old content remains
    blogContainer.innerHTML = '';

    // Dynamically add the blog posts
    blogPosts.forEach(post => {
        const blogCard = document.createElement('div');
        blogCard.classList.add('blog-card');
        blogCard.innerHTML = `
            <img src="${post.image}" alt="Blog image" class="blog-post-image">
            <h3>${post.title}</h3>
            <p>${post.excerpt}</p>
            <p>${post.excerpt2}</p>
            <a href="#">Read more</a>
        `;
        blogContainer.appendChild(blogCard);
    });
});
