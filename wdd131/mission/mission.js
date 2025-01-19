// Selects the theme selector dropdown and logo image
const themeSelector = document.querySelector("#themeSelector");
const logo = document.querySelector(".logo")

//Function to change the theme
function changeTheme() {
    const theme = themeSelector.value; //Gets the current value
    const body = document.body;

    if (theme === "dark") {
        body.classList.add("dark");
        logo.src = "byui-logo_white.png";
    } else {
        body.classList.remove("dark"); 
        logo.src = "byui-logo_blue.webp";
    }
}

// event listener
themeSelector.addEventListener("change", changeTheme);