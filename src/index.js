let JSZip = require("jszip");

// Get input element
let inputRef = document.getElementById('my-input')

// Add listener to listen for file changes 
inputRef.addEventListener('change', (evt) => {
    // Get filelist
    let files = evt.target.files

    // Assign new zip object
    let zip = new JSZip()

    // Loop through the filelist to get each filename and pass each file to zip object
    for(let file of files){ 
        let filename = file.name
        zip.file(filename, file)
    }

    // Generate the complete zip file
    zip.generateAsync({type:'blob'}).then((blobdata)=>{
        // create zip blob file
        let zipblob = new Blob([blobdata])

        // For development and testing purpose
        // Download the zipped file 
        var elem = window.document.createElement("a")
        elem.href = window.URL.createObjectURL(zipblob)
        elem.download = 'compressed.zip'
        elem.click()
    })

})