tinymce.init({
    selector: '.main',  // Change this value according to your HTML
    plugins: 'textcolor',  // Include the textcolor plugin
    toolbar: 'forecolor backcolor',  // Add buttons for text and background color
    menubar: false,  // Optional: Hide the menu bar if not needed
    height: 500  // Optional: Set the height of the editor
});