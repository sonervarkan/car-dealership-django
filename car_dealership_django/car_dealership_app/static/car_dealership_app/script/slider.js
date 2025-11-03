const slider_img = document.getElementById("slider-image");
const brand = document.querySelector(".brand");
const model = document.querySelector(".model");
const year = document.querySelector(".year");

let carIndex = 0;   
let imageIndex = 0;   

function updateSlider() {
    const currentCar = vehicles[carIndex];
    const currentImage = currentCar.images[imageIndex];

    slider_img.src = currentImage;
    brand.textContent = "Brand: " + currentCar.brand;
    model.textContent = "Model: " + currentCar.model;
    year.textContent = "Year: " + currentCar.year;
}


if (vehicles.length > 0 && vehicles[0].images.length > 0) {
    updateSlider();

    setInterval(() => {
     
        imageIndex++;
        if (imageIndex >= vehicles[carIndex].images.length) {
            imageIndex = 0;
            carIndex = (carIndex + 1) % vehicles.length; 
        }
        updateSlider();
    }, 1500);
} else {
    console.warn("No vehicle images found.");
}
