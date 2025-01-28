document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".menu-button");
  const menu = document.querySelector(".menu");
  const gallery = document.querySelector(".gallery");

  // Handle menu toggle
  menuButton.addEventListener("click", () => {
      menu.classList.toggle("visible");
  });

  // Function to show the modal with the selected image
  function viewHandler(event) {
      if (event.target.tagName === "IMG") {
          // Get the src of the clicked image, replace '-sm' with '-full' to get the larger image
          const imageSrc = event.target.src.replace("-sm", "-full"); 
          const altText = event.target.alt;
          const viewerHtml = viewerTemplate(imageSrc, altText);
          document.body.insertAdjacentHTML("afterbegin", viewerHtml);

          // Add event listener to close button
          const closeButton = document.querySelector(".close-viewer");
          closeButton.addEventListener("click", closeViewer);
      }
  }

  // Modal template
  function viewerTemplate(imageSrc, altText) {
      return `
          <div class="viewer active">
              <button class="close-viewer">X</button>
              <img src="${imageSrc}" alt="${altText}">
          </div>
      `;
  }

  // Function to close the modal
  function closeViewer() {
      const viewer = document.querySelector(".viewer");
      viewer.remove();
  }

  // Add event listener for the gallery images
  gallery.addEventListener("click", viewHandler);
});
