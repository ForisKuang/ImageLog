function readURL(input) {
    var files = input.target.files;
    var f = files[0];
    var reader = new FileReader();
     
      reader.onload = (function(theFile) {
            return function(e) {
              document.getElementById('list').innerHTML = ['<img src="', e.target.result,'" title="', theFile.name, '" width="50" />'].join('');
            };
      })(f);
       
      return reader.readAsDataURL(f);
}