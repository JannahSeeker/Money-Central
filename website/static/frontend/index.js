// index.js

// Function to update the background gradient based on mouse position
function updateBackground(event) {
    const mouseX = event.clientX; // Get the mouse X position
    const mouseY = event.clientY; // Get the mouse Y position
    
    const bodyWidth = document.body.clientWidth; // Get the width of the body
    const bodyHeight = document.body.clientHeight; // Get the height of the body
    
    const centerX = bodyWidth / 2; // Calculate the X position of the center of the body
    const centerY = bodyHeight / 2; // Calculate the Y position of the center of the body
    
    // Calculate the angle of the mouse position relative to the center of the body
    const radians = Math.atan2(mouseY - centerY, mouseX - centerX);
    let degrees = radians * (180 / Math.PI);
    
    // Ensure the degree value is within the range of 0 to 360
    if (degrees < 0) {
        degrees += 360;
    }
    
    // Set the background gradient with the calculated degree value
    document.querySelector('.Page').style.backgroundImage = `linear-gradient(${degrees}deg, rgb(226, 198, 145), rgb(146, 219, 219) 94%), radial-gradient(circle,  rgb(56, 218, 218), rgb(255, 255, 255))`;
    document.querySelector('.individual-specialboxes').style.backgroundImage = `linear-gradient(${degrees}deg, rgb(226, 198, 145), rgb(146, 219, 219) 94%), radial-gradient(circle,  rgb(56, 218, 218), rgb(255, 255, 255))`;
    document.getElementById("Settings").style.backgroundImage = `linear-gradient(${degrees+3}deg, rgb(226, 198, 145), rgb(146, 219, 219) 94%), radial-gradient(circle,  rgb(56, 218, 218), rgb(255, 255, 255))`;
    document.getElementById("Logout").style.backgroundImage = `linear-gradient(${degrees+5}deg, rgb(226, 198, 145), rgb(146, 219, 219) 94%), radial-gradient(circle,  rgb(56, 218, 218), rgb(255, 255, 255))`;
    document.getElementById("Help").style.backgroundImage = `linear-gradient(${degrees+7}deg, rgb(226, 198, 145), rgb(146, 219, 219) 94%), radial-gradient(circle,  rgb(56, 218, 218), rgb(255, 255, 255))`;
}


// Update the background when the mouse moves














// Function to update the background gradient based on mouse position
function updateradial(event) {
    const mouseX = event.clientX; // Get the mouse X position
    const mouseY = event.clientY; // Get the mouse Y position    
    const divvy = document.querySelector('.vertical-navbar-created'); // Get the divvy element
    const rect = divvy.getBoundingClientRect(); // Get the size and position of the divvy element
    
    const centerX = rect.left + rect.width / 2; // Calculate the X position of the center of the divvy element
    const centerY = rect.top + rect.height / 2; // Calculate the Y position of the center of the divvy element
    
    const distanceX = mouseX - centerX; // Calculate the distance of the mouse from the center in the X direction
    const distanceY = -1*(mouseY - centerY); // Calculate the distance of the mouse from the center in the Y direction
    
    console.log(distanceX)
    console.log(distanceY)
    // Get the reference to your div
    var divElement = document.getElementById("navbar");

    // Get the width of the div including padding and borders
    var width = divElement.offsetWidth;

    var circleX;
    var circleY;

    // Get the height of the div including padding and borders
    var height = divElement.offsetHeight;
    console.log(height)
    console.log(width)
    // Calculate the angle of the mouse position relative to the center of the divvy element
    circleX = distanceX
    circleY= distanceY
    if (distanceX > (width/2) ) {
        console.log("x is greater than width");
        circleX = (width/2) 
    } 
    if (distanceX < -1*(width/2) ){
        console.log("x is less than width");
        circleX = -1*(width/2) 

    }
    if (distanceY  > (height/2)) {
        console.log("y is greater than height");
        circleY = (height/2) 

    } 
    if (distanceY < -1*(height/2)) {
        console.log("y is less than height");
        circleY = -1*(height/2) 

    }
    circleX = (width/2) + circleX
    circleY = (height/2) - circleY
    console.log(circleX)
    console.log(circleY)
    const gradient = `radial-gradient(circle farthest-side at ${circleX}px ${circleY}px, rgb(255, 165, 0) 1%, rgb(255, 255, 255))`;
    divvy.style.backgroundImage = gradient;
}


window.addEventListener('scroll', function() {
    var fixedDiv = document.getElementById('fixed-position');
    var navbarholderfixedDiv = document.getElementById('navbar-holder');
    var placeholder = document.querySelector('.navbar-card-div');
    var navbarholderplaceholder = document.querySelector('.fixed-module-card-div');

    // Get the position of the fixed div relative to the document
    var fixedDivRect = fixedDiv.getBoundingClientRect();
    var navbarholderfixedDivRect = navbarholderfixedDiv.getBoundingClientRect();
    var fixedDivTop = fixedDivRect.top;
    var navbarholderfixedDivTop = navbarholderfixedDivRect.top;

    // Determine when to fix the div
    if (navbarholderfixedDivTop <= 0) {
        fixedDiv.classList.add('fixed');
        // placeholder.style.display = 'inline'; // Show the placeholder to prevent content jump
        placeholder.style.position = 'fixed'
        placeholder.style.top = '1vh'
        placeholder.style.left = '11.5vw'
        placeholder.style.width = '34.6vw'
        console.log('IT IS!')
    } else {
        fixedDiv.classList.remove('fixed');
        placeholder.style.position = 'relative'
        placeholder.style.top = '0%'
        placeholder.style.left = '0%'
        placeholder.style.width = '100%'

        // placeholder.style.display = 'none'; // Hide the placeholder
        console.log('IT ISNT!')

    }
});

document.getElementById("add-account-button").addEventListener("click", function() {
    document.getElementById("entire-form").style.display = "block";
});

document.getElementById("exit-button").addEventListener("click", function() {
    document.getElementById("entire-form").style.display = "none";
});
// Update the background when the mouse moves
document.addEventListener('mousemove', updateradial);

document.addEventListener('mousemove', updateBackground);
