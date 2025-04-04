export const blogPosts = [
    {
        title: "Custom Desktop Computer Build",
        excerpt: "Explore our prebuilt options or create your own custom build from the ground up.",
        excerpt2: "Every PC is hand-built to order by our experienced technicians with care and precision.",
        image: "desktop.jpg"
    },
    {
        title: "Laptop Diagnostic and Repair",
        excerpt: "Don't give up on your broken laptop—our skilled technicians can fix it fast.",
        excerpt2: "We breathe new life into your device so you can get back to what matters most.",
        image: "Laptop Diagnostic and Repair.jpg"
    },
    {
        title: "Computer Consulting Services",
        excerpt: "Not sure what you need? Facing a tech issue you can't solve?",
        excerpt2: "Our experts offer clear, personalized advice to help you make the right decision.",
        image: "Consulting.jpg"
    }
];

// Function to render the blog posts
export function renderBlogPosts() {
    const blogContainer = document.querySelector('.blog-container');
    
    // Clear the container before rendering new posts
    blogContainer.innerHTML = '';
    
    // Render the blog posts
    blogPosts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('blog-post');
        
        postElement.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.excerpt}</p>
            <p>${post.excerpt2}</p>
            <img src="${post.image}" alt="${post.title}" class="blog-post-image">
        `;
        
        blogContainer.appendChild(postElement);
    });
}
