<script>
    // Array of image paths
    const images = [
        "images/ZO1_Actin_Myosin_Crop.gif",
        "images/TJ formation after Ca switch (NG-ZO1).gif"
    ];

    // Track the current image index
    let currentIndex = 0;

    // Get the image element
    const heroImage = document.getElementById("hero-image");

    // Function to change the image
    function changeImage() {
        // Increment the index and reset to 0 if it exceeds the array length
        currentIndex = (currentIndex + 1) % images.length;
        // Update the image source
        heroImage.src = images[currentIndex];
    }

    // Automatically change the image every 10 seconds
    setInterval(changeImage, 10000);
</script>
