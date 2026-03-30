
    const imageUpload = document.getElementById('imageUpload');
    const previewContainer = document.getElementById('previewContainer');
    
    // Listen for file selection
    imageUpload.addEventListener('change', handleFileSelect);

    function handleFileSelect(event) {
        const files = event.target.files; // Get selected files
        if (!files.length) return; // Exit if no files selected
    
        processImageFile(files);
    }

    function readFileAsync(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
        
            reader.onload = function(e){
                resolve(e.target.result); // Data URL 
            };
        
            reader.onerror = () => reject(reader.error);
        
            reader.readAsDataURL(file); 
        });
    }

    async function processImageFile(files) {
    
        data_urls = [];
        previewContainer.innerHTML = ""
    
        // Read the file as a data URL
        for (var file of files){
            data_url = await readFileAsync(file)
            data_urls.push(data_url)
            previewContainer.innerHTML += `
                <img src="${data_url}" width="200px" heigth="auto">
            `
        }

        fetch("/process", 
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ key: data_urls })
            }
        )
        .then((response) => response.json())
        .then((json) => {
            console.log(json['status']);
            document.getElementById("MyResult").textContent = json['status'];
        });
    }