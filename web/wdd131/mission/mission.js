// Select the dropdown element
const themeSelector = document.querySelector('#theme-selector');

// Function to handle theme changes
function changeTheme() {
    // check to see what the current value of our select is.
    // The current value is conveniently found in themeSelector.value!
    const body = document.body;
    const logo = document.querySelector('.logo');

    // if the value is dark then:
    if (themeSelector.value === 'dark') {
        // add the dark class to the body
        body.classList.add('dark');
        // change the source of the logo img to point to the white logo.
        logo.src = 'byui-logo_white.png';
    //otherwise
    } else {
        // remove the dark class from the body
        body.classList.remove('dark');
        // make sure the logo src is the blue logo.
        logo.src = 'byui-logo_blue.webp';
    }
}

// add an event listener to the themeSelector element
// Use the changeTheme function as the event handler function.
themeSelector.addEventListener('change', changeTheme);