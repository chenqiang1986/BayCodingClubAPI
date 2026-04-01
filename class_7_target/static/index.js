
function clickButtonHandler() {
    alert('Button was clicked!');
}

document.getElementById('clickButton').addEventListener('click', clickButtonHandler);


function fileInputHandler(event) {
    const file = event.target.files[0];
    if (file) {
        alert(`Selected file: ${file.path} ${file.name}`);
    } else {
        alert('No file selected.');
    }
}

document.getElementById('fileInput').addEventListener('change', fileInputHandler);