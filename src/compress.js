let JSZip = require("jszip");
var zip = new JSZip();
var count = 0;
var zipFilename = "zipFilename.zip";
var urls = [
  'features\steps\apiTestingStep.py',
  'features\steps\intersectionStep.py'
];

urls.forEach(function(url){
  var filename = "filename";
  // loading a file and add it in a zip file
  JSZipUtils.getBinaryContent(url, function (err, data) {
     if(err) {
        throw err; // or handle the error
     }
     zip.file(filename, data, {binary:true});
     count++;
     if (count == urls.length) {
       zip.generateAsync({type:'blob'}).then(function(content) {
          saveAs(content, zipFilename);
       });
    }
  });
});